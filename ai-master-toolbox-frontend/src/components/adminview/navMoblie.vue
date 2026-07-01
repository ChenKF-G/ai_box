<template>
  <div class="leftNavContainer">
    <div class="tit">
      <button @click.stop="gotoHome" class="navback">管理员中心</button>
    </div>
    <div class="center">
      <!-- <button class="title" @click.stop="gotoHome">管理员中心</button> -->
      <el-dropdown class="selet">
        <span class="el-dropdown-link">
          管理员中心
          <el-icon class="el-icon--right">
            <arrow-down />
          </el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item
              ><router-link
                class="titleNav"
                :to="{ name: 'AccountManageMobile' }"
                active-class="xuanz"
                @click="open"
              >
                <div class="titnav">账号管理</div>
              </router-link></el-dropdown-item
            >
            <el-dropdown-item
              ><router-link
                class="titleNav"
                :to="{ name: 'DataStatisticsMoblie' }"
                active-class="xuanz"
                @click="open"
              >
                <div class="titnav">数据统计</div>
              </router-link></el-dropdown-item
            >
            <el-dropdown-item
              ><router-link
                class="titleNav"
                :to="{ name: 'OrderMOblie' }"
                active-class="xuanz"
                @click="open"
              >
                <div class="titnav">订单</div>
              </router-link></el-dropdown-item
            >
            <el-dropdown-item disabled
              ><router-link
                class="titleNav"
                :to="{ name: 'FeedbackMoblie' }"
                active-class="xuanz"
                @click="open"
              >
                <div class="titnav">反馈</div>
              </router-link></el-dropdown-item
            >
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      collapse: true,
    };
  },
  methods: {
    gotoHome() {
      this.$router.push({ name: "HomeViewMobile" });
    },
    toggleCollapse() {
      this.collapse = !this.collapse;
    },
    open() {
      this.collapse = !this.collapse;
    },
  },
};
</script>

<style scoped>
.leftNavContainer {
  position: relative;
  /* background-color: rgb(239, 239, 239); */
  margin-top: -2.5%;
}
.title {
  color: white;
}
.tit {
  background: rgb(31, 102, 139);
  color: white;
  text-align: center;
}

.collapseBtn {
  /* 折叠按钮样式 */
  /* position: absolute; */
  color: white;
  top: 0;
  right: 0;
}
.pageContainer {
  display: flex;
  flex-flow: row nowrap;
  align-items: stretch;
  overflow: hidden;
  flex-grow: 1;
}
.center {
  /* margin-top: 1%; */
  background-color: rgb(31, 102, 139);
}
button {
  border: none;
  margin-left: 1%;
  background-color: rgb(31, 102, 139);
}
div {
  padding: 3% 0;
}
div:hover {
  color: #9c84e9;
}
.titleNav {
  display: block;
  color: #fff;
  text-decoration: none;
  margin: 0 5%;
}
.selet {
  color: white;
  margin-top: -1%;
  margin-left: 2%;
}
.titnav {
  color: black;
}
.navback {
  color: white;
}
</style>
