// deviceMixin.js

const MOBILE_WIDTH = 680;

export default {
  data() {
    return {
      isMobile: false,
      windowWidth: window.innerWidth,
    };
  },
  mounted() {
    // 使用vue-device库来检查设备宽度
    this.isMobile = this.windowWidth <= MOBILE_WIDTH; // 你可以根据需要设置阈值

    // 添加窗口宽度变化的事件监听器
    window.addEventListener("resize", this.handleResize);

    this.checkRoutePath();
  },
  watch: {
    isMobile(newValue, oldValue) {
      this.checkRoutePath();
    },
  },
  beforeDestroy() {
    // 在组件销毁前移除事件监听器以防止内存泄漏
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      // 当窗口宽度变化时，更新窗口宽度和设备类型
      this.windowWidth = window.innerWidth;
      this.isMobile = this.windowWidth <= MOBILE_WIDTH; // 你可以根据需要设置阈值
    },
    checkRoutePath() {
      if (this.isMobile && this.$route.fullPath.indexOf("desk")) {
        let newPath = this.$route.fullPath.replace("desk", "mobile");
        this.$router.replace(newPath);
      } else if (!this.isMobile && this.$route.fullPath.indexOf("mobile")) {
        let newPath = this.$route.fullPath.replace("mobile", "desk");
        this.$router.replace(newPath);
      }
    },
  },
};
