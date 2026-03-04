<template>
    <h1>vue 조건식</h1>
    <button v-if="!isLogined" @click="doLogin()">로그인버튼</button>
    <button v-if="isLogined" @click="doLogout()">로그아웃버튼</button>

    <h1>vue 반복문</h1>
    <h1>상품목록조회</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>상품명</th>
                <th>상품가격</th>
            </tr>
        </thead>
        <tbody>
            <!-- v-for를 통한 반복문 사용시, 유일한 key값 설정이 필요 -->
            <tr v-for="product in productList" :key="product.id">
                <td>{{product.id}}</td>
                <td>{{product.name}}</td>
                <td>{{product.price}}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios';
export default{
    data(){
        return{
            isLogined: false,
            productList:[]
        }
    },
    // created : 화면이 생성되기 직전에 자동실행되는 함수
    async created(){
        const result = await axios.get("http://localhost:8080/product/list");
        this.productList = result.data.content;
    },
    // 아래 메서드는 실행요청을 받아야 실행되는 코드
    methods:{
        doLogin(){
            this.isLogined = true;
        },
        doLogout(){
            this.isLogined = false;
        }
    }
}
</script>