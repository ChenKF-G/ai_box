export default [
  {
    path: "/admin",
    name: "admin",
    redirect: { name: "adminDesk" },
    children: [
      {
        path: "desk",
        name: "adminDesk",
        component: () => import("@/views/admin/AdminViewDesk.vue"),
        redirect: { name: "DataStatisticsDesk" },
        children: [
          {
            path: "AccountManages",
            name: "AccountManagesDesk",
            redirect: { name: "AccountManageDesk" },
            children: [
              {
                path: "AccountManage",
                name: "AccountManageDesk",
                component: () =>
                  import(
                    "@/components/adminview/AccountMange/AccountMangePage/AccountManageViewDesk.vue"
                  ),
              },
              {
                path: "Details:id",
                name: "UserDetailsDesk",
                component: () =>
                  import(
                    "@/components/adminview/AccountMange/UserDetailsPage/UserDetailsDesk.vue"
                  ),
              },
            ],
          },
          {
            path: "DataStatistics",
            name: "DataStatisticsDesk",
            component: () =>
              import(
                "@/components/adminview/DataStatistics/DataStatisticsViewDesk.vue"
              ),
            redirect: { name: "UserDataDesk" },
            children: [
              {
                path: "UserData",
                name: "UserDataDesk",
                component: () =>
                  import(
                    "@/components/adminview/DataStatistics/UserDataChartPage/UserDataChartViewDesk.vue"
                  ),
              },
            ],
          },
          {
            path: "Order",
            name: "OrderDesk",
            component: () =>
              import(
                "@/components/adminview/Order/OrderTable/OrderViewDesk.vue"
              ),
          },
          {
            path: "Feedbacks",
            name: "FeedbacksDesk",
            redirect: { name: "FeedbackDesk" },
            children: [
              {
                path: "Feedback",
                name: "FeedbackDesk",
                component: () =>
                  import(
                    "@/components/adminview/Feedback/FeedbackPage/FeedbackViewDesk.vue"
                  ),
              },
              {
                path: "FeedbackDetails:id",
                name: "FeedbackDetailsDesk",
                component: () =>
                  import(
                    "@/components/adminview/Feedback/FeedbackDetailsPage/FeedbackDetailsViewDesk.vue"
                  ),
              },
            ],
          },
        ],
      },
      {
        path: "mobile",
        name: "adminMobile",
        component: () => import("@/views/admin/AdminViewMobile.vue"),
        redirect: { name: "DataStatisticsMoblie" },
        children: [
          {
            path: "AccountManages",
            name: "AccountManagesMoblie",
            redirect: { name: "AccountManage" },
            children: [
              {
                path: "AccountManage",
                name: "AccountManageMobile",
                component: () =>
                  import(
                    "@/components/adminview/AccountMange/AccountMangePage/AccountMangeViewMobile.vue"
                  ),
              },
              {
                path: "Details:id",
                name: "UserDetailsMoblie",
                component: () =>
                  import(
                    "@/components/adminview/AccountMange/UserDetailsPage/UserDetailsMoblie.vue"
                  ),
              },
            ],
          },
          {
            path: "DataStatistics",
            name: "DataStatisticsMoblie",
            component: () =>
              import(
                "@/components/adminview/DataStatistics/DataStatisticsViewMoblie.vue"
              ),
            redirect: { name: "UserDataMoblie" },
            children: [
              {
                path: "UserData",
                name: "UserDataMoblie",
                component: () =>
                  import(
                    "@/components/adminview/DataStatistics/UserDataChartPage/UserDataChartViewMoblie.vue"
                  ),
              },
            ],
          },
          {
            path: "Feedbacks",
            name: "FeedbacksMoblie",
            redirect: { name: "FeedbackMoblie" },
            children: [
              {
                path: "Feedback",
                name: "FeedbackMoblie",
                component: () =>
                  import(
                    "@/components/adminview/Feedback/FeedbackPage/FeedbackViewMoblie.vue"
                  ),
              },
              {
                path: "FeedbackDetails:id",
                name: "FeedbackDetailsMoblie",
                component: () =>
                  import(
                    "@/components/adminview/Feedback/FeedbackDetailsPage/FeedbackDetailsViewMoblie.vue"
                  ),
              },
            ],
          },
          {
            path: "Order",
            name: "OrderMOblie",
            component: () =>
              import(
                "@/components/adminview/Order/OrderTable/OrderViewMoblie.vue"
              ),
          },
        ],
      },
    ],
  },
];
