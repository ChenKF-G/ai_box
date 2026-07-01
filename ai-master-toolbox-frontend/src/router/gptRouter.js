export default [
  {
    path: "/gpt",
    name: "gpt",
    redirect: { name: "gptDesk" },
    children: [
      {
        path: "desk",
        name: "gptDesk",
        component: () => import("../views/gpt/gptDesk.vue"),
      },
      {
        path: "mobile",
        name: "gptMobile",
        component: () => import("../views/gpt/gptMobile.vue"),
      },
    ],
  },
];
