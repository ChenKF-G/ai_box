<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
    style="height: 9vh"
  >
    <el-menu-item index="0">
      <router-link to="/">
        <img
          class="logo"
          src="../../assets/images/AIMasterToolboxLOGO.png"
          alt="AI 大师 工具箱"
        />
      </router-link>
    </el-menu-item>
    <div class="flex-grow" />
    <el-sub-menu index="1" v-if="user">
      <template #title>
        <el-icon><Avatar /></el-icon>
        {{ user.username }}
      </template>
      <router-link :to="{ name: 'PersonalInformation' }">
        <el-menu-item index="1-1">
          个人中心
          <el-icon><Setting /></el-icon>
        </el-menu-item>
      </router-link>
      <router-link :to="{ name: 'AccountManagesDesk' }">
        <el-menu-item index="1-2" v-if="user && user.is_superuser">
          管理员页面
          <el-icon><House /></el-icon>
        </el-menu-item>
      </router-link>
      <el-menu-item index="1-3" @click="signOut">
        退出登录
        <el-icon><SwitchButton /></el-icon>
      </el-menu-item>
    </el-sub-menu>
    <button class="login" v-if="!user">
      <router-link to="login"> 登录注册 </router-link>
    </button>
  </el-menu>
</template>

<script>
import { mapState } from "vuex";
import { logout } from "@/api/userApi";
import { ElMessage } from "element-plus";
import Cookies from "js-cookie";

export default {
  created() {
    // 如果token存在则取获取user数据
    if (Cookies.get("token")) {
      this.$fetchData.fetchUser(false);
    }
  },
  data() {
    return {
      activeIndex: 1,
    };
  },
  computed: {
    ...mapState(["user"]),
  },
  methods: {
    async signOut() {
      try {
        await logout();
      } catch (error) {
        if (error) {
          ElMessage.error(error.error);
        }
      } finally {
        Cookies.set("token", "");
        this.$fetchData.clear();
        this.$router.push({ name: "login" });
      }
    },
  },
};
</script>

<style>
a {
  color: black;
  text-decoration: none;
}

.el-menu--horizontal {
  height: 55px;
}

.flex-grow {
  flex-grow: 1;
}

.el-menu--horizontal {
  border-bottom: none;
}

.el-menu--horizontal .el-menu .el-menu-item,
.el-menu--horizontal .el-menu .el-sub-menu__title {
  display: flex;
  justify-content: space-around;
}
.logo {
  width: 145px;
  height: 80px;
}

/* 头像 */
.el-sub-menu img {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  margin-right: 10px;
}

/* 登录按钮 */
.login {
  border: none;
  background: none;
  padding-right: 45px;
}
</style>
