<template>
  <div class="chatGpt">
    <!-- 左边区域 -->
    <div class="left">
      <el-drawer
        v-model="leftListShow"
        :direction="'ltr'"
        :size="'70%'"
        title="对话列表"
      >
        <div class="leftList">
          <div class="leftHeader">
            <el-button @click="newChart"
              ><el-icon><Plus /></el-icon>新的对话</el-button
            >
            <div class="HiddenIcon"></div>
          </div>
          <el-scrollbar>
            <p
              v-for="(item, index) in conversationList"
              :key="index"
              @click.stop="selectMsg(item, index)"
              :class="{ selected: selectedIndex === index }"
            >
              <template v-if="isEditing && index === editingIndex">
                <input
                  type="text"
                  v-model="item.title"
                  ref="Editing"
                  @keyup.enter="updateMsg(item)"
                  @blur="this.isEditing = false"
                />
              </template>
              <template v-else>
                <span :title="item.title">{{ item.title }}</span>
              </template>
              <span class="operations">
                <el-icon @click.stop="deleteMsg(item)"><Delete /></el-icon>
                <el-icon @click.stop="Editing(index)"><EditPen /></el-icon>
              </span>
            </p>
          </el-scrollbar>
          <div class="leftFooter">
            <p>
              <el-icon><User /></el-icon>升级为会员
            </p>
            <div @click="toUser" v-if="user" class="user">
              <span>{{ user.username.slice(0, 2) }}</span>
              <p>{{ user.username }}</p>
            </div>
            <p class="toHome" @click="toHome">
              <el-icon><House /></el-icon>返回首页
            </p>
          </div>
        </div>
      </el-drawer>
    </div>
    <!-- 右边区域 -->
    <div class="right" ref="rightView">
      <div class="rightHeader">
        <el-button
          v-if="!leftListShow"
          @click="this.leftListShow = !this.leftListShow"
          class="openLeft"
          ><el-icon><Fold /></el-icon
        ></el-button>
        <p class="title">{{ localTitle }}</p>
        <el-button @click="newChart"
          ><el-icon><Plus /></el-icon
        ></el-button>
      </div>
      <!-- 内容区 -->
      <el-scrollbar ref="scrollBar" v-if="msgList.length != 0">
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
        <span class="null"></span>
      </el-scrollbar>
      <button class="showButton" v-if="isGenerating" @click="stopGenerate">
        <el-icon><CircleClose /></el-icon>
        停止生成
      </button>
      <button class="showButton" v-if="showReGenerate" @click="reGenerate">
        <el-icon><Refresh /></el-icon>
        重新生成
      </button>
      <h1 v-if="msgList.length == 0">模型</h1>
      <div class="sendMsg">
        <el-input
          autosize
          v-model="message"
          placeholder="请输入"
          style="height: 100%; border: none"
          @keyup.enter="sendMessageByWebSocket"
        />
        <el-button :disabled="isWaiting" @click="sendMessageByWebSocket"
          ><el-icon><Promotion /></el-icon
        ></el-button>
      </div>
    </div>
  </div>
</template>

<script>
import deviceMixin from "@/mixins/deviceMixin.js";
import * as chatApi from "@/api/chatApi";
import { ElMessage } from "element-plus";
import md from "@/components/gpt/markdownInterpreter.js";
import ChatContentMixin from "@/components/gpt/ChatContentMixin";

