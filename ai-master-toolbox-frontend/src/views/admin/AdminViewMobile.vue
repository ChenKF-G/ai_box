<template>
  <div class="nav">
    <Nav></Nav>
  </div>
  <div class="bottom">
    <RouterView></RouterView>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import Nav from "@/components/adminview/navMoblie.vue";
import deviceMixin from "@/mixins/deviceMixin.js";

export default {
  name: "AdminView",
  mixins: [deviceMixin],
  components: {
    Nav,
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

.nav {
  width: 99.1%;
}
.bottom {
  width: 99.1%;
}
</style>
