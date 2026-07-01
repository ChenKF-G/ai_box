<template>
  <div class="HomePageContent">
    <!-- 搜索框模块 -->
    <div class="input">
      <el-input v-model="input" placeholder="请输入工具" prefix-icon="Search" />
      <button @click="Search">搜索</button>
    </div>
    <!-- 具体工具模块 -->
    <div class="toolbox">
      <div class="tools" v-for="title in EndData.ArrayData" :key="title.id">
        <!-- 大分类标题 -->
        <h2>{{ title.catagoryName }}</h2>
        <div class="tool">
          <div
            class="Single"
            style="margin: 0 10px"
            v-for="(tool, index) in title.features"
            :key="index"
            @click="expect(title.catogroryId, tool.featureId)"
          >
            <router-link
              :to="{
                name: tool.pathName,
              }"
              style="
                display: flex;
                flex-wrap: nowrap;
                flex-direction: row;
                align-items: center;
                line-height: 60px;
              "
            >
              <div class="test">
                <el-tooltip
                  :content="tool.body"
                  effect="dark"
                  placement="bottom"
                  popper-class="Home_Page_Content_Component_Tooltip"
                  :z-index="100"
                >
                  <el-button>
                    <el-icon
                      style="font-size: 25px; color: #fff; margin-right: 5px"
                    >
                      <component :is="tool.icon"> </component>
                    </el-icon>
                    <p style="color: #fff">{{ tool.title }}</p>
                  </el-button>
                </el-tooltip>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <!-- 底部备案信息 -->
    <div class="Record">
      <a href="https://beian.miit.gov.cn/" target="_blank">您的备案号</a>
      <a href="https://beian.miit.gov.cn/" target="_blank">
        渝ICP备2023012574号-1</a
      >
    </div>
  </div>
</template>

<script>
import { reactive, ref } from "vue";
import { ElMessageBox } from "element-plus";

export default {
  setup() {
    let showBtn = ref(true);
    // 引入json文件
    const ArrayData = require("./featureButtonInfo.json");
    let EndData = reactive({ ArrayData });

    // input框内容
    const input = ref("");

    // 打开提醒弹窗
    const open = (type) => {
      if (type === expect) {
        ElMessageBox.alert(
          "功能正在研发中，请期待₍˄·͈༝·͈˄*₎◞ ̑̑",
          "AI 大师工具箱",
          {
            confirmButtonText: "OK",
          }
        );
      } else if (type === Search) {
        ElMessageBox.alert(
          "本网站暂不包含此类型的工具，未来会努力研发₍˄·͈༝·͈˄*₎◞ ̑̑",
          "AI 大师工具箱",
          {
            confirmButtonText: "OK",
          }
        );
      }
    };

    // 未上线功能提醒
    function expect(catogroryId, featureId) {
      let isOpen = EndData.ArrayData[catogroryId].features[featureId].isOpen;
      if (!isOpen) {
        open(expect);
      }
    }

    // 搜索功能
    function Search() {
      if (input.value === "") {
        EndData.ArrayData = ArrayData;
        return;
      } else {
        let searchInput = new RegExp(input.value, "i"); // 模糊搜索
        for (let title = 0; title < ArrayData.length; title++) {
          for (let tool = 0; tool < ArrayData[title].features.length; tool++) {
            if (searchInput.test(ArrayData[title].features[tool].body)) {
              EndData.ArrayData = [];
              EndData.ArrayData.unshift(ArrayData[title]);
              console.log("EndData", EndData);
              input.value = "";
              return;
            }
          }
        }
      }
      input.value = "";
      open(Search);
    }

    return {
      // 数据
      showBtn, //显示按钮判断
      input, //input框内容
      EndData, // 具体功能的显示数据
      // 功能
      expect, //未上线功能提醒
      Search, //搜索功能
    };
  },
};
</script>

<style scoped>
.el-button {
  border: none;
  background: rgba(0, 0, 0, 0);
}
.HomePageContent {
  position: relative;
}
.Record {
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translateX(-50%);
  width: 50vh;
  text-align: center;
}
.Record a {
  color: #fff;
  margin-right: 5px;
  transition: all 0.3s;
}
.Record a:hover {
  color: #0091ec;
}
</style>
