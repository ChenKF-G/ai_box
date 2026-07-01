export default [
  {
    path: "/idPhoto",
    name: "idPhoto",
    redirect: { name: "idPhotoMobile" },
    children: [
      {
        path: "mobile",
        name: "idPhotoMobile",
        component: () => import("@/views/idPhoto/idPhotoViewMobile.vue"),
      },
      {
        path: "SelectPhone",
        name: "SelectPhone",
        component: () =>
          import("@/components/idphoto/Mobile/SelectPhotoViewMobile.vue"),
      },
      {
        path: "DownloadPhone",
        name: "DownloadPhone",
        component: () =>
          import("@/components/idphoto/Mobile/DownloadPhotoViewMobile.vue"),
      },
      {
        path: "TakePhoto",
        name: "TakePhoto",
        component: () =>
          import("@/components/idphoto/Mobile/TakePhotoViewMobile.vue"),
      },
    ],
  },
];
