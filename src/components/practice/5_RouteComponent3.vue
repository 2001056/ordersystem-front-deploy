<template>
    <div>라우트3화면</div>

</template>

<script>
export default{
    data(){
        return{

        }
    },
    created(){
        this.id = this.$route.params.productId;
        console.log(this.id);
        // const result = axios.get("http://localhost:8080/product/detail/"+this.id);
        // console.log(result);
    },
}
</script>
