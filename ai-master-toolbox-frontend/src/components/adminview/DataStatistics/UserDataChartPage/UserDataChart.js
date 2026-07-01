import * as echarts from "echarts";
import { ElMessage } from "element-plus";
import {
  getGptCostCount,
  getNewUserCount,
  getActiveUserCount,
} from "@/api/statisticsApi";
import { set } from "nprogress";

// 用户新增图表天数(其他表适用)
const newUserOneMonthNumbers = [];
for (let index = 1; index < 31; index++) {
  newUserOneMonthNumbers.push("第" + index + "天");
}
const newUserHalfYearNumbers = [];
for (let index = 1; index < 7; index++) {
  newUserHalfYearNumbers.push("第" + index + "个月");
}
const newUserOneYearNumbers = [];
for (let index = 1; index < 13; index++) {
  newUserOneYearNumbers.push(index + "月");
}
// 汇率
const EXCHANGE_RATE = 7.5;
const prompt_tokens_RMB = (0.0015 * EXCHANGE_RATE) / 1000; //发送token人民币单价每个token
const completion_tokens_RMB = (0.002 * EXCHANGE_RATE) / 1000; //接收token人民币每个单价token

export default {
  name: "DataChart",
  data() {
    return {
      newUserCountPerDay: [],
      activeUserCountPerDay: [],
      tokenUserCountPerDay: [],
      selectedOption: "option1",
      userActiveOption: "option1",
      usertokenOption: "option1",
      usertokenCostOption: "option1",
      // 下拉框选项
      Options: [
        { value: "option1", label: "天数据" },
        { value: "option2", label: "月数据" },
        { value: "option3", label: "年数据" },
      ],
      // 新增
      newUserCurrentData: [],
      // 活跃
      activeUserData: [],
      // chartgpt成本
      tokenUserData: [],
      // token消耗次数
      tokenCostData: [],
      prompt_tokens: [],
      completion_tokens: [],
    };
  },
  computed: {
    // 新增用户
    newUserDataPerMonth() {
      return this.aggregateByMonth(this.newUserCountPerDay);
    },
    newUserDataPerYear() {
      return this.aggregateByYear(this.newUserCountPerDay);
    },
    newUserOneMonthData() {
      if (this.newUserCountPerDay.length >= 30) {
        return this.newUserCountPerDay.slice(-30);
      }
      return this.newUserCountPerDay.slice(0);
    },
    newUserHalfYearData() {
      if (this.newUserDataPerMonth.length >= 30) {
        return this.newUserDataPerMonth.slice(-30);
      } else {
        return this.newUserDataPerMonth;
      }
    },
    newUserYearData() {
      if (this.newUserDataPerYear.length >= 30) {
        return this.newUserDataPerYear.slice(-30);
      } else {
        return this.newUserDataPerYear;
      }
    },
    // 活跃用户
    activeUserDataPerMonth() {
      return this.aggregateByMonth(this.activeUserCountPerDay);
    },
    activeUserDataPerYear() {
      return this.aggregateByYear(this.activeUserCountPerDay);
    },
    activeUserdayData() {
      if (this.activeUserCountPerDay.length >= 30) {
        return this.activeUserCountPerDay.slice(-30);
      }
      return this.activeUserCountPerDay.slice(0);
    },
    activeUserMonthData() {
      if (this.activeUserDataPerMonth.length >= 30) {
        return this.activeUserDataPerMonth.slice(-30);
      } else {
        return this.activeUserDataPerMonth;
      }
    },
    activeUserYearData() {
      if (this.activeUserDataPerYear.length >= 30) {
        return this.activeUserDataPerYear.slice(-30);
      } else {
        return this.activeUserDataPerYear;
      }
    },
    // Gpt消耗成本
    tokenCostDataPerMonth() {
      return this.aggregateByMonth(this.tokenUserCountPerDay);
    },
    tokenCostDataPerYear() {
      return this.aggregateByYear(this.tokenUserCountPerDay);
    },
    tokenCostDayData() {
      if (this.tokenUserCountPerDay.length >= 30) {
        return this.tokenUserCountPerDay.slice(-30);
      }
      return this.tokenUserCountPerDay.slice(0);
    },
    tokenCostMonthData() {
      if (this.tokenCostDataPerMonth.length >= 30) {
        return this.tokenCostDataPerMonth.slice(-30);
      } else {
        return this.tokenCostDataPerMonth;
      }
    },
    tokenCostYearData() {
      if (this.tokenCostDataPerYear.length >= 30) {
        return this.tokenCostDataPerYear.slice(-30);
      } else {
        return this.tokenCostDataPerYear;
      }
    },
  },
  mounted() {
    this.fetchNewUserCountData();
    this.fetchActiveUserCountData();
    this.fetchGptCostCountData();
  },
  methods: {
    // 月聚合函数
    aggregateByMonth(data) {
      let dataWithMonth = data.map((item) => {
        let itempCopy = { ...item };
        itempCopy.date = itempCopy.date.slice(0, -3);
        return itempCopy;
      });
      let allProperties = Object.keys(data[0]);
      let allMonthList = new Set(dataWithMonth.map((item) => item.date));
      let dataPerMonth = {};
      for (let m of allMonthList) {
        dataPerMonth[m] = {};
        for (let p of allProperties) {
          if (p == "date") continue;
          dataPerMonth[m][p] = 0;
        }
      }
      dataWithMonth.forEach((item) => {
        for (let p of allProperties) {
          if (p == "date") continue;
          dataPerMonth[item.date][p] += item[p];
        }
      });
      let res = [];
      for (let m in dataPerMonth) {
        let tmp = {
          date: m,
        };
        Object.assign(tmp, dataPerMonth[m]);
        res.push(tmp);
      }
      return res;
    },
    // 年聚合函数
    aggregateByYear(data) {
      let dataWithMonth = data.map((item) => {
        let itempCopy = { ...item };
        itempCopy.date = itempCopy.date.slice(0, 4);
        return itempCopy;
      });
      let allProperties = Object.keys(data[0]);
      let allMonthList = new Set(dataWithMonth.map((item) => item.date));
      let dataPerMonth = {};
      for (let m of allMonthList) {
        dataPerMonth[m] = {};
        for (let p of allProperties) {
          if (p == "date") continue;
          dataPerMonth[m][p] = 0;
        }
      }
      dataWithMonth.forEach((item) => {
        for (let p of allProperties) {
          if (p == "date") continue;
          dataPerMonth[item.date][p] += item[p];
        }
      });
      let res = [];
      for (let m in dataPerMonth) {
        let tmp = {
          date: m,
        };
        Object.assign(tmp, dataPerMonth[m]);
        res.push(tmp);
      }
      return res;
    },
    // token消耗金额计算
    Gptcost(data) {
      // const promptTokens = data.map((item) => item.prompt_tokens);
      // const completionTokens = data.map((item) => item.completion_tokens);
      const countcost = data.map(
        (item) =>
          item.completion_tokens * completion_tokens_RMB +
          item.prompt_tokens * prompt_tokens_RMB
      );
      return countcost;
    },
    // 新增数据获取
    fetchNewUserCountData() {
      getNewUserCount()
        .then((response) => {
          this.newUserCountPerDay = response;
          this.newUserCurrentData = this.newUserOneMonthData;
          this.newUserinitChart();
        })
        .catch((error) => {
          // console.log(error);
          if (error) {
            ElMessage({
              message: error.error,
              type: "warning",
            });
          }
        });
    },
    // 活跃用户数据获取
    fetchActiveUserCountData() {
      getActiveUserCount()
        .then((response) => {
          this.activeUserCountPerDay = response;
          this.activeUserData = this.activeUserdayData;
          this.ActiveUserinitChart();
        })
        .catch((error) => {
          // console.log(error);
          if (error) {
            ElMessage({
              message: error.error,
              type: "warning",
            });
          }
        });
    },
    // gpt消耗金额数据获取
    fetchGptCostCountData() {
      getGptCostCount()
        .then((response) => {
          this.tokenUserCountPerDay = response;
          this.tokenUserData = this.tokenCostDayData;
          this.tokenCostData = this.tokenCostDayData;
          this.ChartGptCostChart();
          this.UserGptCostChart();
        })
        .catch((error) => {
          // console.log(error);
          if (error) {
            ElMessage({
              message: error.error,
              type: "warning",
            });
          }
        });
    },
    //新增下拉框选择监听
    newuserchange() {
      // 纵坐标
      if (this.selectedOption === "option1") {
        this.newUserCurrentData = this.newUserOneMonthData;
        this.newUserinitChart();
      } else if (this.selectedOption === "option2") {
        this.newUserCurrentData = this.newUserHalfYearData;
        this.newUserinitChart();
      } else if (this.selectedOption === "option3") {
        this.newUserCurrentData = this.newUserYearData;
        // console.log(this.newUserYearData);
        this.newUserinitChart();
      }
    },
    // 新增图表
    newUserinitChart() {
      // 创建一个基于 DOM 的节点，并将其作为 ECharts 的容器
      const chartContainer = document.getElementById("main");
      const chart = echarts.init(chartContainer);
      const number = this.newUserCurrentData.map((item) => {
        return item.date;
      });

      // 在这里添加你的 ECharts 配置和数据
      // 指定图表的配置项和数据
      const option = {
        title: {
          text: "用户新增数量",
        },
        tooltip: {},
        legend: {
          data: ["人数"],
        },
        xAxis: {
          data: number,
        },
        yAxis: {
          // type: "value",
          // max: 100,
        },
        series: [
          {
            name: "人数",
            type: "line",
            data: this.newUserCurrentData.map((item) => item.count),
          },
        ],
      };
      // 使用刚指定的配置项和数据显示图表。
      chart.setOption(option);
    },
    //
    // 活跃用户监听
    userActivechange() {
      if (this.userActiveOption === "option1") {
        this.activeUserData = this.activeUserdayData;
        this.ActiveUserinitChart();
      } else if (this.userActiveOption === "option2") {
        this.activeUserData = this.activeUserMonthData;
        this.ActiveUserinitChart();
      } else if (this.userActiveOption === "option3") {
        this.activeUserData = this.activeUserYearData;
        this.ActiveUserinitChart();
      }
    },
    // 活跃用户图表
    ActiveUserinitChart() {
      const chartContainers = document.getElementById("userActiveChart");
      const charts = echarts.init(chartContainers);
      const activenumber = this.activeUserData.map((item) => {
        return item.date;
      });

      // 在这里添加你的 ECharts 配置和数据
      // 指定图表的配置项和数据
      const options = {
        title: {
          text: "活跃用户数量",
        },
        tooltip: {},
        legend: {
          data: ["人数"],
        },
        xAxis: {
          data: activenumber,
        },
        yAxis: {
          // type: "value",
          // max: 100,
        },
        series: [
          {
            name: "人数",
            type: "line",
            data: this.activeUserData.map((item) => item.count),
          },
        ],
      };
      // 使用刚指定的配置项和数据显示图表。
      charts.setOption(options);
    },
    // gpt成本金额表监听
    usertokenchange() {
      if (this.usertokenOption === "option1") {
        this.tokenUserData = this.tokenCostDayData;
        this.ChartGptCostChart();
      } else if (this.usertokenOption === "option2") {
        this.tokenUserData = this.tokenCostMonthData;
        this.ChartGptCostChart();
      } else if (this.usertokenOption === "option3") {
        this.tokenUserData = this.tokenCostYearData;
        this.ChartGptCostChart();
      }
    },
    // token成本金额表
    ChartGptCostChart() {
      // 获取容器元素
      const chartContainer = document.getElementById("usertokenChart");
      // 初始化图表
      const gptchart = echarts.init(chartContainer);

      const cost = this.Gptcost(this.tokenUserData);
      const gptNumber = this.tokenUserData.map((item) => {
        return item.date;
      });

      // 定义图表配置项和数据
      const gptoptions = {
        title: {
          text: "ChartGpt消耗成本",
        },
        tooltip: {},
        legend: {
          data: ["金额"],
        },
        xAxis: {
          type: "category",
          data: gptNumber,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            name: "金额",
            type: "line",
            data: cost,
          },
        ],
      };

      // 使用配置项和数据渲染图表
      gptchart.setOption(gptoptions);
    },
    // tiken消耗监听
    usertokenCostchange() {
      if (this.usertokenCostOption === "option1") {
        this.tokenCostData = this.tokenCostDayData;
        this.UserGptCostChart();
      } else if (this.usertokenCostOption === "option2") {
        this.tokenCostData = this.tokenCostMonthData;
        this.UserGptCostChart();
      } else if (this.usertokenCostOption === "option3") {
        this.tokenCostData = this.tokenCostYearData;
        this.UserGptCostChart();
      }
    },
    // token消耗表
    UserGptCostChart() {
      // 获取容器元素
      const chartContainer = document.getElementById("usertokenCostChart");
      // 创建图表实例
      const chart = echarts.init(chartContainer);

      const time = this.tokenCostData.map((item) => item.date);
      const promptTokens = this.tokenCostData.map((item) => item.prompt_tokens);
      const completionTokens = this.tokenCostData.map(
        (item) => item.completion_tokens
      );

      // 配置数据
      const data = {
        legend: ["发送token", "接收token"],
        xAxis: time, // 横坐标数据
        series: [
          {
            name: "发送token",
            type: "line",
            data: promptTokens, // 第一个折线图的数据
            itemStyle: {
              color: "rgba(255, 99, 132, 0.5)",
            },
          },
          {
            name: "接收token",
            type: "line",
            data: completionTokens, // 第二个折线图的数据
            itemStyle: {
              color: "rgba(54, 162, 235, 0.5)",
            },
          },
        ],
      };

      // 配置选项
      const options = {
        title: {
          text: "Token消耗次数",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: data.legend,
        },
        xAxis: {
          data: data.xAxis,
        },
        yAxis: {},
        series: data.series,
      };

      // 更新图表配置和数据
      chart.setOption(options);
    },
  },
};
