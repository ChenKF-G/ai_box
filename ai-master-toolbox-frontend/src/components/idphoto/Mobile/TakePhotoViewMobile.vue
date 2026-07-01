<template>
  <div class="content">
    <div class="backes">
      <el-button class="backs" @click="banked">返回</el-button>
    </div>
    <div class="cash">
      <div class="peo">
        <img
          src="@\components\idphoto\Mobile\人物取景框.png"
          alt=""
          class="peoimg"
        />
      </div>
      <video ref="videoElement" autoplay class="vido"></video>
      <canvas ref="canvasElement"></canvas>
    </div>
    <div class="takebut">
      <el-button @click="takePhoto" class="but">拍照</el-button>
    </div>
    <!-- <img :src="photoData" v-if="photoData" alt=""> -->
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
      photoData: null,
      color: this.$route.query.color,
      colorli: this.$route.query.colorli,
      size: this.$route.query.size,
      sizeli: this.$route.query.sizeli,
      processedPhotoUrl: null,
      watermarkimage: null,
    };
  },
  mounted() {
    this.initCamera();
  },
  methods: {
    initCamera() {
      navigator.mediaDevices
        .getUserMedia({ video: true })
        .then((stream) => {
          const videoElement = this.$refs.videoElement;
          videoElement.srcObject = stream;
          videoElement.play();
        })
        .catch((error) => {
          console.error("无法访问摄像头：", error);
        });
    },
    banked() {
      const query = {
        color: this.$route.query.color,
        size: this.$route.query.size,
      };
      this.$router.push({ name: "SelectPhone", query });
    },
    takePhoto() {
      const videoElement = this.$refs.videoElement;
      const canvasElement = this.$refs.canvasElement;
      const context = canvasElement.getContext("2d");

      // 将视频流的画面绘制到Canvas中
      context.drawImage(
        videoElement,
        0,
        0,
        canvasElement.width,
        canvasElement.height
      );

      // 获取Canvas中的图像数据
      const imageData = canvasElement.toDataURL("image/png");

      // 将base64编码的图像数据转换为Blob对象
      const byteString = atob(imageData.split(",")[1]);
      const mimeString = imageData.split(",")[0].split(":")[1].split(";")[0];
      const ab = new ArrayBuffer(byteString.length);
      const ia = new Uint8Array(ab);
      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }
      const blob = new Blob([ab], { type: mimeString });

      // 创建文件对象并保存
      const file = new File([blob], "photo.png", { type: mimeString });

      // 存储拍摄的照片文件
      this.photoData = file;
      console.log(this.photoData);

      //   发送请求，更换底色
      const formData = new FormData();
      formData.append("photo", file, "photo.jpg");
      formData.append("color", this.color);
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
            color: this.$route.query.color,
            size: this.$route.query.size,
            colorli: this.$route.query.colorli,
            sizeli: this.$route.query.sizeli,
          };
          this.$router.push({ name: "DownloadPhone", query });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
.content {
  width: 100%;
  height: 100%;
}
.backs {
  margin-left: 80%;
  margin-top: 4%;
}
.cash {
  width: 100%;
  height: 65%;
  /* background-color: antiquewhite; */
  margin-top: 2%;
  position: relative;
}
.takebut {
  width: 100%;
  height: 28.3%;
  background-color: rgb(0, 0, 0);
}
.vido {
  height: 100%;
  width: 100%;
}
.peo {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  margin: auto;
  z-index: 1; /* 将 peo 盒子的层级设置为 1 */
  margin-left: 18%;
  margin-top: 33%;
}
.peoimg {
  width: 75%;
  height: 70%;
}
.but {
  width: 23%;
  height: 36%;
  margin-top: 15%;
  margin-left: 38%;
  border-radius: 50%;
  z-index: 2;
}
canvas {
  width: 0px;
  height: 0px;
}
</style>
