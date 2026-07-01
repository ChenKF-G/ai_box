<template>
  <HeadNav />
  <div class="box">
    <LeftMenu />
    <router-view></router-view>
  </div>
  <BottomModule />
</template>

<script>
import HeadNav from "../../components/home/HeadNav.vue";
import LeftMenu from "../../components/userView/Desk/LeftMenu.vue";
import BottomModule from "../../components/userView/Desk/BottomModule.vue";
import deviceMixin from "@/mixins/deviceMixin.js";
export default {
  mixins: [deviceMixin],
  components: {
    HeadNav,
    LeftMenu,
    BottomModule,
  },
};
</script>

<style lang="less" scoped>
.box {
  padding: 30px 0 0 30px;
}
</style>