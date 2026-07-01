import { createApp } from "vue";
import App from "./App.vue";
//引入路由
import router from "@/router";  

//引入Element库
import ElementPlus from "element-plus";
//引入Element样式
import "element-plus/dist/index.css";
//引入图标
import * as ElementPlusIconsVue from "@element-plus/icons-vue";
// 引入vuex
import store from "@/store";
import VueDevice from "vue-device";
import fetchDataPlugin from "./plugins/fetchDataPlugin";

const app = createApp(App);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}
// 使用vuex
app.use(store);
//使用路由
app.use(router);
//使用插件
app.use(ElementPlus);
app.use(fetchDataPlugin, { store }); // 使用插件并传入 store
app.use(VueDevice);

app.mount("#app");
