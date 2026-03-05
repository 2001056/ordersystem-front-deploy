<template>
    <v-app-bar>
        <v-container>
            <v-row>
                <v-col class="d-flex justify-start">
                    <div v-if="userRole==='ADMIN'">
                        <v-btn :to="'/member/list'">회원관리</v-btn>
                        <v-btn :to="'/product/manage'">상품관리</v-btn>
                        <v-btn :href="`/order/list`">실시간주문건수 {{ liveOrderCount }}</v-btn>
                    </div>
                </v-col>
                
                <v-col class="text-center">
                    <v-btn :to="`/`"> vue shop </v-btn>
                    </v-col>
                <v-col class="d-flex justify-end">
                    <v-btn v-if="isLogined" :to="'/order/cart'">장바구니 {{ totalQuantity }}</v-btn>
                    <v-btn :to="'/product/list'">상품목록</v-btn>
                    <v-btn v-if="isLogined" :to="'/member/mypage'">마이페이지</v-btn>
                    <v-btn v-if="!isLogined" :to="'/member/create'">회원가입</v-btn>
                    <v-btn v-if="!isLogined" :to="'/member/login'">로그인</v-btn>
                    <v-btn v-if="isLogined" @click="doLogout()">로그아웃</v-btn>
                </v-col>
            </v-row>
        </v-container>
    </v-app-bar>
</template>
<script>
import { cartStore } from '@/store/cart';
import { EventSourcePolyfill } from 'event-source-polyfill';
import { jwtDecode } from 'jwt-decode';
import axios from 'axios';
    export default{
        data(){
            return{
                userRole: null,
                isLogined: false,
                liveOrderCount:0,
            }
        },
        created() {
            const accessToken = localStorage.getItem("accessToken");
            if(accessToken){
                const payload = jwtDecode(accessToken);
                this.userRole=(payload.role);
                this.isLogined=true;
            }
            if(this.userRole==='ADMIN'){
                this.sseConnect();
            }
        },
        computed:{
            totalQuantity(){
                const store = cartStore();
                return store.getTotalQuantity;
            }
        },
        methods:{
            sseConnect() {
            const accessToken = localStorage.getItem("accessToken");
            const sse = new EventSourcePolyfill(`${process.env.VUE_APP_API_BASE_URL}/sse/connect`, {
                headers: { Authorization: `Bearer ${accessToken}` }
            });

            sse.addEventListener('connect', (event) => {
                console.log(event);
            });

            sse.addEventListener('ordered', (event) => {
                console.log(event);
                this.liveOrderCount++;
            });
                
            // sse연결해제를위한 이벤트 설정
            window.addEventListener("beforeunload",this.disconnect);   
            },
            async disconnect(){
                await axios.get(`${process.env.VUE_APP_API_BASE_URL}/sse/disconnect`,)

            },
            doLogout(){
                localStorage.clear();
                this.isLogined = false;
                this.userRole = null;
                this.$router.push("/");
            }

        }
    }
</script>