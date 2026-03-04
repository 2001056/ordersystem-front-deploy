<template>
    <v-container>
        <v-row>
            <v-col>
                <v-card>
                    <v-card-title class="text-center text-h5">
                        회원상세조회
                    </v-card-title>
                    <v-card-text>
                        <v-table>
                            <tbody>
                                <tr><td>ID : </td><td>{{member.id}}</td></tr>
                                <tr><td>NAME : </td><td>{{member.name}}</td></tr>
                                <tr><td>EMAIL : </td><td>{{member.email}}</td></tr>
                            </tbody>
                        </v-table>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import axios from 'axios';

export default{
    props:['isMyPage'],
    data(){
        return{
            member: {},
        }
    },
    async created(){
        try{
            if(this.isMyPage){
                const result = await axios.get(`${process.env.VUE_APP_API_BASE_URL}/member/myinfo`);
                this.member = result.data;
            }else{
                const id = this.$route.params.memberId;
                const result = await axios.get(`${process.env.VUE_APP_API_BASE_URL}/member/detail/${id}`);
                this.member = result.data;
            }
        
        } catch(e){
            console.log(e);
        }
    }
}
</script>