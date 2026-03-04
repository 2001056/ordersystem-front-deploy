<template>
    <v-container>
        <v-row>
            <v-col>
                <v-card>
                    <v-card-title class="text-center text-h5">
                        주문목록
                    </v-card-title>
                    <v-card-text>
                        <v-data-table
                        :headers="tableHeaders"
                        :items="orderList"
                        show-expand
                        >
                            <!-- template은 v-data-table에서 슬롯(slot)을 커스터마이징하는 문법 -->
                            <template v-slot:expanded-row="{ item, columns }">
                                <tr> 
                                    <!-- colspan은 컬럼을 하나로 합한것 -->
                                    <td :colspan="columns.length">
                                    <!-- <v-icon size="small" >mdi-package</v-icon> -->
                                    <strong>상세내역:</strong>
                                    <span v-for="detail in item.orderDetails" :key="detail.detailId">
                                        {{ detail.productName }} {{ detail.productCount }}개, 
                                    </span>
                                    </td>
                                </tr>
                            </template>
                        </v-data-table>
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
        return {
            tableHeaders:[{title:"ID", key:"id"},{title:"회원EMAIL", key:"memberEmail"}, {title:"주문상태", key:"orderStatus"} ],
            orderList:[]
        }
    },
    async created(){
        try{
            if(this.isMyPage){
                const result = await axios.get(`${process.env.VUE_APP_API_BASE_URL}/ordering/myorders`);
                this.orderList = result.data;
            }
            else{
                const result = await axios.get(`${process.env.VUE_APP_API_BASE_URL}/ordering/list`);
                this.orderList = result.data;
            }
        }
        catch(e){
            console.log(e);
        }
    }
}

</script>