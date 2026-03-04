<template>
    <!-- 단방향바인딩 : 변수 -> 화면 -->
    <h1>hello world {{language}}</h1>
    <!-- 양방향바인딩 : 변수 -> 화면, 화면 -> 변수, v-model문법사용 -->
    <input type="text" v-model="language2">
    <button @click="showValue()">변수확인</button>
</template>

<script>
export default{
    data(){
        return{
            language: "java",
            language2: "java",
        }
    },
    methods:{
        showValue(){
            console.log(this.language2);
        }
    }
}
</script>