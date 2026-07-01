<template>
  <div>
    <div class="headNav">
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
        @select="handleSelect"
      >
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
    </div>
    <div class="home">
      <HomePageContent />
    </div>
  </div>
</template>

<script>
import HomePageContent from "../../components/home/HomePageContentComponent.vue";
import deviceMixin from "@/mixins/deviceMixin.js";
import { mapState } from "vuex";
import { logout } from "@/api/userApi";
import { ElMessage } from "element-plus";
import Cookies from "js-cookie";

export default {
  name: "HomeView",
  components: {
    HomePageContent,
  },
  mixins: [deviceMixin],

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

<style lang="less" scoped>
.headNav {
  height: 9vh;
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
}

.home {
  display: flex;
  height: 90vh;
  background-image: linear-gradient(to top, #000000, #000086, #fff);
  /deep/ .HomePageContent {
    min-width: 1px;
    color: #fff;
    padding: 10px;
    box-sizing: border-box;
  }
  /* 搜索框样式 */
  /deep/ .input {
    display: flex;
    padding: 0 30px;
  }
  /deep/ .input button {
    width: 30%;
    height: 35px;
    background: white;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-left: 20px;
    cursor: pointer;
  }

  /* 工具箱样式 */
  /deep/ .toolbox {
    width: 100%;
    max-height: 550px;
    padding: 20px;
    box-sizing: border-box;
  }
  /deep/ .tools h2 {
    line-height: 80px;
  }
  /deep/ .tool {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    justify-items: stretch;
    grid-row-gap: 25px;
  }
  /deep/ .Single {
    height: 60px;
    line-height: 60px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    transition: all 0.5s;
  }
  /deep/ .Single p {
    font-size: 14px;
  }
  /deep/ .Single img {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    margin: 10px;
  }
  /deep/ .el-menu-item {
    padding: 0;
  }
}
</style>
