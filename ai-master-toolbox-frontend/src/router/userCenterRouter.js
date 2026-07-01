export default [
  {
    path: "/user",
    name: "user",
    component: () => import("../views/user/UserView.vue"),
    children: [
      {
        path: "desk",
        name: "UserViewDesk",
        component: () => import("../views/user/UserViewDesk.vue"),
        children: [
          {
            path: "MyMessage",
            name: "MyMessage",
            component: () =>
              import("../components/userView/Desk/MyMessage.vue"),
          },
          {
            path: "PersonalInformation",
            name: "PersonalInformation",
            component: () =>
              import("../components/userView/Desk/PersonalInformation.vue"),
          },
          // 问题反馈
          {
            path: "ProblemFeedback",
            name: "ProblemFeedback",
            component: () =>
              import(
                "../components/userView/Desk/ProblemFeedback/ProblemFeedbackHome.vue"
              ),
          },
          // 反馈弹窗
          {
            path: "FeedbackPop-ups",
            name: "FeedbackPop-ups",
            component: () =>
              import(
                "../components/userView/Desk/ProblemFeedback/FeedbackPop-ups"
              ),
          },
          // 详情弹窗
          {
            path: "DetailsPop-up",
            name: "DetailsPop-up",
            component: () =>
              import(
                "../components/userView/Desk/ProblemFeedback/DetailsPop-up.vue"
              ),
          },
          {
            path: "Recharge",
            name: "Recharge",
            component: () => import("../components/userView/Desk/Recharge.vue"),
          },
        ],
      },
      {
        path: "mobile",
        name: "UserViewMobile",
        component: () => import("../views/user/UserViewMobile.vue"),
        children: [
          {
            path: "PersonalInformation",
            name: "PersonalInformationMobile",
            component: () =>
              import("../components/userView/Mobile/PersonalInformation.vue"),
          },
          {
            path: "ProblemFeedbackHome",
            name: "ProblemFeedbackHomeMobile",
            component: () =>
              import(
                "../components/userView/Mobile/ProblemFeedback/ProblemFeedbackHome.vue"
              ),
          },
          // 反馈弹窗
          {
            path: "FeedbackPop-ups_Mobile",
            name: "FeedbackPop-ups_Mobile",
            component: () =>
              import(
                "../components/userView/Mobile/ProblemFeedback/FeedbackPop-ups.vue"
              ),
          },
          // 详情弹窗
          {
            path: "DetailsPop-up_Mobile",
            name: "DetailsPop-up_Mobile",
            component: () =>
              import(
                "../components/userView/Mobile/ProblemFeedback/DetailsPop-up.vue"
              ),
          },
          {
            path: "Recharge",
            name: "RechargeMobile",
            component: () =>
              import("../components/userView/Mobile/Recharge.vue"),
          },
        ],
      },
    ],
  },
];
