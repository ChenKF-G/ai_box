<template>
  <div class="left" v-show="isMin">
    <div class="user" v-if="user">
      <p>{{ user.username }}</p>
    </div>
    <div class="elements">
      <ul>
        <!-- <router-link to="MyMessage">
          <li>系统消息</li>
        </router-link> -->
        <router-link :to="{ name: 'PersonalInformation' }">
          <li>个人信息</li>
        </router-link>
        <router-link :to="{ name: 'ProblemFeedback' }">
          <li>问题反馈</li>
        </router-link>
        <router-link :to="{ name: 'Recharge' }">
          <li>充值记录</li>
        </router-link>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Cookies from "js-cookie";

export default {
  data() {
    return {
      isMin: true,
      radio: 6,
      demand: "",
      description: "",
      activeName: "first",
      input: "1111",
    };
  },

  created() {
    window.addEventListener("resize", () => {
      if (window.outerWidth < 1350) {
        this.isMin = false;
      } else {
        this.isMin = true;
      }
    });

    // 如果token存在则取获取user数据
    if (Cookies.get("token")) {
      this.$fetchData.fetchUser(false);
    }
  },

  mounted() {
    console.log(this.user);
  },

  computed: {
    ...mapState(["user"]),
  },
};
</script>

<style lang="less" scoped>
.left {
  float: left;
  width: 15%;
  min-width: 200px;
  height: 500px;
  border: 1px solid #ddd;
  border-radius: 5px;
  .user {
    display: flex;
    height: 80px;
    background: #f0f4f6;
    border-radius: 5px 5px 0 0;
    border-bottom: 1px solid #ddd;
    line-height: 80px;
    text-align: center;
    span {
      position: relative;
      display: inline-block;
      margin: auto 20px;
      width: 30px;
      height: 30px;
      line-height: 60px;
      background: #140050;
      color: aliceblue;
      font-size: 40px;
      border-radius: 50%;
      overflow: hidden;
      svg {
        position: absolute;
        top: -5px;
        left: -5px;
      }
    }
    p {
      margin-left: 30px;
    }
  }
  .elements {
    ul {
      list-style: none;
      li {
        height: 50px;
        line-height: 50px;
        padding-left: 20px;
        border-bottom: 1px solid #e1e7ea;
        &:hover {
          background: #f0f4f6;
        }
      }
    }
  }
}
</style>