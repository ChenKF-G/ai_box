<template>
  <div class="dataview">
    <span>数据图表展示</span>
  </div>
  <div class="charts">
    <!-- 新增 -->
    <div class="chart">
      <el-select
        v-model="selectedOption"
        placeholder=""
        class="sel"
        id="userid"
        @change="newuserchange"
      >
        <el-option
          v-for="option in Options"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        ></el-option>
      </el-select>
      <div class="chr" id="main"></div>
    </div>
    <!-- 活跃用户 -->
    <div class="chart">
      <el-select
        v-model="userActiveOption"
        placeholder=""
        class="sel"
        id="userid"
        @change="userActivechange"
      >
        <el-option
          v-for="option in Options"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        ></el-option>
      </el-select>
      <div class="chr" id="userActiveChart"></div>
    </div>
    <!-- token消耗金额表 -->
    <div class="chart">
      <el-select
        v-model="usertokenOption"
        placeholder=""
        class="sel"
        id="userid"
        @change="usertokenchange"
      >
        <el-option
          v-for="option in Options"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        ></el-option>
      </el-select>
      <div class="chr" id="usertokenChart"></div>
    </div>
    <!-- token消耗金额表 -->
    <div class="chart">
      <el-select
        v-model="usertokenCostOption"
        placeholder=""
        class="sel"
        id="userid"
        @change="usertokenCostchange"
      >
        <el-option
          v-for="option in Options"
          :key="option.value"
          :label="option.label"
          :value="option.value"
        ></el-option>
      </el-select>
      <div class="chr" id="usertokenCostChart"></div>
    </div>
  </div>
</template>

<script>
import UserDataChartJs from "./UserDataChart"
import deviceMixin from "@/mixins/deviceMixin.js";

export default {
  mixins: [UserDataChartJs,deviceMixin],
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped>
.dataview {
  text-align: center;
}
.charts {
  margin-top: 1%;
  display: flex;
  flex-wrap: wrap;
}
.chart {
  margin-left: 3%;
  margin-top: 2%;
  margin-bottom: 2%;
  width: 45%;
  flex-wrap: wrap;
  padding: auto;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  // text-align: center;
}
.tits {
}
.chr {
  width: 600px;
  height: 400px;
}
.sel {
  margin-left: 75%;
}
</style>
