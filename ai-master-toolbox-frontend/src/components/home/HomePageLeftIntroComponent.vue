<template name = 'life'>
  <!-- 主页左侧轮播图 -->
  <el-carousel
    height="670px"
    direction="vertical"
    :autoplay="false"
    v-show="isMin"
  >
    <el-carousel-item v-for="item in 1" :key="item"> </el-carousel-item>
  </el-carousel>
</template>


<script>
import { ref } from "vue";

export default {
  setup() {
    let isMin = ref(true);

    window.addEventListener("resize", () => {
      if (window.outerWidth < 600) {
        isMin.value = false;
      } else {
        isMin.value = true;
      }
    });

    return {
      isMin,
    };
  },
};
</script>


<style scoped>
.el-carousel__item {
  background-image: url("/src/assets/images/posters/Mini_program_QR_code.jpg");
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: center;
}

/* 改变左侧轮播图的大小 */
.el-carousel--vertical {
  overflow-y: hidden;
  width: 20%;
  border-radius: 5px;
  min-width: 200px;
}
</style>
