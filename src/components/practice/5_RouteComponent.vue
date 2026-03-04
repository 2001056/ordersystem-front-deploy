<template>
    <v-btn href="/practice/route2">일반 라우팅</v-btn>
    <v-btn @click="hrefRouting()">일반 라우팅(함수)</v-btn>
    <v-btn :to="'/practice/route2'">SPA 경로 기반 라우팅</v-btn>
    <v-btn @click="spaRouting1()">SPA 경로 기반 라우팅(함수)</v-btn>
    <v-btn :to="{name:'RouteComponent2'}">SPA 이름 기반 라우팅</v-btn>
    <v-btn @click="spaRouting2()">SPA 이름 기반 라우팅(함수)</v-btn>
    <v-btn @click="goToProduct()">상세조회</v-btn>
</template>
<script>
    export default{
        data() {
            return{
                id:1,
            }
        },
        methods: {
            hrefRouting() {
                // 화면전체에 새로고침이 발생하는 라우팅방식.
                // 특징1. 화면상에 모든 컴포넌트가 새롭게 created 특징2. 화면에 깜빡임으로 인해 사용자경험이 떨어질 수 있음.
                window.location.href="/practice/route2";
            },
            spaRouting1() {
                // spa 방식 : single page application
                // 특징1. 새롭게 라우트되는 컴포넌트만 created 특징2. 새로고침없는 페이지로드
                this.$router.push("/practice/route2");
            },
            spaRouting2() {
                this.$router.push({name:'Route2Component'});
            },
            goToProduct() {
                this.$router.push("/practice/route3/" + this.id);
            }
        }
    }
</script>