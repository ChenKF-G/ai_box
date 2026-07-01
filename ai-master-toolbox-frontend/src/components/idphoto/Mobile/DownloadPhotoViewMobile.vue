<template>
  <div class="content">
    <div class="back">
      <el-button class="backs" @click="banked">返回</el-button>
    </div>
    <div class="tits">
      <span class="title">电子照片</span>
    </div>
    <hr class="hrs" />
    <div class="showPhoto">
      <div class="borders">
        <img
          :src="watermarkurl"
          v-if="watermarkurl"
          alt="美化照片"
          class="imgs"
        />
      </div>
    </div>
    <div class="selectbut">
      <el-button class="but" @click="banked">重新选择</el-button>
      <el-button @click="drawer = true" type="primary" class="downbut">
        下载证件照
      </el-button>
    </div>
    <div class="downloadwindow">
      <el-drawer title="" v-model="drawer" :direction="direction" size="40%">
        <div class="downloadtit">下载方式</div>
        <div class="selectdown">
          <div class="select">
            <div class="txt">高清无码下载</div>
            <div class="txt">￥1.99</div>
          </div>
        </div>
        <el-button class="download" @click="downphoto">下载照片</el-button>
      </el-drawer>
    </div>
  </div>
</template>
<script>
import { downloadphoto } from "@/api/picApi";
import { ElMessageBox } from "element-plus";

export default {
  data() {
    return {
      photourl: this.$route.query.photoUrl,
      watermarkurl: this.$route.query.watermark,
      imgurl: null,
      drawer: false,
      direction: "btt",
    };
  },
  mounted() {},
  created() {
    console.log(this.watermarkurl);
  },
  methods: {
    banked() {
      const query = {
        color: this.$route.query.color,
        size: this.$route.query.size,
        colorli: this.$route.query.colorli,
        sizeli: this.$route.query.sizeli,
      };
      this.$router.push({ name: "SelectPhone", query });
    },
    async downphoto() {
      try {
        let response = await downloadphoto();

        const blob = new Blob([response], {
          type: "image/png",
        });

        // 创建一个 URL 对象，并生成下载链接
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = "image.png";

        // 模拟点击下载链接
        link.click();

        // 释放 URL 对象
        URL.revokeObjectURL(url);
      } catch (error) {
        ElMessageBox.alert("请先获取下载次数", "提示", {
          confirmButtonText: "确定",
          type: "error",
          showClose: false,
        });
      }
    },
  },
};
</script>
<style scoped>
.txt {
  margin-top: 5%;
}
.st {
  margin-left: 5%;
}
.selectdown {
  height: 50%;
  width: 100%;
  margin-top: 5%;
}
.select {
  border-radius: 5%;
  margin-left: 31%;
  text-align: center;
  height: 60%;
  width: 35%;
  background-color: rgb(253, 236, 238);
  display: inline-block;
  font-size: 14px;
  border: 1px solid rgb(252, 38, 38);
}
.content {
  width: 99%;
  height: 100%;
  margin: auto;
  background-color: rgb(241, 241, 241);
}
.tits {
  margin-top: 5%;
  /* background-color: rgb(244, 237, 228); */
  text-align: center;
}
.hrs {
  width: 80%;
  margin: auto;
  background-color: gray;
}
.showPhoto {
  height: 60%;
  margin-top: 5%;
  /* background-color: bisque; */
}
.imgs {
  margin-top: 8%;
  margin-left: 12%;
  height: 60%;
  width: 60%;
  margin-left: 20%;
}
.borders {
  border: 1px solid gray;
  background-color: rgb(236, 235, 235);
}
.selectbut {
  /* background-color: bisque; */
  margin: auto;
}
.but {
  margin-left: 18%;
  background-color: skyblue;
}
.downbut {
  /* margin-top: 5%; */
  margin-left: 17%;
}
.download {
  background-color: rgb(139, 139, 251);
  margin-top: 5%;
  margin-left: 14%;
  width: 70%;
}
.back {
  margin-left: 3%;
}
.backs {
  margin-top: 3%;
}
</style>
