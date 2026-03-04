import ProductCreate from "@/views/product/ProductCreate.vue";
import ProductList from "@/views/product/ProductList.vue";




export const productRouter=[
    {
        path: "/product/create",
        name: "ProductCreate",
        component: ProductCreate
    },
    {
        path: "/product/list",
        name: "ProductList",
        component: ProductList,
        props: {isAdmin : false, pageTitle:"상품목록"}
    },
    {
        path: "/product/manage",
        name: "ProductManage",
        component: ProductList,
        props: {isAdmin : true, pageTitle:"상품관리"}
    },

    
    
]