<template>
<div>testvue2</div>
<TestVue/>
</template>
<script>
import TestVue from './0_TestVue.vue';

export default{
    // 다른 화면을 import하여 현재 화면에서 사용하려고 할때는 components에 다른 화면 나열
    components:{
        TestVue
    },
    data(){
        return{
        }
    },
    methods:{
        
    }
}
</script>
<style>
</style>