<template>
  <div class="Recharge">
    <div>
      <div class="headline">
        <p>反馈记录</p>
        <router-link to="/user/desk/FeedbackPop-ups">
          <el-button type="text">
            <el-icon><Plus /></el-icon>
          </el-button>
        </router-link>
      </div>
      <div class="Informations">
        <div
          class="Information"
          v-for="(Information, index) in Information"
          :key="index"
        >
          <p class="title">{{ Information.title }}</p>
          <p class="detail">{{ Information.detail }}</p>
          <p class="item">{{ Information.item }}</p>
          <p class="state">{{ Information.state }}</p>
          <router-link :to="{ name: 'DetailsPop-up' }">
            <button class="btn">详情</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>


<script >
export default {
  data() {
    return {
      Information: [
        {
          title: "建议增加ai排版功能",
          detail:
            "很多做设计的小伙伴经常会接到画册传单之类的需求，这些使用ai来排版是非常方便的，今天就和大家分享一些简单而又高效地提高字体排版效果的一些小窍门。希望可以帮助大家更好的提高工作效率~",
          item: "2023/10/13",
          state: "未审核",
        },
        {
          title: "建议增加ai排版功能",
          detail:
            "很多做设计的小伙伴经常会接到画册传单之类的需求，这些使用ai来排版是非常方便的，今天就和大家分享一些简单而又高效地提高字体排版效果的一些小窍门。希望可以帮助大家更好的提高工作效率~",
          item: "2023/10/13",
          state: "未审核",
        },
      ],
    };
  },
};
</script>


<style lang="less" scoped>
.Recharge {
  box-sizing: border-box;
  margin: 0 20%;
  width: 60%;
  min-width: 550px;
  height: 500px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  overflow: auto;
  .headline {
    display: flex;
    justify-content: space-between;
    height: 70px;
    line-height: 70px;
    border-bottom: 1px solid #ccc;
    padding: 0 20px 0 10px;
    font-size: 20px;
    font-weight: 700;
    .el-button {
      margin: auto 0;
      cursor: pointer;
      font-size: 25px;
    }
  }
  .Informations {
    .Information {
      display: flex;
      justify-content: space-between;
      height: 50px;
      line-height: 50px;
      border-bottom: 1px solid #ccc;
      padding: 0 20px;
      .title {
        width: 150px;
        font-weight: 600;
      }
      .detail {
        width: 20%;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
      }
      .btn {
        width: 50px;
        height: 35px;
        margin: auto 0;
        background: #f0f4f6;
        border: 1px solid #c9dae2;
        border-radius: 5px;
        cursor: pointer;
      }
    }
  }
}
.Recharge::-webkit-scrollbar {
  display: none;
}
</style>