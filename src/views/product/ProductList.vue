<template>
    <v-container>
        <v-row class="d-flex justify-content-between mt-5">
            <v-col>
                <v-form>
                    <v-row>
                        <v-col cols="auto">
                            <v-select
                            v-model="searchType"
                            :items="searchOptions"
                            item-title="text"
                            item-value="value"/>
                        </v-col>
                        <v-col>
                            <v-text-field
                            v-model="searchValue"
                            label="검색어"
                            @keyup.enter="searchProduct"
                            />
                        </v-col>
                        <v-col cols="auto">
                            <v-btn @click="searchProduct()">검색</v-btn>
                        </v-col>
                    </v-row>
                </v-form>
            </v-col>
            <v-col cols="auto" v-if="!isAdmin">
                <v-btn color="primary" @click="addCart()">장바구니</v-btn>
                <v-btn color="secondary" @click="createOrder()">주문하기</v-btn>
            </v-col>
            <v-col cols="auto" v-if="isAdmin">
                <v-btn :to="'/product/create'" color="primary">상품등록</v-btn>
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <v-card>
                    <v-card-title class="text-center text-h5">
                        {{pageTitle}}
                        </v-card-title>
                    <v-card-text>
                        <v-table>
                            <thead>
                                <tr><th>제품사진</th><th>제품명</th><th>가격</th><th>재고수량</th><th>주문수량</th><th>Action</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="product in productList" :key="product.id">
                                    <td><v-img :src="product.imagePath"/></td>
                                    <td>{{product.name}}</td>
                                    <td>{{product.price}}</td>
                                    <td>{{product.stockQuantity}}</td>
                                    <td><v-text-field type="number" style="width: 65px;" v-model.number="product.productCount"/></td>
                                    <td><input type="checkbox" v-model="product.selected"></td>
                                </tr>
                            </tbody>
                        </v-table>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import { cartStore } from '@/store/cart';
import axios from 'axios';

    export default{
        // 화면을 호출하는 쪽에서 넘긴 props 변수를 아래와 같이 받아서 변수로 사용 가능 
        props: ['isAdmin','pageTitle'],
        data() {
            return{
                isLastPage: false,
                isLoading: false,
                pageSize : 5,
                pageNumber : 0,
                productList: [],
                searchType: "optional",
                searchValue: "",
                searchOptions: [{text:"선택", value:"optional"},{text:"상품명", value:"productName"},{text:"카테고리", value:"category"}]
            }
        },
        created(){
            this.loadData();
            window.addEventListener("scroll", this.scrollPaging);
        },
        methods: {
            addCart(){
                const store = cartStore();
                const data = this.productList.filter(p=>p.selected && p.productCount>0).map(p=>({productId:p.id,productName:p.name, productCount:p.productCount,price:p.price}));
                data.forEach(p=>store.addCart(p));
            },
            scrollPaging() {
                // 현재화면높이 + 스크롤로 이동한 거리 > 전체화면높이-n이 성립하면 추가 데이터 로드
                const isBottom = window.innerHeight + window.scrollY > document.body.offsetHeight - 220;
                if (isBottom && !this.isLoading && !this.isLastPage) {
                    this.loadData();
                }
            },
            searchProduct() {
                this.isLastPage = false;
                this.isLoading = false;
                this.pageNumber = 0;
                this.productList = [];
                this.loadData();
            },
            async loadData() {
                try {
                    this.isLoading = true;
                    // params라는 이름의 객체를 사용하여 쉽게 파라미터형식으로 url 조립
                    // 예시) http://localhost:8080/product/list?size=10&page=1&productName=apple
                    let params= {size: this.pageSize, page: this.pageNumber};
                    if(this.searchType==="productName") {
                        params.productName = this.searchValue;
                    }
                    if(this.searchType==="category") {
                        params.category = this.searchValue;

                    }
                    const result = await axios.get(`${process.env.VUE_APP_API_BASE_URL}/product/list`, {params});
                    const additionalData = result.data.content.map(p=>({...p, productCount:0, selected: false}));
                    if(additionalData.length == 0) {
                        this.isLastPage = true;
                    }
                    this.productList = [...this.productList, ...additionalData];
                    this.pageNumber++;
                    this.isLoading = false;
                } catch(e) {
                    console.log(e);
                }
            },
            async createOrder() {
                try {
                    const data = this.productList.filter(p=>p.selected && p.productCount>0).map(p=>({productId:p.id, productCount:p.productCount}));
                    if (data.length > 0) {
                        await axios.post(`${process.env.VUE_APP_API_BASE_URL}/ordering/create`, data);
                        alert("주문이 완료되었습니다.");
                        window.location.reload();
                    }
                } catch(e) {
                    console.log(e);
                    alert("주문이 실패되었습니다.");
                }
            }
        }
    }
</script>