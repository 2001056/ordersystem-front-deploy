<template>
    <h1>store component B</h1>
    <div>지역변수값 : {{ count }}</div>
    <v-btn @click="incrementCount()">지역변수 count값 증가</v-btn>
    <div>전역변수값 : </div>
</template>
<script>
export default{
    data() {
        return{
            count: 0
        }
    },
    methods: {
        incrementCount() {
            this.count++;
        }
    }
}
</script>