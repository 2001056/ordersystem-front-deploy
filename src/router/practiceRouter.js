import TestVue from "@/components/practice/0_TestVue.vue";
import TestVue2 from "@/components/practice/0_TestVue2.vue";
import ModelingComponent from "@/components/practice/1_ModelingComponent.vue";
import ConditionalComponent from "@/components/practice/2_ConditionalComponent.vue";
import HookComponent from "@/components/practice/3_HookComponent.vue";
import VuetifyComponent from "@/components/practice/4_VuetifyComponent.vue";
import RouteComponent from "@/components/practice/5_RouteComponent.vue";
import RouteComponent2 from "@/components/practice/5_RouteComponent2.vue";
import RouteComponent3 from "@/components/practice/5_RouteComponent3.vue";
import StoreTestComponent from "@/components/practice/6_StoreTestComponent.vue";


export const practiceRouter = [
    {
        path: "/practice/test",
        name: "TestVue",
        component: TestVue
    },
    {
        path: "/practice/test2",
        name: "TestVue2",
        component: TestVue2
    },
    {
        path: "/practice/modeling",
        name: "ModelingComponent",
        component: ModelingComponent
    },
    {
        path: "/practice/conditional",
        name: "ConditionalComponent",
        component: ConditionalComponent
    },
    {
        path: "/practice/hook",
        name: "HookComponent",
        component: HookComponent
    },
    {
        path: "/practice/vuetify",
        name: "VuefifyCompent",
        component: VuetifyComponent
    },
    {
        path: "/practice/route",
        name: "RouteComponent",
        component: RouteComponent
    },{
        path: "/practice/route2",
        name: "RouteComponent2",
        component: RouteComponent2
    },
    {
        path: "/practice/route3/:productId",
        name: "RouteComponent3",
        component: RouteComponent3
    },
    {
        path: "/practice/store",
        name: "StoreTestComponent",
        component: StoreTestComponent
    },
]