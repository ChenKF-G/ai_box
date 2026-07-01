<template>
  <div class="BottomModule">
    <img src="../../../assets/images/AIMasterToolboxLOGO.png" alt="LOGO" />
    <p>重庆光辰慧思信息科技有限责任公司版权所有</p>
    <p style="cursor: pointer">帮助文档</p>
    <div class="QRCode1"></div>
    <div class="QRCode2"></div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="less" scoped>
.BottomModule {
  position: absolute;
  bottom: 10px;

  min-width: 930px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  width: 100%;
  height: 95px;
  line-height: 100px;
  padding: 0 50px;
  border-top: 1px solid #d7e1e7;
  p {
    margin-left: 50px;
  }
  .QRCode1 {
    width: 80px;
    height: 80px;
    background: #d7e1e7;
    border-radius: 50%;
    margin: auto 50px;
  }
  .QRCode2 {
    width: 80px;
    height: 80px;
    background: #d7e1e7;
    margin: auto 0;
  }
}
</style>