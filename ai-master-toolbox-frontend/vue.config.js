const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false, //关闭Vue生产提示
  devServer: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000/api/", // 后端 API 地址
        changeOrigin: true,
        pathRewrite: {
          "^/api": "", // 重写路径，将 /api 替换为空字符串
        },
      },
    },
  },
});
