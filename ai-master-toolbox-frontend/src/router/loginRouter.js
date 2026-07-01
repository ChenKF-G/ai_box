export default [
  {
    path: "/login",
    name: "login",
    redirect: { name: "loginDesk" },
    children: [
      {
        path: "desk",
        name: "loginDesk",
        component: () => import("../views/login/LoginViewDesk.vue"),
      },
      {
        path: "mobile",
        name: "loginMobile",
        component: () => import("../views/login/LoginViewMobile.vue"),
      },
    ],
  },
];
