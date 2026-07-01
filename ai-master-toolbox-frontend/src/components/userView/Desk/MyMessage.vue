<template>
  <div class="box">
    <button>标记所有为已读</button>
    <el-input
      v-model="input2"
      class="w-50 m-2"
      placeholder="输入搜索的内容"
      style="width: 200px"
      :prefix-icon="Search"
    />
    <hr />
    <!-- 消息内容 -->
    <div class="MessageContent">
      <p>您的账户余额为XXX元 请充值</p>
      <p><span>6</span>小时以前</p>
    </div>
    <div class="MessageContent">
      <p>您已于2023/10/11日17：36分充值成功，您的账户余额为XXX</p>
      <p><span>8</span>小时以前</p>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { Search } from "@element-plus/icons-vue";
export default {
  data() {
    return {
      input: ref(""),
      Search,
    };
  },
};
</script>

<style lang="less" scoped>
.box {
  padding-left: 20px;
  position: relative;
  width: 78%;
  min-width: 700px;
  height: 450px;
  overflow: auto;
  margin-left: 50px;
  button {
    position: absolute;
    top: 30px;
    right: 65px;
    height: 30px;
    background: none;
    border: none;
  }
  hr {
    margin-top: 20px;
  }
  .MessageContent {
    padding-right: 45px;
    display: flex;
    justify-content: Space-between;
    height: 50px;
    line-height: 50px;
    border-bottom: 1px solid #f0f4f6;
  }
}

.box::-webkit-scrollbar {
  display: none;
}
</style>