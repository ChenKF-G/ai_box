export default [
  {
    path: "/",
    name: "home",
    redirect: { name: "HomeViewDesk" },
    children: [
      {
        path: "desk",
        name: "HomeViewDesk",
        component: () => import("../views/home/HomeViewDesk.vue"),
      },
      {
        path: "mobile",
        name: "HomeViewMobile",
        component: () => import("../views/home/HomeViewMobile.vue"),
      },
    ],
  },
];
