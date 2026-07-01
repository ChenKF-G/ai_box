import * as userApi from "@/api/userApi";
import { ElMessage } from "element-plus";
import Cookies from "js-cookie";
import { mapState } from "vuex";
export default {
  data() {
    return {
      showLogin: true,
      showRegister: false,
      showResetPassword: false,
      email: "",
      password: "",
      password2: "",
      verifyCode: "",
      isWrongEmail: false,
      verifyCodeLinkText: "获取验证码",
      notSamePassword: false,
    };
  },
  computed: {
    ...mapState(["user"]),
  },
  methods: {
    switchPage(pageNum) {
      // 0 代表 login, 1 代表 register, 2代表reset password
      this.showRegister = false;
      this.showResetPassword = false;
      this.showLogin = false;
      if (pageNum == 1) {
        this.showRegister = true;
      } else if (pageNum == 2) {
        this.showResetPassword = true;
      } else {
        this.showLogin = true;
      }
    },
    checkEmail() {
      const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

      // 使用正则表达式的 test 方法来验证 email 参数是否符合格式
      this.isWrongEmail = !emailPattern.test(this.email);
      return !this.isWrongEmail;
    },
    checkPassword() {
      this.notSamePassword = this.password != this.password2;
      return !this.notSamePassword;
    },
    checkVerifyCode() {
      let verifyCodePattern = /^[0-9]{6}$/;
      return verifyCodePattern.test(this.verifyCode);
    },
    async handleLogin() {
      this.$fetchData.clear();
      userApi
        .login({
          username: this.email,
          password: this.password,
        })
        .then(async (res) => {
          Cookies.set("token", res.token);
          ElMessage({
            message: "登录成功，即将跳转...",
            type: "success",
          });
          await this.$fetchData.fetchUser();
          if (this.user.is_superuser) {
            setTimeout(() => {
              this.$router.push({ name: "admin" });
            }, 500);
          } else {
            setTimeout(() => {
              this.$router.push({ name: "home" });
            }, 500);
          }
        })
        .catch((error) => {
          if (error) {
            ElMessage({
              message: error.error,
              type: "warning",
            });
          }
        });
    },
    handleRegister() {
      if (!this.checkEmail()) {
        return;
      }
      if (!this.checkPassword() || !this.password) {
        this.notSamePassword = true;
        return;
      }
      if (!this.checkVerifyCode) {
        ElMessage({
          message: "验证码错误",
          type: "warning",
        });
        return;
      }
      userApi
        .register({
          email: this.email,
          password: this.password,
          verify_code: this.verifyCode,
        })
        .then((res) => {
          ElMessage({
            message: "注册成功，即将跳转登录页面",
            type: "success",
          });
          setTimeout(() => {
            this.showLogin = true;
          }, 500);
        })
        .catch((error) => {
          ElMessage({
            message: error.error,
            type: "warning",
          });
        });
    },
    getVerifyCode() {
      let leftSecond = 60;
      let inteval = setInterval(() => {
        this.verifyCodeLinkText = leftSecond + "s";
        leftSecond -= 1;
        if (leftSecond <= 0) {
          this.verifyCodeLinkText = "获取验证码";
          clearInterval(inteval);
        }
      }, 1000);
      userApi
        .getVerifyCode({ email: this.email })
        .then((res) => {})
        .catch((error) => {
          this.verifyCodeLinkText = "获取验证码";
          clearInterval(inteval);
          if (error) {
            ElMessage({
              message: error.error,
              type: "warning",
            });
          }
        });
    },
    resetPassword() {
      if (!this.checkEmail()) {
        return;
      }
      if (!this.checkPassword() || !this.password) {
        this.notSamePassword = true;
        return;
      }
      if (!this.checkVerifyCode) {
        ElMessage({
          message: "验证码错误",
          type: "warning",
        });
        return;
      }
      userApi
        .resetPassword({
          email: this.email,
          password: this.password,
          verify_code: this.verifyCode,
        })
        .then((res) => {
          ElMessage({
            message: "重置密码成功，即将跳转登录页面",
            type: "success",
          });
          setTimeout(() => {
            this.showLogin = true;
          }, 500);
        })
        .catch((error) => {
          if (error) {
            ElMessage({
              message: error.error,
              type: "warning",
            });
          }
        });
    },
  },
};
