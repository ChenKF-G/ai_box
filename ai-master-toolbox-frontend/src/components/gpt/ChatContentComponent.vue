<template>
  <!-- 右边区域 -->
  <div class="right" ref="rightView">
    <el-button v-if="!leftListShow" @click="switchLeft" class="openLeft"
      ><el-icon><Fold /></el-icon
    ></el-button>
    <!-- 内容区 -->
    <div v-if="msgList.length != 0" class="rightScroll">
      <el-scrollbar ref="scrollBar">
        <div ref="scrollBarInner">
          <div class="content" v-for="(item, index) in msgList" :key="index">
            <div class="request" v-if="item.role == 'user'">
              <span>Me</span>
              <p>{{ item.content }}</p>
            </div>
            <div class="response" v-else>
              <img src="@/assets/chatLogo.png" alt="" />
              <div v-html="render(item.content)"></div>
            </div>
          </div>
        </div>
        <div v-if="isWaiting" class="loading" v-loading="isWaiting"></div>
      </el-scrollbar>
      <button v-if="isGenerating" @click="stopGenerate">
        <el-icon><CircleClose /></el-icon>停止生成
      </button>
      <button v-if="showReGenerate" @click="reGenerate">
        <el-icon><Refresh /></el-icon>重新加载
      </button>
    </div>
    <h1 v-if="msgList.length == 0">模型</h1>
    <div v-if="msgList.length == 0" class="recommend">
      <div class="list" v-for="item in 4" :key="item">
        <div class="title">Brainstorm names</div>
        <div class="context">
          for my fantasy football team with a frog theme
        </div>
      </div>
    </div>
    <div class="sendMsg">
      <el-input
        @keyup.enter="sendMessageByWebSocket"
        autosize
        v-model="message"
        placeholder="请输入"
        style="height: 100%; border: none"
      />
      <el-button
        :disabled="isWaiting || isGenerating"
        @click="sendMessageByWebSocket"
        ><el-icon><Promotion /></el-icon
      ></el-button>
    </div>
  </div>
</template>

<script>
import md from "./markdownInterpreter.js";
import ChatContentMixin from "./ChatContentMixin";

export default {
  mixins: [ChatContentMixin],
  data() {
    return {
      localconversationId: null, //当前对话id
      localTitle: null, //当前对话title
      loadingId: null, //等待id
    };
  },
  props: {
    leftListShow: {},
    conversationId: {}, //当前对话id
    selectConversationTitle: {},
  },
  watch: {
    async conversationId(newVal, oldVal) {
      if (this.loadingId != newVal) {
        this.isWaiting = false;
      }
      if(newVal){
        this.localconversationId = newVal;
      await this.getMsgDetil(newVal);
      }else{
        this.localconversationId = null
        this.$store.state.gptMessageList = []
      }
    },
    msgList: {
      handler() {
        setTimeout(() => {
          this.scrollToBottom();
        });
      },
      deep: true, // 深度监听数组内部元素的变化
    },
    selectConversationTitle(newVal, oldVal) {
      this.localTitle = newVal;
    },
  },
  methods: {
    //markedown解析
    render(text) {
      let render = md.render(text.replace(/\\n/g, "\n"));
      return render;
    },
    //左边列表开关
    switchLeft() {
      this.$emit("open", true);
    },
  },
};
</script>

