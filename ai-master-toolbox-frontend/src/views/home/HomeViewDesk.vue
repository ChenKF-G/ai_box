<template>
  <div>
    <HeadNav />
    <div class="home">
      <CarouselLife />
      <HomePageContent />
      <CarouselRight />
    </div>
  </div>
</template>

<script>
import HeadNav from "../../components/home/HeadNav.vue";
import CarouselLife from "../../components/home/HomePageLeftIntroComponent.vue";
import CarouselRight from "../../components/home/HomePageRightIntroComponent.vue";
import HomePageContent from "../../components/home/HomePageContentComponent.vue";

import deviceMixin from "@/mixins/deviceMixin.js";

export default {
  name: "HomeView",
  components: {
    HeadNav,
    CarouselLife,
    CarouselRight,
    HomePageContent,
  },
  mixins: [deviceMixin],
  created() {},
};
</script>

<style scoped>
.home {
  display: flex;
  height: 91vh;
  background-image: linear-gradient(to top, #000000, #000086, #fff);
}

>>> .HomePageContent {
  min-width: 480px;
  width: 60%;
  color: #fff;
  margin: 50px 50px 0 50px;
}

/* 搜索框样式 */
>>> .input {
  display: flex;
  padding: 0 80px 50px 80px;
}

>>> .input button {
  width: 20%;
  height: 35px;
  background: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-left: 20px;
  cursor: pointer;
}

/* 工具箱样式 */
>>> .toolbox {
  width: 100%;
  /* height: 550px; */
  padding: 20px;
  /* 元素溢出添加滚动条 */
  overflow: auto;
}

>>> .toolbox::-webkit-scrollbar {
  /* 隐藏滚动条 */
  display: none;
}

>>> .tools h2 {
  line-height: 80px;
}

>>> .tool {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-row-gap: 25px;
  min-width: 480px;
}
>>> .Single {
  width: 80%;
  height: 60px;
  line-height: 60px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  transition: all 0.5s;
}
>>> .Single:hover {
  transform: translateY(-10px);
  box-shadow: 0px 0px 8px #ccc;
}
>>> .Single p {
  font-size: 14px;
}
>>> .Single img {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  margin: 10px;
}

>>> .el-carousel__container {
  top: 50%;
  transform: translateY(-50%);
}
</style>
