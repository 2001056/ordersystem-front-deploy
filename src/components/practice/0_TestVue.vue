<template>
    <div>HTML화면</div>
    <!-- 화면내에서 변수를 사용할때에는 {{}} 사용 -->
    <div>{{name}}</div>
    <div>{{email}}</div>
    <!-- @click : 이벤트요소 -->
    <button @click="test()">test함수 호출</button>
</template>
<script>
export default{
    // 컴포넌트의 이름
    name: "TestVue",
    // 컴포넌트내에서 사용할 변수정의
    data(){
        return{
            name: "hongildong",
            email: "hong@naver.com"
        }
    },
    // 컴포넌트내에서 사용할 함수(메서드) 정의
    methods:{
        test(){
            console.log("hello world");
            // vue에서 전역변수에 접근할때에는 template에서는 this키워드 없이 접근이 가능하지만, 메서드에서는 this키워드 필요
            console.log(this.name);
            console.log(this.email);
        }
    }
}
</script>
<style>
</style>