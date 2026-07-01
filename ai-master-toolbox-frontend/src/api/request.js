//引入axios
import axios from "axios";
//进度条展示功能
import NProgress from "nprogress";
import { ElMessage } from "element-plus";
import Cookies from "js-cookie";
import router from "@/router";

NProgress.configure({ showSpinner: false }); // 显示右上角螺旋加载提示
const request = axios.create({
  baseURL: "/api", //地址
  timeout: 120 * 1000, //请求时间 50s
  headers: {
    Accept: "application/json", // 接受的数据类型
    "Content-Type": "application/json",
  },
});

//请求拦截器
request.interceptors.request.use(
  (config) => {
    NProgress.start();
    if (Cookies.get("token")) {
      config.headers["Authorization"] = "Bearer " + Cookies.get("token");
    }
    if (config.contentType) {
      config.headers["Content-Type"] = config.contentType;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    NProgress.done();
    return response.data;
  },
  (error) => {
    NProgress.done();
    if (
      !(error && error.response && error.response.data) ||
      typeof error.response.data === "string"
    ) {
      ElMessage({
        message: "服务器或网络错误，请稍后重试",
        type: "warning",
      });
      return Promise.reject();
    }
    if (error.response) {
      // 如果响应错误，根据 HTTP 状态码进行处理
      const status = error.response.status;

      // 如果状态码是 401（未授权）或 403（禁止访问），可能表示 token 失效
      if (status === 401 || status === 403) {
        // 在这里进行 token 失效的处理逻辑
        // 例如，清除本地存储的 token，然后跳转到登录页面
        Cookies.set("token", "");
        router.push("/login"); // 重定向到登录页面
        if (error.response.data.error || error.response.data.detail) {
          ElMessage({
            message: error.response.data.error || error.response.data.detail,
            type: "warning",
          });
        } else {
          ElMessage({
            message: "服务器或网络错误，请稍后重试",
            type: "warning",
          });
        }
        return Promise.reject();
      }
    }
    return Promise.reject({
      status: error.response.status,
      error: error.response.data.error || error.response.data.detail,
    });
  }
);

export default request;
