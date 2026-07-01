import Cookies from "js-cookie";
import { ElMessage } from "element-plus";
import * as chatApi from "@/api/chatApi";
import { mapState, mapMutations } from "vuex";
import config from "@/config.json";

const EventType = {
  auth: "auth",
  send_message: "send_message",
  send_received: "send_received",
  response_message: "response_message",
  response_finished: "response_finished",
  re_generate: "re_generate",
  title_changed: "title_changed",
  error: "error",
};

const environment = process.env.NODE_ENV;
const socketUrl = config["socketUrl"][environment];

export default {
  data() {
    return {
      message: "", //要发送的消息
      isWaiting: false,
      isGenerating: false,
    };
  },
  async created() {
    try {
      await this.$fetchData.fetchUser(false);
      try {
        this.createSocket();
      } catch (error) {}
      this.$fetchData.fetchConversationList(false);
    } catch {}
  },
  beforeUnmount() {
    try {
      this.socket.close();
    } catch (error) {}
  },
  computed: {
    ...mapState(["conversationList", "user", "gptMessageList", "socket"]),
    conversation() {
      if (!this.localconversationId) return null;
      if (this.conversationList) {
        return this.conversationList.find(
          (item) => item.id === this.localconversationId
        );
      } else {
        return null;
      }
    },
    msgList() {
      if(this.gptMessageList){
        let res = this.gptMessageList[this.localconversationId];
      return res ? res : [];
      }
    },
    showReGenerate() {
      if (
        this.isWaiting == false &&
        this.isGenerating == false &&
        this.msgList.length > 0
      ) {
        return true;
      }
      return false;
    },
  },
  methods: {
    ...mapMutations(["set_Socket"]),
    //停止生成
    stopGenerate() {
      this.isWaiting = false;
      this.isGenerating = false;
      this.socket.close();
    },
    //重新生成
    reGenerate() {
      if (this.msgList.length <= 0) return;
      this.isWaiting = true;
      this.loadingId = this.conversationId;
      let lastMessage = this.msgList[this.msgList.length - 1];
      if (lastMessage.role == "assistant") {
        lastMessage.content = "";
      }
      let send_data = {
        eventType: EventType.re_generate,
        conversation_id: this.localconversationId,
      };

      this.createSocket().then(() => {
        this.socket.send(JSON.stringify(send_data));
      });
    },
    async sendMessageByWebSocket() {
      if (!this.message) return;
      if (this.isWaiting) return;
      this.isWaiting = true;
      // 如果没有会话，新建一个
      if (this.msgList.length === 0 && this.localconversationId == null) {
        try {
          let res = await chatApi.newChart();
          this.conversationList.unshift(res);
          this.localconversationId = res.id;
          this.loadingId = this.localconversationId;
          this.localTitle = res.title;
          this.gptMessageList[this.localconversationId] = [];
        } catch (error) {
          if (error) {
            ElMessage.error(error.error);
            this.isWaiting = false;
          }
          return;
        }
      }
      this.gptMessageList[this.localconversationId].push({
        role: "user",
        content: this.message,
      });
      let send_data = {
        eventType: EventType.send_message,
        content: this.message,
        conversation_id: this.localconversationId,
      };

      this.message = null;

      this.createSocket().then(async () => {
        this.socket.send(JSON.stringify(send_data));
      });
    },
    //滚动栏自动滚动到底部
    scrollToBottom() {
      this.$nextTick(() => {
        // 获取滚动容器的引用
        const scrollBar = this.$refs.scrollBar;
        const scrollInner = this.$refs.scrollBarInner;
        if (!scrollBar) {
          return;
        }
        // // 滚动到底部
        scrollBar.setScrollTop(scrollInner.clientHeight);
      });
    },
    //获取历史消息详情
    async getMsgDetil(id) {
      if (this.gptMessageList[this.localconversationId]) return;
      try {
        const res = await chatApi.getMsgDetil(id);
        this.gptMessageList[this.localconversationId] = res;
      } catch {
        if (!error) {
          return;
        }
        ElMessage({
          message: error.error,
          type: "warning",
        });
      }
    },
    createSocket() {
      return new Promise((resolve, errorHandler) => {
        try {
          if (!this.socket) {
            const socket = new WebSocket(socketUrl + "/ws/chat_socket/");
            this.set_Socket(socket);
            // 处理连接打开事件
            socket.onopen = () => {
              // 发送权限信息
              let authData = {
                eventType: EventType.auth,
                user_id: this.user.id,
                token: Cookies.get("token"),
              };
              socket.send(JSON.stringify(authData));
            };

            // 处理接收到的消息事件
            socket.onmessage = async (event) => {
              let data = JSON.parse(event.data);
              if (data.eventType == EventType.auth) {
                resolve();
              } else if (data.eventType == EventType.send_received) {
              } else if (data.eventType == EventType.response_message) {
                this.isWaiting = false;
                this.isGenerating = true;
                let content = data.content;
                let conversation_id = data.conversation_id;
                let role = data.role;
                const msgList = this.gptMessageList[conversation_id];
                msgList[msgList.length - 1].role != role;
                if (msgList[msgList.length - 1].role != role) {
                  msgList.push({ role: role, content: "" });
                } else {
                  msgList[msgList.length - 1].content += content;
                }
              } else if (data.eventType == EventType.response_finished) {
                this.isGenerating = false;
              } else if (data.eventType == EventType.title_changed) {
                let content = data.content;
                let conversation_id = data.conversation_id;
                if (
                  this.conversation &&
                  this.conversation.id == conversation_id
                ) {
                  if (this.conversation.title == "无标题") {
                    this.conversation.title = "";
                  }
                  this.conversation.title += content;
                }
              } else if (data.eventType == EventType.error) {
                this.isGenerating = false;
                this.isWaiting = false;

                const error = data.content;
                if (error.code) {
                  if (error.code == 401) {
                    // 没有用户信息，转到登录页面
                    ElMessage.error("用户信息已过期，请登录");
                    this.$router.push({ name: "login" });
                  } else if (error.code == 426) {
                    // 已经超过了免费使用次数，需要升级
                    ElMessage({
                      message: "已经超过了免费使用次数，请升级",
                      type: "warning",
                    });
                  } else if (error.code == 429) {
                    // 超出了限流限制
                    ElMessage({
                      message: error.message,
                      type: "warning",
                    });
                  } else if (error.code == 500) {
                    // 后端open api出现问题
                    ElMessage.error(error.message);
                  }
                } else {
                  ElMessage.error(error);
                }
              }
            };

            // 处理连接关闭事件
            socket.onclose = () => {
              this.set_Socket(null);
              this.isGenerating = false;
              this.isWaiting = false;
              console.log("WebSocket连接已关闭");
            };

            // 处理连接错误事件
            socket.onerror = (event) => {
              this.isGenerating = false;
              this.isWaiting = false;
              this.set_Socket(null);
              // ElMessage.error("网络连接出错，请重试");
              console.log("WebSocket连接错误：", event);
              try {
                this.socket.close();
              } catch (e) {}
            };
          } else {
            resolve();
          }
        } catch (error) {
          errorHandler(error);
        }
      });
    },
  },
};
