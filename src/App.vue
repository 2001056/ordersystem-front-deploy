<!-- 화면의 요소는 template안에 작업 -->
<template>
<!-- vuetify에서는 모든 태그의 최상단에 v-app으로 감싸져있어야 정상적으로 동작 -->
<v-app>
  <HeaderComponent/>
  <!-- router-view는 현재 url 에 매칭된 컴포넌트를 렌더링(화면생성)하는 영역 -->
    <v-main>
      <router-view/>
    </v-main>
  <FooterComponent/>
</v-app>
</template>

<!-- js의 요소는 script안에 작업 -->
<script>
import FooterComponent from './components/FooterComponent.vue';
import HeaderComponent from './components/HeaderComponent.vue';

// vue는 export를 통하여 .vue, .js 등의 요소를 다른 화면에서도 import할수 있도록 설정.
export default {
  // name을 생략시 파일명이 name이 됨.
  name: "App",
  components:{
    HeaderComponent, FooterComponent
  }
}
</script>

<!-- css의 요소는 style안에 작업 -->
<style>
</style>
