<template>
  <!-- 左边区域 -->
  <div class="leftList">
    <div class="leftHeader">
      <el-button @click="newChart"
        ><el-icon><Plus /></el-icon>新的对话</el-button
      >
      <div class="HiddenIcon">
        <el-button @click="switchLeft"
          ><svg
            viewBox="0 0 1024 1024"
            xmlns="http://www.w3.org/2000/svg"
            data-v-ea893728=""
          >
            <path
              fill="currentColor"
              d="M896 192H128v128h768V192zm0 256H384v128h512V448zm0 256H128v128h768V704zM320 384 128 512l192 128V384z"
            ></path>
          </svg>
        </el-button>
      </div>
    </div>

    <el-scrollbar>
      <div>
        <p
          v-for="(item, index) in conversationList"
          :key="index"
          @click.stop="selectMsg(item, index)"
          @mouseenter="handleMouseEnter(index)"
          @mouseleave="handleMouseLeave"
          :class="{ selected: selectedIndex === index }"
        >
          <template v-if="isEditing && currentHoverIndex === index">
            <input
              type="text"
              v-model="item.title"
              ref="Editing"
              @keyup.enter="updateMsg(item)"
            />
            <el-icon @click="isEditing = false"><CloseBold /></el-icon>
            <el-icon @click="updateMsg(item)"><Select /></el-icon>
          </template>
          <template v-else>
            <span :title="item.title">{{ item.title }}</span>
            <span class="operations">
              <el-icon @click.stop="deleteMsg(item,index)"><Delete /></el-icon>
              <el-icon @click.stop="Editing(index)"><EditPen /></el-icon>
            </span>
          </template>
        </p>
      </div>
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
</template>

<script>
import * as chatApi from "@/api/chatApi";
import { ElMessage } from "element-plus";
import { mapState } from "vuex";
export default {
  props: {
    leftListShow: {},
  },
  data() {
    return {
      selectedIndex: -1,
      currentHoverIndex: -1,
      selectedConversationId: null, //选中对话
      isEditing: false, // 添加编辑状态
    };
  },
  computed: {
    ...mapState(["conversationList", "user"]),
  },
  methods: {
    switchLeft() {
      this.$emit("close", false);
    },
    //新增消息
    async newChart() {
      try {
        let res = await chatApi.newChart();
        this.conversationList.unshift(res);
        this.deliver(res.id, res.title);
        this.selectedIndex = -1;
        this.$fetchData.fetchConversationList();
      } catch (error) {
        if (error) {
          ElMessage.error(error.error);
        }
      }
    },
    //选择列表
    async selectMsg(item, index) {
      this.selectedIndex = index;
      this.selectedConversationId = item.id;
      this.deliver(this.selectedConversationId, item.title);
    },
    //传递参数给父组件
    deliver(id, title) {
      this.$emit("selectConversation", id);
      this.$emit("selectConversationTitle", title);
    },
    //修改列表
    async updateMsg(item) {
      console.log("修改");
      try {
        let res = await chatApi.updatedMsg(item.id, { title: item.title });
        this.$fetchData.fetchConversationList();
        this.isEditing = false;
      } catch (error) {
        ElMessage.error("请求出错请重试");
      }
    },
    //删除列表
    async deleteMsg(item,index) {
      try {
        let res = await chatApi.deleteMsg(item.id);
        this.$fetchData.fetchConversationList();
        if( this.selectedIndex = index){
         this.deliver(null, null);
         this.selectedIndex = -1
        }
        ElMessage.success("删除成功");
      } catch (error) {
        if (error) {
          ElMessage.error(error.error);
        }
      }
    },

    Editing(index) {
      this.isEditing = true;
      this.$nextTick(() => {
        if (this.$refs.Editing) {
          this.$refs.Editing[0].focus();
        }
      });
    },
    handleMouseEnter(index) {
      this.currentHoverIndex = index;
    },
    handleMouseLeave() {
      this.isEditing = false;
      this.currentHoverIndex = -1;
    },
    finishEditing(item) {
      this.updateMsg(item);
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
.leftList {
  position: relative;
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  width: 18%;
  max-width: 300px;
  min-width: 200px;
  height: 100vh;
  max-height: 100vh;
  background-color: #050509;
  opacity: 0.9;
  box-sizing: border-box;
  justify-content: space-between;
}

.leftHeader {
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  /* flex: 0 0 70px; */
}
.leftList .el-button {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
  height: 44px;
  width: 60%;
  background-color: #050509;
  border: var(--el-border);
  border-color: hsla(0, 0%, 100%, 0.2);
  font-size: var(--el-font-size-base);
  border-radius: 0.375rem;
  margin-left: 10px;
  margin-top: 10px;
  flex: 1;
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
.el-scrollbar {
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  /* height: 70%;
  max-height: 69%; */
  background-color: #050509;
  flex: 1 1 70%;
}
>>> .el-scrollbar__wrap {
  width: 100%;
}

.el-scrollbar p {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-around;
  width: 90%;
  height: 44px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: #050509;
  color: #ffffff;
  overflow: hidden;
}
.el-scrollbar p span {
  max-width: 70%;
  white-space: nowrap; /* 防止文字换行 */
  overflow: hidden; /* 隐藏超出容器的部分 */
  text-overflow: ellipsis; /* 在溢出时显示省略号 (...) */
}
/* 选中样式 */
.el-scrollbar .selected {
  background: #3a3a40;
}
.el-scrollbar p .el-icon {
  --color: #737382;
  float: right;
  margin-left: 10px;
}
.el-scrollbar p .el-icon:hover {
  --color: #a5a5be;
}
.el-scrollbar p:hover {
  background-color: #4a4a51;
  opacity: 0.8;
}
.leftFooter {
  width: 100%;
  max-height: 152px;
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-around;
  align-items: flex-start;
  flex: 0 0 150px;
  padding: 10px 0;
  align-items: center;
  background-color: #050509;
  box-sizing: border-box;
  border-top: 1px solid #d9d9e3;
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
  width: 100%;
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
  /* justify-content: center;
    align-items: center; */
  fill: currentColor;
  color: var(--color);
  font-size: inherit;
  margin: 5px 10px;
}
.leftFooter .user:hover {
  background-color: #4a4a51;
}
>>> .el-scrollbar__view {
  height: 100%;
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
  display: none;
}

.el-scrollbar p:hover .operations {
  display: inline-block;
}
</style>
