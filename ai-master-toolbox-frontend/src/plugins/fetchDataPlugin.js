// fetchDataPlugin.js
import { ElMessage } from "element-plus";
import { getUser, getAllUserList } from "@/api/userApi";
import * as chatApi from "@/api/chatApi";
import { getUserCount, getNewUserCount } from "@/api/statisticsApi";

export default {
  install: (app, options) => {
    const cachedData = {};
    app.config.globalProperties.$fetchData = {
      async fetchUser(foreceUpdate = true) {
        if (!foreceUpdate && cachedData["user"]) {
          return;
        }
        try {
          const res = await getUser(0 /*获取自己的用户详情*/);
          options.store.commit("set_user", res);
          cachedData["user"] = res;
        } catch (error) {
          if (!error) {
            return;
          }
          ElMessage({
            message: error.error,
            type: "warning",
          });
        }
      },
      async fetchAllUserList(foreceUpdate = true) {
        if (!foreceUpdate && cachedData["allUserList"]) {
          return;
        }
        try {
          const res = await getAllUserList();
          options.store.commit("set_allUserList", res);
          cachedData["allUserList"] = res;
        } catch (error) {
          if (!error) {
            return;
          }
          ElMessage({
            message: error.error,
            type: "warning",
          });
        }
      },

      async fetchConversationList(foreceUpdate = true) {
        if (!foreceUpdate && cachedData["conversationList"]) {
          return;
        }
        try {
          const res = await chatApi.getConversationList();
          options.store.commit("set_conversationList", res);
          cachedData["conversationList"] = res;
        } catch (error) {
          if (!error) {
            return;
          }
          ElMessage({
            message: error.error,
            type: "warning",
          });
        }
      },
      async fetchAll(foreceUpdate = true) {
        await this.fetchUser(foreceUpdate);
      },
      clear() {
        for (let key in cachedData) {
          delete cachedData[key];
        }
      },
    };
  },
};