<style scoped>
.right {
  height: 100%;
  position: relative;
  transition: all 0.3s linear;
  flex-grow: 1;
  font-size: 16px;
  line-height: 25px;
  box-sizing: border-box;
  flex: 1 1 82%;
}
.recommend {
  width: 63%;
  height: 130px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-content: space-between;
  position: absolute;
  top: 69%;
  left: 21%;
}
.recommend .list {
  width: 49%;
  height: 45%;
  background-color: #ffffff;
  border-radius: 10px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.recommend .list:hover {
  background-color: #d9d9e3;
}

.recommend .title {
  font-weight: 600;
  padding-left: 20px;
  text-align: start;
  line-height: 250%;
  color: #40414f;
  font-size: 14px;
  width: 85%;
  height: 50%;
}
.recommend .context {
  padding-left: 20px;
  text-align: start;
  color: #95959e;
  font-size: 14px;
  width: 85%;
  height: 50%;
}
.sendMsg {
  min-height: 40px;
  width: 63%;
  height: 7%;
  position: absolute;
  bottom: 4%;
  left: 21%;
  border-radius: 10px;
  box-shadow: rgb(125, 124, 124) 0px 0px 10px;
  display: flex;
  justify-content: space-around;
  max-height: 44px;
}
.sendMsg .el-input {
  --el-input-height: var(--el-component-size);
  font-size: var(--el-font-size-base);
  display: inline-flex;
  width: 93%;
  line-height: var(--el-input-height);
  box-sizing: border-box;
  vertical-align: middle;
}
.sendMsg .el-button {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
  height: 100%;
  width: 10%;
  min-width: 44px;
  background-color: #ffffff;
  font-size: var(--el-font-size-base);
}
.sendMsg .el-icon {
  --color: #40414f;
  width: 15px;
  height: 15px;
}
.right h1 {
  text-align: center;
  font-size: 50px;
  margin: 150px auto;
  opacity: 0.3;
}
.openLeft {
  z-index: 10;
  position: absolute;
  top: 2%;
  left: 1.5%;
}
.right .rightScroll {
  height: 89%;
  position: relative;
}

.rightScroll .el-scrollBar {
  height: 100%;
}
.content {
  max-width: 100%;
}
.content p {
  display: inline-block;
  text-align: center;
  font-size: 16px;
  word-wrap: break-word;
  word-break: break-all;
  flex-wrap: nowrap;
  color: rgb(55, 65, 81);
  font-family: Söhne, ui-sans-serif;
  font-size: 16px;
}
.request {
  position: relative;
  padding: 2% 26%;
  background-color: #fff;
  display: flex;
  align-items: center;
}
.request p {
  text-align: start;
}
.request span {
  display: flex;
  position: absolute;
  width: 36px;
  height: 36px;
  left: 20%;
  top: 25%;
  border-radius: 2px;
  justify-content: center;
  align-items: center;
  background-color: #079802;
}
.response {
  position: relative;
  padding: 1.5% 26%;
  border: 1px solid #cacacb;
  background-color: rgba(249, 249, 255, 0.8);
  color: rgb(55, 65, 81);
  font-family: Söhne, ui-sans-serif;
  font-size: 16px;
  min-height: 28px;
  max-width: 100%;
}
.response img {
  position: absolute;
  width: 36px;
  height: 36px;
  opacity: 0.9;
  left: 20%;
}
>>> .copy-textarea {
  position: absolute;
  left: -9999px;
  top: -9999px;
}
>>> pre {
  font-size: 16px;
  margin-bottom: 10px;
  position: relative;
  line-height: 25px;
}
>>> .codeBlockHeader {
  display: flex;
  flex-flow: row nowrap;
  height: 25px;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  background-color: rgb(52, 53, 65);
  color: rgb(217, 217, 227);
  font-size: 12px;
  margin-top: 10px;
  padding: 10px;
  box-sizing: border-box;
}
>>> .codeBlockHeader b {
}
>>> .codeBlockHeader button {
  position: absolute;
  right: 5px;
  background-color: #514f4f;
  color: rgb(217, 217, 227);
}
.loading {
  box-sizing: border-box;
  width: 100%;
  height: 70px;
  border: 1px solid #cacacb;
  background-color: rgba(244, 244, 252, 0.8);
}
>>> code {
  font-size: 14px;
  font-weight: 600;
  font-variation-settings: normal;
  font-family: "Söhne Mono", Monaco;
  white-space: pre-line;
  tab-size: 4;
  white-space: pre-wrap;
}
.rightScroll button {
  display: flex;
  align-items: center;
  height: 30px;
  position: absolute;
  right: 5%;
  bottom: 5%;
  background-color: rgb(255, 255, 255);
  border: 1px solid rgba(0, 0, 0, 0.1);
  font-size: 14px;
  font-weight: 400;
  padding: 8px 12px;
  color: rgb(64, 65, 79);
  align-items: center;
  border-radius: 4px;
  z-index: 999;
}

.rightScroll button .el-icon {
  margin-right: 10px;
}
.rightScroll button:hover {
  background-color: rgb(228, 228, 228);
}
</style>
