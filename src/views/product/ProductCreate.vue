<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="6">
                <v-card>
                    <v-card-title class="text-h5-">상품등록</v-card-title>
                    <v-card-text>
                        <v-form>
                            <v-text-field label="상품명"
                            v-model="name"/>
                            <v-text-field label="카테고리"
                            v-model="category"/>
                            <v-text-field label="가격"
                            v-model.number="price"/>
                            <v-text-field label="재고수량"
                            v-model.number="stockQuantity"/>
                            <v-file-input label="상품이미지"
                            @change="fileUpload" multiple/>
                            <v-row>
                                <v-col>
                                    <v-btn color="secondary" block @click="productCreate()">등록</v-btn>
                                </v-col>
                            </v-row>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';

    export default {
        data() {
            return{
                name: null,
                category: null,
                price: 0,
                stockQuantity: 0,
                productImage: null,
            }
        },
        methods: {
            // event객체에 업로드할 파일이 주입
            fileUpload(event) {
                // 여러개의 이미지일 경우 for문을 실행하여 productImage에 리스트형태로 push
                this.productImage = event.target.files[0];
            },
            async productCreate() {
                try {
                    // multi-part-Formdata 또는 url인코딩 방식인 경우, FormData클래스 사용
                    const data = new FormData();
                    data.append("name", this.name);
                    data.append("category", this.category);
                    data.append("price", this.price);
                    data.append("stockQuantity", this.stockQuantity);
                    // image를 아예 append 시키지 않으면, 백엔드 dto에 null로 매핑되나, null을 append시키면 백엔드에서 타입에러 발생
                    if(this.productImage) {
                        data.append("productImage", this.productImage);
                    } 
                    await axios.post(`${process.env.VUE_APP_API_BASE_URL}/product/create`, data);
                    this.$router.push("/product/list");
                } catch (e) {
                    alert(e.response.data.error_message);
                }
            }
        }
    }
</script>

<style>

</style>