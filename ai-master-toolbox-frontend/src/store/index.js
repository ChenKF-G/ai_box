import { createStore } from "vuex";

export default createStore({
  state: {
    user: null,
    allUserList: null,
    userCount: null,
    newusercount: null,
    conversationList: [], //当前对话集合
    gptMessageList: {},
    socket: null,
  },
  getters: {
    GET_ISMSG(state) {
      return state.isMsg;
    },
  },
  mutations: {
    set_user(state, user) {
      state.user = user;
    },
    set_allUserList(state, allUserList) {
      state.allUserList = allUserList;
    },
    set_conversationList(state, conversationList) {
      state.conversationList = conversationList;
    },
    set_usercount(state, userCount) {
      state.userCount = userCount;
    },
    set_newusercount(state, newuserCount) {
      state.newuserCount = newuserCount;
    },
    update_MsgTitle(state, msgContent) {
      state.conversationList.forEach((item, index) => {
        if (item.id === msgContent.id) {
          item.title = msgContent.title;
        }
      });
    },
    set_Socket(state, socket) {
      state.socket = socket;
    },
  },
  actions: {},
  modules: {},
});
