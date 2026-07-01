<template>
  <div class="Recharge">
    <div>
      <div class="headline">
        <p>充值记录</p>
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
}
.Recharge::-webkit-scrollbar {
  display: none;
}
</style>