<template>
  <div class="Recharge">
    <div>
      <div class="headline">
        <p>反馈记录</p>
        <router-link to="FeedbackPop-ups_Mobile">
          <el-button type="text">
            <el-icon><Plus /></el-icon>
          </el-button>
        </router-link>
      </div>
      <div class="Informations">
        <div class="Information">
          <p class="title">建议增加ai排版功能</p>
          <p class="item">2023/10/13</p>
          <router-link to="DetailsPop-up_Mobile">
            <button class="btn">详情</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>


<script >
export default {};
</script>


<style lang="less" scoped>
.Recharge {
  box-sizing: border-box;
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
</style>