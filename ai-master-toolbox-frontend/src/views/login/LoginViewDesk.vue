<template>
  <div class="container">
    <!-- 轮播图 -->
    <div class="info">
      <el-carousel height="739px" direction="vertical" :autoplay="false">
        <el-carousel-item v-for="item in 4" :key="item" />
      </el-carousel>
    </div>
    <!-- 登录注册 -->
    <div class="loginAndRegisterFrame">
      <template v-if="showLogin">
        <div class="formItem">
          <span>
            <el-icon><Avatar /></el-icon>
          </span>
          <input
            type="email"
            placeholder="请输入邮箱"
            v-model="email"
            @blur="checkEmail"
          />
        </div>
        <div class="formItem">
          <span>
            <el-icon><Lock /></el-icon
          ></span>
          <input
            type="password"
            placeholder="请输入密码"
            v-model="password"
            @keyup.enter="handleLogin"
          />
        </div>
        <el-button type="primary" @click="handleLogin">登录</el-button>
        <div style="display: flix; padding-left: 140px; margin-top: 10px">
          <span class="registrationJump" @click.prevent="switchPage(1)">
            注册账号
          </span>
          <span class="registrationJump" @click.prevent="switchPage(2)">
            找回密码
          </span>
        </div>
      </template>

      <template v-else>
        <div class="formItem">
          <span>
            <el-icon><Avatar /></el-icon>
          </span>
          <input
            type="email"
            placeholder="请输入邮箱"
            v-model="email"
            @blur="checkEmail"
          />
        </div>
        <div class="errorMessage" v-if="isWrongEmail">邮箱格式错误</div>
        <div class="formItem">
          <span>
            <el-icon><Lock /></el-icon>
          </span>
          <input
            type="password"
            placeholder="请输入密码"
            v-model="password"
            @blur="checkPassword"
          />
        </div>
        <div class="formItem">
          <span
            ><el-icon><Lock /></el-icon
          ></span>
          <input
            type="password"
            placeholder="请再次输入密码"
            v-model="password2"
            @blur="checkPassword"
          />
        </div>
        <div class="errorMessage" v-if="notSamePassword">两次密码不一致</div>
        <div class="formItem">
          <input
            class="verifyCodeInput"
            type="number"
            placeholder="请输入验证码"
            v-model="verifyCode"
          />
          <el-link
            class="verifyCodeLink"
            type="primary"
            @click.prevent="getVerifyCode"
          >
            {{ verifyCodeLinkText }}
          </el-link>
        </div>

        <el-button v-if="showRegister" type="primary" @click="handleRegister">
          注册
        </el-button>
        <el-button
          v-else
          type="primary"
          @click="resetPassword"
          style="letter-spacing: 20px; padding-left: 30px"
        >
          重置密码
        </el-button>
        <span class="registrationJump" @click.prevent="switchPage(0)">
          立即登录
        </span>
      </template>
    </div>
  </div>
</template>

<script>
import deviceMixin from "@/mixins/deviceMixin.js";
import loginViewMixin from "./LoginViewMixin";
export default {
  mixins: [deviceMixin, loginViewMixin],
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped>
@import "@/assets/style/common.less";
.container {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  flex-flow: row nowrap;
}

.info {
  width: 55%;
  height: 100%;
  background: linear-gradient(to right, #fff, #252ab6);
}

.el-carousel__item {
  background-image: url(../../assets/images/AIMasterToolboxLogin.png);
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: center;
}

.loginAndRegisterFrame {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
  background: linear-gradient(to left, #000, #252ab6);
  width: 45%;
  height: 100%;

  .errorMessage {
    width: 240px;
    font-size: 10px;
    color: red;
  }

  .formItem {
    width: 300px;
    height: 45px;
    border: 1px solid var(--el-border-color);
    border-radius: 5px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-start;
    align-items: center;
    padding: 0 5px;
    margin-bottom: 30px;
    background-color: #fff;
    font-size: 14px;

    .el-icon {
      font-size: 18px;
      text-align: center;
      margin: 5px;
    }

    &:hover {
      border-color: rgb(64, 158, 255);
    }

    input {
      flex-grow: 1;
      border: none;
      height: 100%;
      outline: none;
      padding: 0 10px;
      font-size: 14px;
    }
  }

  .registrationJump {
    cursor: pointer;
    margin: 0 10px;
    color: rgba(255, 255, 255, 0.5);
    &:hover {
      color: rgb(255, 255, 255);
    }
  }

  .el-button {
    width: 300px;
    height: 35px;
    background: #4fb9ff;
    letter-spacing: 50px;
    padding-left: 60px;
    transition: all 1s;

    &:hover {
      background: #8fd2ff;
    }
  }

  & > * {
    margin-bottom: 13px;
  }
}

.verifyCodeInput {
  width: 150px;
}

.verifyCodeLink {
  font-size: 12px;
  border-left: 1px solid var(--el-border-color);
  padding-left: 5px;
}
</style>
