<template>
  <div class="title">数据总览</div>
  <div class="imforpage">
    <div class="imfor">
      <div class="tit">总用户</div>
      <div class="number">{{ userCount }}</div>
    </div>
    <div class="imfor">
      <div class="tit">当日新增</div>
      <div class="number">{{ todayNewUserCount }}</div>
    </div>
    <div class="imfor">
      <div class="tit">当月新增</div>
      <div class="number">{{ thisMonthNewUser }}</div>
    </div>
    <div class="imfor">
      <div class="tit">当日活跃用户数</div>
      <div class="number">{{ todayActiveUser }}</div>
    </div>
    <div class="imfor">
      <div class="tit">当月活跃用户数</div>
      <div class="number">{{ thisMonthActiveUser }}</div>
    </div>
    <div class="imfor">
      <div class="tit">当月token消耗金额</div>
      <div class="number">{{ tokenCost }}</div>
    </div>
    <!-- <div class="imfor">
      <div class="tit">当日订单量</div>
      <div class="number">{{}}</div>
    </div>
    <div class="imfor">
      <div class="tit">当月订单量</div>
      <div class="number">{{}}</div>
    </div> -->
  </div>
</template>

<script>
import DataCountJs from "./DataCount";
import deviceMixin from "@/mixins/deviceMixin.js";
export default {
  mixins: [DataCountJs,deviceMixin],
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped>
.title {
  text-align: center;
  margin-bottom: 1%;
}
.imforpage {
  // height: 100%;
  background-color: rgb(228, 231, 231);
  display: flex;
  flex-wrap: wrap;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}
.imfor {
  width: 10%;
  border: 1px solid rgb(187, 208, 219);
  margin-left: 8%;
  margin-top: 1%;
  margin-bottom: 1%;
  flex-wrap: wrap;
  padding: auto;
}
.tit {
  margin-top: 5%;
  text-align: center;
}
.number {
  margin-top: 5%;
  margin-bottom: 5%;
  text-align: center;
}
</style>
