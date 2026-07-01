<template>
  <!--左 导航样式及排版 -->

  <div class="leftNavContainer">
    <button class="title" @click.stop="gotoHome">管理员中心</button>
    <router-link
      class="titleNav"
      :to="{ name: 'AccountManageDesk' }"
      active-class="xuanz"
    >
      <div>账号管理</div>
    </router-link>
    <router-link
      class="titleNav"
      to="/admin/desk/DataStatistics/UserData"
      active-class="xuanz"
    >
      <div>数据统计</div>
    </router-link>
    <router-link class="titleNav" to="/admin/desk/Order" active-class="xuanz">
      <div>订单</div>
    </router-link>
    <router-link class="titleNav" to="/admin/desk/Feedbacks" active-class="xuanz">
      <div>反馈</div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "LeftNav",
  methods: {
    gotoHome() {
      this.$router.push({ name: "home" });
    },
    photos() {
      this.$router.push({ name: "takephotos" });
    },
  },
};
</script>
<style lang="less" scoped>
.leftNavContainer {
  width: 100%;
  height: 100%;
  background: rgb(31, 102, 139);
}

.title {
  width: 100%;
  height: 60px;
  display: flex;
  flex-flow: row nowrap;
  justify-content: center;
  align-items: center;
  color: #fff;
  font-size: 25px;
  font-weight: 600;
  border: none;
  border-bottom: 3px solid #fff;
  background: rgb(31, 102, 139);
  margin: 0;
  padding: 0;
  margin-bottom: 20px;
  cursor: pointer;
}

div {
  text-align: center;
  margin-bottom: 15px;
  padding: 15px 0;
}
div:hover {
  color: #9c84e9;
}
.titleNav {
  display: block;
  color: #fff;
  text-decoration: none;
  margin: 0 30px;
}
.xuanz {
  border-radius: 50px;
  background: rgb(82, 89, 165);
}
</style>
