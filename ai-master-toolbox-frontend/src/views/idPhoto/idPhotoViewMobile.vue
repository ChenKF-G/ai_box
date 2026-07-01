<template>
  <div class="content">
    <div class="back">
      <el-button class="backs" @click="banked">返回</el-button>
    </div>
    <!-- 证件照 -->
    <div class="id_photo">
      <div class="colortit" style="text-align: center">快速生成</div>
      <div class="colors">
        <div class="colortit ot">请选择颜色</div>
        <div class="selectcolor">
          <div class="sel rebor">
            <el-button class="red" @click="butred"></el-button>
            <div class="colortext">红色</div>
          </div>
          <div class="sel">
            <el-button class="blue" @click="butblue"></el-button>
            <div class="colortext">蓝色</div>
          </div>
          <div class="sel">
            <el-button class="white" @click="butwhite"></el-button>
            <div class="colortext">白色</div>
          </div>
          <div style="margin-top: 1%" class="ip">
            <span>已选颜色：{{ colors }}</span
            ><span
              :style="{ background: backgroundColor }"
              class="showcolor"
            ></span>
          </div>
        </div>
      </div>
      <div class="sizes">
        <div class="colortit ot">请选择大小</div>
        <div class="selectsize">
          <el-button class="selsi" @click="butone">一寸</el-button>
          <el-button class="selsi" @click="buttwo">二寸</el-button>
          <!-- <el-button class="selsi" @click="butlitone">小一寸</el-button> -->
        </div>
        <div style="margin-top: 3%" class="ip">
          <span>已选尺寸：{{ sizes }}</span>
        </div>
      </div>
      <div class="yesok">
        <el-button class="but" @click="ok">确认</el-button>
      </div>
    </div>
    <!-- 其他 -->
    <div class="others">
      <div class="colortit" style="text-align: center">其他</div>
      <div class="otherphoto">
        <button class="thphoto" @click="tishi">
          <div><span>简历照片</span></div>
          <div class="otin">
            <span>像素: 295 x 413 px，</span> <span>冲印：25 x 35 mm</span>
          </div>
        </button>
        <button class="thphoto" @click="tishi">
          <div><span>自定义规格</span></div>
          <div class="otin">
            <span>尺寸: px / mm，</span> <span>文件大小，</span
            ><span>分辨率</span>
          </div>
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import { ElMessageBox } from "element-plus";

const cm_to_pixel = 118.110236;

export default {
  data() {
    return {
      colors: null,
      sizes: null,
      backgroundColor: null,
      colorlist: [],
      sizelist: [],
    };
  },
  mounted() {},
  methods: {
    tishi() {
      ElMessageBox.alert("尚在开发中哦,敬请期待~", "提示", {
        confirmButtonText: "确定",
        type: "error",
        showClose: false,
      });
    },
    banked() {
      this.$router.push({ name: "HomeViewMobile" });
    },
    ok() {
      const query = {
        color: this.colors,
        colorli: this.colorlist,
        size: this.sizes,
        sizeli: this.sizelist,
        csscolor: this.backgroundColor,
      };
      console.log(query);
      if (this.colors && this.sizes) {
        this.$router.push({ name: "SelectPhone", query });
      } else {
        ElMessageBox.alert("请选择底色或者尺寸", "提示", {
          confirmButtonText: "确定",
          type: "error",
          showClose: false,
        });
      }
    },
    butred() {
      this.colors = "红色";
      this.backgroundColor = "red";
      this.colorlist.length = 0;
      this.colorlist.push(255);
      this.colorlist.push(0);
      this.colorlist.push(0);
    },
    butblue() {
      this.colors = "蓝色";
      this.backgroundColor = "blue";
      this.colorlist.length = 0;
      this.colorlist.push(0);
      this.colorlist.push(0);
      this.colorlist.push(255);
    },
    butwhite() {
      this.colors = "白色";
      this.backgroundColor = "white";
      this.colorlist.length = 0;
      this.colorlist.push(255);
      this.colorlist.push(255);
      this.colorlist.push(255);
    },
    butone() {
      this.sizes = "一寸";
      this.sizelist.push(295);
      this.sizelist.push(413);
    },
    buttwo() {
      this.sizes = "两寸";
      this.sizelist.push(413);
      this.sizelist.push(578);
    },
  },
};
</script>
<style>
.ip {
  margin-left: 28%;
}
.showcolor {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin-left: 3%;
  border-radius: 50%;
}
.content {
  width: 99%;
  height: 100%;
  margin: auto;
  font-family: cursive;
  background-color: rgb(241, 241, 241);
}
.backs {
  margin-top: 1%;
  margin-left: 1%;
}
.id_photo {
  height: 50%;
  width: 100%;
  margin-top: 5%;
  border-radius: 10px;
}
.colortit {
  /* text-align: center; */
  background-color: rgb(186, 186, 186);
}
.colors {
  width: 100%;
  height: 30%;
  /* box-shadow: 4px 2px 4px rgba(0, 0, 0, 0.2); */
  background-color: rgb(235, 233, 233);
}
.sizes {
  width: 100%;
  height: 40%;
  /* background-color: aqua; */
  margin-top: 5%;
  margin-right: 45%;
  box-shadow: 4px 2px 4px rgba(0, 0, 0, 0.2);
  background-color: rgb(235, 233, 233);
}
.selectcolor {
  height: 50%;
  width: 100%;
  margin-top: 2%;
}
.sel {
  width: 20%;
  height: 20%;
  margin-top: 5%;
  margin-left: 9%;
  display: inline-block;
}
.ot {
  background-color: rgb(239, 239, 239);
  color: blue;
}
.red {
  border: none;
  background-color: red;
  margin-top: 10%;
  margin-left: 30%;
  border-radius: 50%;
}
.red:hover {
  background-color: red;
  border: 4px solid skyblue;
}
.white {
  border: none;
  background-color: white;
  margin-top: 10%;
  margin-left: 30%;
  border-radius: 50%;
}
.white:hover {
  background-color: white;
  border: 4px solid rgb(108, 200, 236);
}
.blue {
  border: none;
  background-color: blue;
  margin-top: 10%;
  margin-left: 30%;
  border-radius: 50%;
}
.blue:hover {
  background-color: blue;
  border: 4px solid skyblue;
}
.colortext {
  margin-top: 5%;
  text-align: center;
}
.selsi {
  background-color: skyblue;
  margin-left: 8%;
  margin-top: 10%;
}
.but {
  height: 40px;
  width: 90px;
  background-color: rgb(164, 226, 206);
  margin-left: 38%;
  margin-top: 5%;
}
.others {
  width: 100%;
}
.thphoto {
  width: 95%;
  height: 70px;
  margin-left: 2%;
  margin-top: 5%;
  box-shadow: 4px 2px 4px rgba(0, 0, 0, 0.2);
  background-color: white;
  border-radius: 10px;
  text-align: center;
  border: 0px solid;
}
.otin {
  margin-top: 2%;
}
</style>
