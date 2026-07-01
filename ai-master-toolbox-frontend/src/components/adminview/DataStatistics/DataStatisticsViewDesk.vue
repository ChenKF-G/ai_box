<template>
  <div class="page">
    <div class="dataview">
      <DataCount></DataCount>
    </div>
    <el-scrollbar class="data">
      <div class="datanav">
        <UserDataChart></UserDataChart>
      </div>
    </el-scrollbar>
  </div>
</template>

<script>
import DataCount from "@/components/adminview/DataStatistics/DataCountPage/DataCountViewDesk.vue";
// import DataNav from "@/components/adminview/DataStatistics/DataStatisticsNavView.vue";
import UserDataChart from "@/components/adminview/DataStatistics/UserDataChartPage/UserDataChartViewDesk.vue";
import deviceMixin from "@/mixins/deviceMixin.js";

export default {
  name: "DataStatistics",
   mixins: [deviceMixin],
  components: {
    DataCount,
    UserDataChart,
  },
};
</script>

<style lang="less" scoped>
.page {
  flex-flow: column nowrap;
  align-items: stretch;
  width: 100%;
  // height: 700px;
  background-color: rgb(239, 239, 239);
  font-family: "\5b8b\4f53";
}
.data {
  width: 100%;
  height: 100%;
  margin-top: 1%;
  // background-color: antiquewhite;
  height: 100vh; /* 设置容器高度为视口高度的100% */
  overflow: auto; /* 当内容溢出容器时显示滚动条 */
}
.dataview {
  width: 100%;
  height: 30%;
  // background-color: rgb(221, 185, 138);
}
.chart {
  width: 100%;
  height: 100%;
  margin-top: 5%;
}
.datanav {
  padding: 10px 20px 0 20px;
  height: 5%;
  width: 100%;
}
.datachart {
  height: 100%;
}
</style>
