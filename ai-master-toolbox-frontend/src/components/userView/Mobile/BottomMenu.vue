<template>
  <div class="test">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
      <router-link to="PersonalInformation">
        <el-menu-item index="1">个人信息</el-menu-item>
      </router-link>
      <router-link to="ProblemFeedbackHome">
        <el-menu-item index="2">问题反馈</el-menu-item>
      </router-link>
      <router-link to="Recharge">
        <el-menu-item index="3">充值记录</el-menu-item>
      </router-link>
    </el-menu>
  </div>
</template>

<script  setup>
import { ref } from "vue";
const activeIndex = ref("1");
</script>

<style lang="less" scoped>
.test {
  bottom: 0;
  .el-menu--horizontal.el-menu {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-evenly;
  }
}
</style>
