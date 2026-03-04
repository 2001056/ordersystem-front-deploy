<template>
    <MemberDetail
    :isMyPage="true"
    />
    <OrderList
    :isMyPage="true"
    />
</template>

<script>
import OrderList from '../order/OrderList.vue';
import MemberDetail from './MemberDetail.vue';

export default {
    components: {
        MemberDetail,
        OrderList
    }
}
</script>