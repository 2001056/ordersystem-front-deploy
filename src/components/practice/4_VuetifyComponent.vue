<template>
    <v-container>
        <v-row>
            <v-col cols="8">helloworld1</v-col>
            <v-col cols="4">helloworld2</v-col>
        </v-row>
        <v-row>
            <v-card>
                <v-card-title>
                    회원가입
                </v-card-title>
                <v-card-text>
                    회원가입을 해 주세요
                </v-card-text>
            </v-card>
        </v-row>
        <v-row>
            <v-simple-table>
                <thead>
                    <tr>
                    <th>이름</th>
                    <th>이메일</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>test</td><td>test@naver.com</td></tr>
                    <tr><td>test2</td><td>test2@naver.com</td></tr>
                </tbody>
            </v-simple-table>
        </v-row>
        <v-row>
            <v-card>
                <!-- vuetify와 순수css를 함께 적용하는것은 가능. 그러나, 원하는 정확한 디자인을 적용하기 위해서는 일반적으로 순수css만을 사용한다. -->
                <v-card-title class="abc" id = "signup-title" style="font-size:30px">
                    회원가입
                </v-card-title>
                <v-card-text>
                    <v-form>
                        <v-text-field label="name" type="text" ></v-text-field>
                        <v-text-field
                        label="email"
                        type="email">
                        </v-text-field>
                        <v-text-field
                        label="password"
                        type="password"
                        ></v-text-field>
                        <v-btn color ="secondary">제출하기</v-btn>
                    </v-form>
                </v-card-text>
            </v-card>
        </v-row>
        <v-btn @click="basicPopup()">기본팝업</v-btn>
        <v-btn @click="cancel()">모달창(취소버튼)</v-btn>
        <!-- v-dialog는 내부적으로 true/false값을 가지고 외부에 공개될지 말지 여부가 결정 -->
        <v-dialog v-model="trueOrFalse" max-width="400px">
            <v-card>
                <v-card-title>
                    정말 취소하시겠습니까
                </v-card-title>
                <v-card-actions>
                    <v-btn color="primary">예</v-btn>
                    <v-btn color="secondary">아니오</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script>
export default{
    data(){
        return{
            trueOrFalse:false
        }
    },
    methods:{
        basicPopup(){
            alert("hello world")
        },
        cancel(){
            this.trueOrFalse=true;
        }
    }

}
</script>
<style>
#signup-title{
    color:grey

}
.abc{
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

</style>