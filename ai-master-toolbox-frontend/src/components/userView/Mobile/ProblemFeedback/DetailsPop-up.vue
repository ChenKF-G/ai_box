<template>
  <!-- 详情弹窗 -->
  <div class="DetailBox" ref="DetailBox">
    <p style="font-weight: 800; font-size: 20px; margin-bottom: 20px">详情</p>
    <button class="submit" @click="ShutDown">
      <svg
        t="1697159348644"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="4391"
        width="25"
        height="25"
      >
        <path
          d="M700.371228 394.525472 174.028569 394.525472l255.952416-227.506551c12.389168-11.011798 13.505595-29.980825 2.492774-42.369993-11.011798-12.386098-29.977755-13.506619-42.367947-2.492774L76.425623 400.975371c-6.960529 5.496178-11.434423 14.003945-11.434423 23.561625 0 0.013303 0.001023 0.026606 0.001023 0.039909 0 0.01228-0.001023 0.025583-0.001023 0.037862 0 0.473791 0.01535 0.946558 0.037862 1.418302 0.001023 0.016373 0.001023 0.032746 0.001023 0.049119 0.39295 8.030907 3.992941 15.595186 10.034541 20.962427l315.040163 280.028764c5.717212 5.083785 12.83533 7.580652 19.925818 7.580652 8.274454 0 16.514115-3.403516 22.442128-10.07445 11.011798-12.387122 9.896394-31.357172-2.492774-42.367947l-256.128425-227.665163 526.518668 0c109.219517 0 198.075241 88.855724 198.075241 198.075241s-88.855724 198.075241-198.075241 198.075241L354.324888 850.696955c-16.57449 0-30.011524 13.437034-30.011524 30.011524s13.437034 30.011524 30.011524 30.011524l346.046341 0c142.31631 0 258.098289-115.783003 258.098289-258.098289S842.686515 394.525472 700.371228 394.525472z"
          fill="#272636"
          p-id="4392"
        ></path>
      </svg>
    </button>

    <div class="BoxDetail">
      <div class="feedback">
        <!-- 需求 -->
        <div class="demand">
          <p>需求：</p>
          <p class="title">建议增加ai排版功能</p>
        </div>
        <!-- 需求简述 -->
        <div class="description">
          <p>需求简述：</p>
          <p class="detail">
            很多做设计的小伙伴经常会接到画册传单之类的需求，这些使用ai来排版是非常方便的，今天就和大家分享一些简单而又高效地提高字体排版效果的一些小窍门。希望可以帮助大家更好的提高工作效率~
          </p>
        </div>
        <!-- 反馈时间 -->
        <div class="item">
          <p>反馈时间：</p>
          <p>2023/10/03</p>
        </div>
        <!-- 反馈状态 -->
        <div class="state">
          <p>反馈状态：</p>
          <p>待审核</p>
        </div>
        <!-- 客服回应 -->
        <div class="state">
          <p>回应内容：</p>
          <p class="Reply">
            我们立志于给客户们带来更多的便捷与更舒适的体验，您的建议我们已经收到，在不久的将来该功能即将上线，尽情期待
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script >
export default {
  methods: {
    ShutDown() {
      this.$router.push({
        name: "ProblemFeedbackHomeMobile",
      });
    },
  },
};
</script>


<style lang="less" scoped>
.DetailBox {
  position: relative;
  padding: 20px;
  .feedback {
    height: 70vh;
    overflow: auto;
    padding: 10px;
    p {
      width: 120px;
    }
    .type,
    .demand,
    .description,
    .item,
    .state {
      display: flex;
      margin-bottom: 20px;
    }
  }
  .feedback::-webkit-scrollbar {
    display: none;
  }
  .submit {
    position: absolute;
    right: 20px;
    top: 20px;
    width: 50px;
    height: 30px;
    background: none;
    border: none;
    border-radius: 5px;
  }

  .BoxDetail {
    padding-top: 20px;
    .title {
      width: 150px;
      font-weight: 600;
    }
    .detail,
    .Reply {
      width: 65%;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  }
}
</style>