import { defineStore } from "pinia";


export const practiceStore = defineStore('practice',{

    // 상태 초기화
    state: () => ({
        count: 0
    }),
    // 상태값을 변경하는 메서드
    actions: {
        incrementCount() {
            this.count++;
        }
    },
    // 상태값을 가져가기위한 메서드
    getters: {
        getCount: state => state.count
    }
})