<template>
  <!-- 反馈弹窗 -->
  <div class="FeedbackPop-ups">
    <div class="feedback">
      <!-- 反馈类型 -->
      <div class="type">
        <p>反馈类型<span style="color: red">*</span></p>
        <el-radio-group v-model="importForm.radio">
          <el-radio :label="1">给本工具箱提交需求</el-radio>
          <el-radio :label="2">向本工具箱反馈缺陷</el-radio>
        </el-radio-group>
      </div>
      <!-- 需求 -->
      <div class="demand">
        <p>需求<span style="color: red">*</span></p>
        <el-input
          v-model="importForm.demand"
          placeholder="请用一句话描述你的需求"
        />
      </div>
      <!-- 需求简述 -->
      <div class="description">
        <p>需求简述</p>
        <el-input
          v-model="importForm.description"
          :rows="2"
          type="textarea"
          placeholder="请在此详细描述你的需求，如您要为本工具提出的建议具体有什么需求，或是本工具现存的有什么缺陷。未提供或描述不清，将作为无效问题关闭"
        />
      </div>
      <!-- 上传截屏 -->
      <div class="Take_a_screenshot">
        <p>上传截屏</p>
        <div class="upload">
          <div>
            <el-upload
              action=""
              accept="image/jpeg,image/gif,image/png"
              multiple="true"
              limit="5"
              :show-file-list="false"
              :on-change="onUploadChange"
              :auto-upload="false"
              :on-exceed="handleExceed"
            >
              <el-button size="small" type="primary"> 选取</el-button>
            </el-upload>
            <div class="upIMGs">
              <img
                class="upIMG"
                v-for="(image, index) in importForm.base64"
                :key="index"
                :src="image"
                alt="上传图片"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <button class="submit" @click="ShutDown">提交</button>
  </div>
</template>

<script >
export default {
  data() {
    return {
      block: "block",
      none: "none",

      // 反馈内容
      importForm: {
        radio: 1,
        demand: "",
        description: "",
        base64: [], // 存储base64数据的数组
      },

      fileList: [], // 显示上传内容
    };
  },
  methods: {
    // 文件状态改变时的钩子，添加文件、上传成功和上传失败时都会被调用
    onUploadChange(file) {
      console.log(file);
      console.log(this.fileList);
      const isIMAGE =
        file.raw.type === "image/jpeg" ||
        file.raw.type === "image/png" ||
        file.raw.type === "image/gif";
      const isLt1M = file.size / 1024 / 1024 < 1;

      if (!isIMAGE) {
        this.$message.error("上传文件只能是图片格式!");
        return false;
      }
      if (!isLt1M) {
        this.$message.error("上传文件大小不能超过 1MB!");
        return false;
      }
      let reader = new FileReader();
      reader.readAsDataURL(file.raw);
      reader.onload = () => {
        const base64Data = reader.result; // 图片的base64数据
        this.importForm.base64.push(base64Data); // 将base64数据添加到数组中
        console.log(this.importForm.base64);
      };
    },
    // 上传上限提示
    handleExceed() {
      this.$message.error("只能上传5张图片");
    },

    // 提交反馈
    ShutDown() {
      console.log(this.importForm);
      this.$router.push({
        name: "ProblemFeedback",
      });
    },
  },
};
</script>

<style lang="less" scoped>
.FeedbackPop-ups {
  position: relative;
  box-sizing: border-box;
  width: 65%;
  min-width: 500px;
  height: 500px;
  margin: auto;
  background: #f0f4f6;
  padding: 20px;
  border-radius: 5px;

  .feedback {
    position: relative;
    padding: 10px;
    p {
      width: 150px;
    }
    .type,
    .demand,
    .description,
    .Take_a_screenshot {
      display: flex;
      margin-bottom: 20px;
    }
    /deep/ .el-upload-list {
      height: 120px;
      overflow: auto;
    }
    // 图片上传大小
    /deep/.el-upload--picture-card {
      --el-upload-picture-card-size: 80px;
    }
  }
  .submit {
    position: absolute;
    right: 50px;
    bottom: 20px;
    width: 50px;
    height: 30px;
    background: #f0f4f6;
    border: 1px solid #c9dae2;
    border-radius: 5px;
    margin-right: 10px;
    &:hover {
      background: #c9dae2;
      border: 1px solid #464879;
    }
  }
}

// 组件样式
/deep/.el-radio__input.is-checked .el-radio__inner {
  border-color: #464879;
  background: #464879;
}
/deep/.el-radio__input.is-checked + .el-radio__label {
  color: #464879;
}
/deep/.el-input__wrapper {
  display: block;
  margin: 0 25px;
}
/deep/.el-textarea__inner {
  width: 93%;
  margin: 0 25px;
  height: 100px;
  max-height: 100px;
}

/deep/.el-upload-list el-upload-list--picture-card {
  span {
    width: 50px;
    height: 50px;
  }
}

/deep/span .el-upload-list__item-actions {
  width: 50px;
}

.upload {
  display: flex;
  width: 80%;
  height: 160px;
  overflow: auto;
  .upIMGs {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    .upIMG {
      max-width: 280px;
      max-height: 80px;
      margin-top: 10px;
    }
  }
}
</style>