<template>
  <div class="chatGpt">
    <transition>
      <LeftListComponent
        v-if="leftListShow"
        :leftListShow="leftListShow"
        @close="switchLeft"
        @selectConversation="handleselectConversation"
        @selectConversationTitle="handleselectConversationTitle"
      ></LeftListComponent>
    </transition>
    <ChatContentComponent
      ref="rightView"
      :leftListShow="leftListShow"
      :conversationId="selectedConversationId"
      :selectConversationTitle="selectConversationTitle"
      @open="switchLeft"
    ></ChatContentComponent>
  </div>
</template>

<script>
import deviceMixin from "@/mixins/deviceMixin.js";
import ChatContentComponent from "@/components/gpt/ChatContentComponent.vue";
import LeftListComponent from "@/components/gpt/LeftListComponent.vue";
export default {
  mixins: [deviceMixin],
  data() {
    return {
      selectedConversationId: null,
      selectConversationTitle: null,
      leftListShow: true,
    };
  },
  
  components: {
    ChatContentComponent,
    LeftListComponent,
  },
  methods: {
    handleselectConversationTitle(title) {
      this.selectConversationTitle = title;
    },
    handleselectConversation(id) {
      this.selectedConversationId = id;
    },
    switchLeft(value) {
      this.leftListShow = value;
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
  max-width: 100%;
  width: 100%;
  display: flex;
  flex-direction: row;
  height: 100%;
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
</style>
