import OrderCart from "@/views/order/OrderCart.vue";
import OrderList from "@/views/order/OrderList.vue";



export const orderRouter=[
    {
        path: "/order/list",
        name: "OrderList",
        component: OrderList
    },
    {
        path: "/order/cart",
        name: "OrderCart",
        component: OrderCart
    },
    
    
]