import { createRouter, createWebHistory } from "vue-router";
import { practiceRouter } from "./practiceRouter";
import { memberRouter } from "./memberRouter";
import { productRouter } from "./productRouter";
import { orderRouter } from "./orderRouter";

// routes에서는 url경로와 화면을 매핑
const routes = [
    ...productRouter,
    ...practiceRouter,
    ...memberRouter,
    ...orderRouter,
]

// 일반적으로 .js에서는 export default가 아닌, named export 방식 사용. .vue에서는 export default 사용.
export const router = createRouter(
    {
        // vue route방법은 크게 2가지 종류
        // 1)createWebHistory : http://localhost:3000/member/create 2)createWebHashHistory : http://localhost:3000/#/member/create 
        history: createWebHistory(),
        routes
    }
)