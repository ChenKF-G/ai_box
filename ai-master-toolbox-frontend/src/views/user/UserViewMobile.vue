<template>
  <HeadNav />
  <div class="box">
    <router-view />
    <Bottom style="" />
  </div>
</template>

<script>
import HeadNav from "../../components/home/HeadNav.vue";
import Bottom from "../../components/userView/Mobile/BottomMenu.vue";
import deviceMixin from "@/mixins/deviceMixin.js";
export default {
  mixins: [deviceMixin],
  components: {
    HeadNav,
    Bottom,
  },
};
</script>

<style lang="less" scoped>
.box {
  position: relative;
  height: 90vh;
  background: linear-gradient(to top, #000569, #fff);
}
/deep/ .el-menu-item {
  padding: 0;
}
</style>