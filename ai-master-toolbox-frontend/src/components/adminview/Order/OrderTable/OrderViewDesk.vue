<template>
  <div class="mys">
    <span class="my">我的订单</span>
  </div>
  <div class="orders">
    <div class="classification">
      <span class="cla"><a href="">全部订单</a></span>
      <span class="cla"><a href="">待付款</a></span>
      <span class="cla"><a href="">待发货</a></span>
      <span class="clb">|</span>
      <span class="clb"><a href="">已经取消订单</a></span>
      <div class="gets">
        <el-input
          style="width: 80%; height: 2%"
          v-model="searchKeyword"
          placeholder="订单名称 / 订单号"
          aria-valuetext=""
        ></el-input>
      </div>
      <button @click="search" class="search">搜索</button>
    </div>
    <div class="searchexs">
      <select class="Select">
        <option value="option1">今年内订单</option>
        <option value="option2">近一个月订单</option>
        <option value="option3">近一年订单</option>
      </select>
      <span class="sea">订单详情</span>
      <span class="sea">收货人</span>
      <span class="seb">金额</span>
      <select class="Select state">
        <option value="option1">全部状态</option>
        <option value="option2">等待付款</option>
        <option value="option3">等待收货</option>
        <option value="option3">已完成</option>
      </select>
      <span class="seb">操作</span>
    </div>
    <div class="box"></div>
  </div>
  <div>
    
  </div>
</template>

<script>
import OrderJs from "./Order"
import deviceMixin from "@/mixins/deviceMixin.js";

export default {
  mixins: [OrderJs,deviceMixin],
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped>
.mys {
  margin-top: 1%;
  margin-left: 1%;
  width: 90%;
  height: 10%;
  background-color: rgb(255, 255, 255);
  font-family: "\5b8b\4f53";
  display: flex;
  align-items: center;
}
.my {
  height: 50%;
  width: 10%;
  margin-top: 40%;
  text-align: center;
  padding-left: 1%;
  margin-top: 1%;
}
.orders {
  margin-top: 3%;
  margin-left: 1%;
  width: 90%;
  height: 80%;
  background-color: rgb(255, 255, 255);
  font-family: "\5b8b\4f53";
  overflow: auto;
}
.classification {
  height: 8%;
  margin-top: 1%;
  // background-color: aqua;
}
.cla {
  display: inline-block;
  margin-left: 3%;
  // background-color: aqua;
}
.clb {
  display: inline-block;
  margin-left: 5%;
}
a {
  text-decoration: none;
}
.gets {
  display: inline-block;
  margin-left: 30%;
}
.search {
  background-color: rgb(239, 239, 239);
  width: 5%;
  height: 30px;
  border: none;
  margin-top: 6px;
  margin-left: -10px;
}
.searchexs {
  margin-top: 1%;
  margin-left: 2.5%;
  width: 90%;
  height: 7%;
  background-color: rgb(239, 239, 239);
  font-family: "\5b8b\4f53";
  overflow: auto;
}
.Select {
  border: none; /* 去掉边框 */
  outline: none; /* 去掉聚焦时的边框 */
  appearance: none; /* 去掉默认样式（部分浏览器） */
  -webkit-appearance: none; /* 去掉默认样式（部分浏览器） */
  -moz-appearance: none; /* 去掉默认样式（部分浏览器） */
  padding: 5px;
  background-color: #f2f2f2;
  color: #333;
  position: relative;
  margin-left: 1%;
  margin-top: 0.6%;
}
.Select option {
  /* 选项的样式 */
  background-color: #fff;
  color: #333;
}

.Select select {
  /* 下拉列表的样式 */
  background-color: #745be7;
  color: #333;
  border: none;
  box-shadow: none;
}
.sea {
  margin-left: 18%;
}
.seb {
  margin-left: 10%;
}
.state {
  margin-left: 8%;
}
</style>
