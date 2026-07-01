import { createRouter, createWebHashHistory } from "vue-router";
import homeRouter from "./homeRouter";
import loginRouter from "./loginRouter";
import adminRouter from "./adminRouter";
import gptRouter from "./gptRouter";
import userCenterRouter from "./userCenterRouter";
import idPhotoRouter from "./idPhotoRouter";

const routes = [
  ...homeRouter,
  ...loginRouter,
  ...adminRouter,
  ...gptRouter,
  ...userCenterRouter,
  ...idPhotoRouter,
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