export default {
  mixins: [deviceMixin, ChatContentMixin],
  data() {
    return {
      selectedIndex: -1,
      isEditing: false, // 添加编辑状态
      editingIndex: null, // 编辑index
      leftListShow: false,
      message: null, //要发送的消息
      isWaiting: false,
      localconversationId: null, //当前对话id
      localTitle: null, //当前对话title
    };
  },
  watch: {
    async localconversationId(newVal, oldVal) {
      if (newVal != null) {
        await this.getMsgDetil(newVal);
        this.leftListShow = false;
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
  },
  methods: {
    //markedown解析
    render(text) {
      let render = md.render(text.replace(/\\n/g, "\n"));
      return render;
    },
    //新增消息
    async newChart() {
      try {
        let res = await chatApi.newChart();
        this.conversationList.unshift(res);
        this.$fetchData.fetchConversationList();
        this.localconversationId = res.id;
        this.localTitle = res.title;
        this.selectedIndex = -1;
        this.leftListShow = false;
      } catch (error) {
        if (error) {
          ElMessage.error(error.error);
        }
      }
    },
    //选择列表
    async selectMsg(item, index) {
      this.selectedIndex = index;
      this.localconversationId = item.id;
      this.localTitle = item.title;
      this.leftListShow = false;
    },
    //修改列表
    async updateMsg(item) {
      try {
        let res = await chatApi.updatedMsg(item.id, { title: item.title });
        this.$fetchData.fetchConversationList();
        this.isEditing = false;
      } catch (error) {
        ElMessage.error("请求出错请重试");
      }
    },
    //删除列表
    async deleteMsg(item) {
      try {
        let res = await chatApi.deleteMsg(item.id);
        this.$fetchData.fetchConversationList();
        this.localconversationId = null;
        this.localTitle = null;
        this.msgList = [];
        this.leftListShow = false;
        ElMessage.success("删除成功");
        
      } catch (error) {
        if (error) {
          ElMessage.error(error.error);
        }
      }
    },
    Editing(index) {
      this.isEditing = true;
      this.editingIndex = index;
      this.$nextTick(() => {
        if (this.$refs.Editing) {
          console.log(this.$refs.Editing);
          this.$refs.Editing[0].focus();
        }
      });
    },
     //跳转首页
    toHome() {
      this.$router.push({
        name: "home",
      });
    },
    //跳转用户中心
    toUser() {
      this.$router.push({
        name: "PersonalInformation",
      });
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
li {
  list-style: none;
}
a {
  text-decoration: none;
}
.chatGpt {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
  justify-content: center;
}

.v-enter-active {
  animation: slidein 0.2s linear;
}
.v-leave-active {
  animation: slidein 0.2s linear reverse;
}
@keyframes slidein {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0px);
  }
}

/* 以下为左边样式 */
>>> .el-drawer {
  position: absolute;
  box-sizing: border-box;
  background-color: #050509;
  display: flex;
  flex-direction: column;
  box-shadow: var(--el-box-shadow-dark);
  overflow: hidden;
  transition: all var(--el-transition-duration);
}
>>> .el-drawer__body {
  display: flex;
  justify-content: space-around;
  flex: 1;
  padding: 0;
  overflow: auto;
}
>>> .el-drawer__header {
  margin-bottom: 7px;
}
.leftList {
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  background-color: #050509;
  opacity: 0.9;
  box-sizing: border-box;
  align-content: space-between;
}

.leftHeader {
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
  justify-content: center;
  max-height: 55px;
}
.leftList .el-button {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
  height: 44px;
  width: 98%;
  background-color: #050509;
  border: var(--el-border);
  border-color: hsla(0, 0%, 100%, 0.2);
  font-size: var(--el-font-size-base);
  border-radius: 0.375rem;
  margin: 10px;
  /* flex: 1; */
}
.leftHeader .el-icon:nth-of-type(1) {
  margin-right: 15px;
}
.HiddenIcon .el-button {
  color: rgba(255, 255, 255, var(--tw-text-opacity));
  height: 44px;
  width: 44px;
  text-align: center;
  background-color: #050509;
  border: var(--el-border);
  border-color: hsla(0, 0%, 100%, 0.2);
  font-size: var(--el-font-size-base);
  border-radius: 0.375rem;
  margin-top: 10px;
  margin-right: 13px;
}
>>> .HiddenIcon span {
  display: inline-block;
  width: 15px;
  height: 15px;
}
.leftList .el-scrollbar {
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  padding: 0 5%;
  background-color: #050509;
}
.leftList >>> .el-scrollbar__wrap {
  max-width: 100%;
}
.leftList .el-scrollbar p {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 44px;
  margin: 10px 0 10px 0;
  text-align: center;
  border-radius: 4px;
  background: #050509;
  color: #ffffff;
  overflow: hidden;
  font-size: 14px;
}
.leftList .el-scrollbar p span {
  max-width: 70%;
  white-space: nowrap; /* 防止文字换行 */
  overflow: hidden; /* 隐藏超出容器的部分 */
  text-overflow: ellipsis; /* 在溢出时显示省略号 (...) */
}
/* 选中样式 */
.leftList .el-scrollbar .selected {
  background: #3a3a40;
}
.leftList .el-scrollbar p .el-icon {
  --color: #737382;
  float: right;
  margin-left: 10px;
}
.leftList .el-scrollbar p .el-icon:hover {
  --color: #a5a5be;
}
.leftFooter {
  max-height: 150px;
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-around;
  align-items: flex-start;
  flex: 0 0 150px;
  padding: 10px 0;
  align-items: center;
  background-color: #050509;
  border-top: 1px solid #d9d9e3;
  margin-top: 3px;
}

.leftFooter > * {
  display: flex;
  flex-flow: row nowrap;
  justify-content: flex-start;
  align-items: center;
  width: 90%;
  font-size: 14px;
}

.leftFooter p:nth-child(1) {
  width: 92%;
  height: 44px;
  background-color: #050509;
  border-radius: 4px;
  line-height: 44px;
  color: #ffffff;
  padding-left: 25px;
  box-sizing: border-box;
}
.leftFooter p:nth-child(n):hover {
  background-color: #4a4a51;
}
.leftFooter .user {
  width: 92%;
  height: 50px;
  display: flex;
  flex-flow: row nowrap;
  justify-items: center;
  align-items: center;
  overflow: hidden;
  background-color: #050509;
  border-radius: 4px;
  padding-left: 30px;
  box-sizing: border-box;
}
.leftFooter .el-icon {
  --color: #ffffff;
  height: 2em;
  width: 2em;
  line-height: 1em;
  display: inline-flex;
  fill: currentColor;
  color: var(--color);
  font-size: inherit;
  margin: 5px 10px;
}
.leftFooter .user:hover {
  background-color: #4a4a51;
}
.user span {
  display: flex;
  width: 36px;
  height: 36px;
  justify-content: center;
  align-items: center;
  background-color: #7b7c38;
  margin: 12px;
  color: #ffffff;
}
.user p {
  display: inline-block;
  color: #ffffff;
  float: left;
  line-height: 34px;
}
.user .el-icon {
  width: 15px;
  height: 15px;
  float: right;
  margin-top: 24px;
}
.toHome {
  color: #ffffff;
  border-radius: 5px;
  display: flex;
  flex-flow: row nowrap;
  padding-left: 30px;
}
.operations {
  /* display: none; */
}

.leftList .el-scrollbar p:hover .operations {
  display: inline-block;
}

/* 以下为右边样式 */
.right {
  display: flex;
  flex-direction: column;
  max-width: 100%;
  max-height: 100%;
  transition: all 0.3s linear;
  flex-grow: 1;
  font-size: 16px;
  line-height: 25px;
  box-sizing: border-box;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
}
.rightHeader {
  width: 100%;
  position: relative;
  min-height: 21px;
  max-height: 32px;
  height: 5%;
  background-color: #050509;
  text-align: center;
}
.rightHeader p {
  width: 50%;
  font-size: 14px;
  color: #fff;
  display: inline-block;
  white-space: nowrap; /* 防止文字换行 */
  overflow: hidden; /* 隐藏超出容器的部分 */
  text-overflow: ellipsis; /* 在溢出时显示省略号 (...) */
}
.rightHeader .el-button {
  width: 44px;
  height: 100%;
  background-color: #050509;
  position: absolute;
  right: 0;
  top: 0;
}
.rightHeader .el-icon {
  --color: #fff;
}
.sendMsg {
  width: 85%;
  height: 44px;
  border-radius: 10px;
  box-shadow: rgb(125, 124, 124) 0px 0px 10px;
  display: flex;
  justify-content: space-around;
  flex: 0 0 44px;
}
>>> .sendMsg .el-input {
  --el-input-height: var(--el-component-size);
  font-size: var(--el-font-size-base);
  display: inline-flex;
  width: 93%;
  line-height: var(--el-input-height);
  box-sizing: border-box;
  vertical-align: middle;
  border: none;
  outline: none;
}
.sendMsg .el-button {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
  height: 100%;
  width: 10%;
  min-width: 44px;
  background-color: #ffffff;
  font-size: var(--el-font-size-base);
  border: none;
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
  position: absolute;
  top: 0;
  left: 0;
  width: 44px;
  height: 100%;
  background-color: #050509;
  color: #fff;
}
.right .el-scrollbar {
  width: 100%;
  height: 89%;
  flex: 1 1 86%;
}
.content {
  max-width: 100%;
  width: 100%;
}
.content p {
  display: inline-block;
  text-align: center;
  word-wrap: break-word;
  word-break: break-all;
  flex-wrap: nowrap;
  color: rgb(55, 65, 81);
  font-family: Söhne, ui-sans-serif;
  font-size: 14px;
}
.request {
  display: flex;
  align-items: center;
  min-height: 50px;
  position: relative;
  padding: 1.5% 10% 1.5% 20%;
  background-color: #fff;
}
.request p {
  text-align: start;
}
.request span {
  display: flex;
  position: absolute;
  width: 36px;
  height: 36px;
  left: 4%;
  top: 10%;
  border-radius: 2px;
  justify-content: center;
  align-items: center;
  background-color: #079802;
}
.response {
  position: relative;
  padding: 1.5% 10% 1.5% 20%;
  border: 1px solid #cacacb;
  background-color: rgba(249, 249, 255, 0.8);
  color: rgb(55, 65, 81);
  font-family: Söhne, ui-sans-serif;
  font-size: 14px;
  min-height: 50px;
}
.response img {
  position: absolute;
  width: 36px;
  height: 36px;
  opacity: 0.9;
  left: 4%;
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
>>> .loading {
  box-sizing: border-box;
  width: 100%;
  height: 70px;
  border: 1px solid #cacacb;
  background-color: rgba(244, 244, 252, 0.8);
  z-index: 0;
}
>>> code {
  font-size: 14px;
  font-weight: 600;
  font-variation-settings: normal;
  font-family: "Söhne Mono", Monaco;
  tab-size: 4;
  white-space: pre-line;
}
>>> pre code {
  overflow: scroll;
  white-space: pre-wrap;
  overflow-x: scroll;
}
.showButton {
  width: 85px;
  height: 22px;
  position: absolute;
  right: 2%;
  bottom: 60px;
  background-color: rgb(255, 255, 255);
  border: 1px solid rgba(0, 0, 0, 0.1);
  font-size: 14px;
  font-weight: 400;
  color: rgb(64, 65, 79);
  border-radius: 4px;
  z-index: 999;
}
.el-scrollbar button:hover {
  background-color: rgb(228, 228, 228);
}
.null {
  display: block;
  height: 38px;
}
</style>
