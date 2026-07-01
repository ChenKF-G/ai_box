<template>
  <div class="contentPage">
    <div class="back">
      <el-button class="backs" @click="banked">返回</el-button>
    </div>
    <div class="tit">
      <span>证件照规格说明</span>
    </div>
    <hr />
    <div class="text">
      <div class="tis">照片大小：{{ this.size }}</div>
      <div class="tis">
        背景色：{{ this.color
        }}<span :style="{ background: show }" class="showcolor"></span>
      </div>
    </div>
    <!-- 建议 -->
    <div class="something">
      <span class="things">拍照建议</span>
      <div class="dian">
        <div class="dis">1.表情自然，抬头挺胸，两眼直视前方</div>
        <div class="dis">2.找他人协助，用后置摄像头拍摄</div>
        <div class="dis">3.穿深色衣服，在纯色或者白色背景下效果更佳</div>
      </div>
    </div>
    <div class="buttons">
      <el-button class="but" @click="openGallery">相册选择(推荐)</el-button>
      <input
        ref="fileInput"
        type="file"
        accept="image/*"
        style="display: none"
        @change="handleFileSelect"
      />
      <el-button class="but" @click="takephoto">直接拍摄</el-button>
    </div>
  </div>
</template>
<script>
import { changephotobackground } from "@/api/picApi";
import config from "@/config.json";

const environment = process.env.NODE_ENV;
const serverHost = config["serverHost"][environment];

export default {
  data() {
    return {
      color: this.$route.query.color,
      colorli: this.$route.query.colorli,
      size: this.$route.query.size,
      sizeli: this.$route.query.sizeli,
      processedPhotoUrl: null,
      watermarkimage: null,
      show: this.$route.query.csscolor,
    };
  },
  mounted() {},
  methods: {
    banked() {
      this.$router.push({ name: "idPhotoMobile" });
    },
    openGallery() {
      this.$refs.fileInput.click(); // 触发文件选择
    },
    handleFileSelect(e) {
      const file = e.target.files[0]; // 获取选择的文件
      const formData = new FormData();
      formData.append("photo", file, "photo.jpg");
      formData.append("size", this.size);
      formData.append("colorlist", this.colorli);
      formData.append("sizelist", this.sizeli);
      changephotobackground(formData)
        .then((response) => {
          this.processedPhotoUrl = serverHost + response.image_url;
          this.watermarkimage = serverHost + response.watermarkimage_url;
          console.log(this.processedPhotoUrl);
          const query = {
            photoUrl: this.processedPhotoUrl,
            watermark: this.watermarkimage,
            color: this.color,
            size: this.size,
            colorli: this.$route.query.colorli,
            sizeli: this.$route.query.sizeli,
          };
          this.$router.push({ name: "DownloadPhone", query });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    takephoto() {
      const query = {
        color: this.color,
        size: this.size,
        colorli: this.colorli,
        sizeli: this.sizeli,
      };
      this.$router.push({ name: "TakePhoto", query });
    },
  },
};
</script>
<style lang="less" scoped>
.contentPage {
  width: 90%;
  margin: auto;
}
.showcolor {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin-left: 3%;
  border-radius: 50%;
}
.backs {
  margin-top: 3%;
}
.tit {
  margin-top: 5%;
  margin-bottom: 5%;
}
.text {
  margin-top: 15%;
}
.tis {
  margin-top: 10%;
}
.something {
  margin-top: 20%;
}
.things {
  font-size: 18px;
  font-weight: bold;
}
.dian {
  margin-top: 5%;
}
.dis {
  font-size: 13px;
}
.buttons {
  width: 100%;
  margin-top: 10%;
}
.but {
  height: 15%;
  width: 35%;
  display: block;
  margin-left: 25%;
  margin-top: 5%;
  border: 1px solid blue;
  background-color: rgb(164, 201, 226);
}
</style>
