import { mapState } from "vuex";
import {
  getUserCount,
  getNewUserCount,
  getActiveUserCount,
  getGptCostCount,
} from "@/api/statisticsApi";

const currentDate = new Date();
const dayOfMonth = currentDate.getDate();

// 汇率
const EXCHANGE_RATE = 7.5;
const prompt_tokens_RMB = (0.0015 * EXCHANGE_RATE) / 1000; //发送token人民币单价每个token
const completion_tokens_RMB = (0.002 * EXCHANGE_RATE) / 1000; //接收token人民币每个单价token

export default {
  name: "DataCount",
  data() {
    return {
      userCount: null,
      newUserCountPerDay: null,
      todayNewUserCount: null,
      thisMonthNewUser: null,
      ActiveUserCount: null,
      todayActiveUser: null,
      thisMonthActiveUser: null,
      tokenUserCountPerDay: [],
      tokenCost: 0,
    };
  },
  created() {},
  // 在组件挂载时调用fetchData方法来获取数据
  mounted() {
    this.fetchUserCountData();
    this.fetchNewUserCountData();
    this.fetchActiveUserCountData();
  },
  methods: {
    // 总用户
    fetchUserCountData() {
      getUserCount()
        .then((response) => {
          // 在这里处理 API 请求的响应结果
          this.userCount = response.count;
          // console.log(this.userCount);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 新增用户
    fetchNewUserCountData() {
      getNewUserCount()
        .then((response) => {
          // 在这里处理 API 请求的响应结果,拿到新增一年数据
          this.newUserCountPerDay = response;
          // 获取今日新增数据
          this.todayNewUserCount =
            this.newUserCountPerDay[this.newUserCountPerDay.length - 1].count;
          // console.log(this.newUserCountPerDay,dayOfMonth)
          // 这个月新增
          const newUserCountPerDayPro = this.newUserCountPerDay.reverse();
          for (let i = 0; i <= dayOfMonth - 1; i++) {
            this.thisMonthNewUser =
              this.thisMonthNewUser + newUserCountPerDayPro[i].count;
          }
          // console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    //活跃用户
    fetchActiveUserCountData() {
      getActiveUserCount()
        .then((response) => {
          // 在这里处理 API 请求的响应结果
          this.ActiveUserCount = response;
          // console.log(this.ActiveUserCount);
          // 今日活跃用户
          this.todayActiveUser =
            this.ActiveUserCount[this.ActiveUserCount.length - 1].count;
          // 这个月活跃用户
          const ActiveUserCountPro = this.ActiveUserCount.reverse();
          for (let i = 0; i <= dayOfMonth - 1; i++) {
            this.thisMonthActiveUser =
              this.thisMonthActiveUser + ActiveUserCountPro[i].count;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    fetchGptCostCountData() {
      getGptCostCount()
        .then((response) => {
          this.tokenUserCountPerDay = response;
          const ActiveUserCountPro = this.tokenUserCountPerDay.reverse();
          for (let i = 0; i <= dayOfMonth - 1; i++) {
            this.tokenCost =
              this.tokenCost +
              prompt_tokens_RMB * prompt_tokens +
              completion_tokens_RMB * completion_tokens;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  computed: {
    ...mapState(["userCount", "newusercount"]),
  },
};
