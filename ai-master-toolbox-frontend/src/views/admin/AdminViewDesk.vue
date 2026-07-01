<template>
  <div class="page">
    <div class="pageContainer">
      <div class="left">
        <LeftNav></LeftNav>
      </div>
      <div class="right">
        <RouterView></RouterView>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import LeftNav from "@/components/adminview/LeftNav.vue";
import deviceMixin from "@/mixins/deviceMixin.js";

export default {
  name: "AdminView",
  mixins: [deviceMixin],
  components: {
    LeftNav,
  },
  async created() {
    await this.$fetchData.fetchUser(false);
    if (!this.user || !this.user.is_superuser) {
      this.$router.push("/login");
    }
  },
  computed: {
    ...mapState(["user"]),
  },
};
</script>

<style lang="less" scoped>
// @import "@/assets/styles/entirePage.less";

.page {
  display: flex;
  flex-flow: column nowrap;
  align-items: stretch;
  width: 100%;
  height: 700px;
  background-color: rgb(239, 239, 239);
}
.pageContainer {
  display: flex;
  flex-flow: row nowrap;
  align-items: stretch;
  overflow: hidden;
  flex-grow: 1;
}
.left {
  width: 10%;
  min-width: 200px;
  flex-grow: 0;
}
.right {
  flex-grow: 1;
  padding: 10px 20px 0 20px;
}
</style>
