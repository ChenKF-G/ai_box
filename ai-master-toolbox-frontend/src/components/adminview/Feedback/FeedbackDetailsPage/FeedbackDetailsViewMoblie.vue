<template>
  <div class="bank">
    <button class="btu" @click="banked(pk)">←</button>
    <span class="user">用户{{}}的反馈详情页面</span>
  </div>
</template>
<script>
import FeedbackDetailsJs from "./FeedbackDetails"
import deviceMixin from "@/mixins/deviceMixin.js";

export default {
  mixins: [FeedbackDetailsJs,deviceMixin],
  data() {
    return {
      pk:2
    };
  },
};
</script>
<style lang="less" scoped>
.btu {
  width: 5%;
  height: 2%;
  font-size: 30px;
  border-radius: 15px;
  border: 0px solid rgb(106, 146, 188);
}
.bank {
  margin-left: 1%;
  margin-top: 5px;
}
.user {
  margin-left: 15.5%;
}
</style>
