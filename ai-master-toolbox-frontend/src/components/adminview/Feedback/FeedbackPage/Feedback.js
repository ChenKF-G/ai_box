export default {
  name: "Feedback",

  data() {
    return {
      feedbacks: [
        {
          id: "1",
          username: "",
          message:
            "这是一条反馈信息这是一条反馈信息这是一条反馈信息这是一条反馈信息这是一条反馈信息这是一条反馈信息这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message:
            "这是一条反馈信息这是一条反馈信息这是一条反馈信息这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息这是一条反馈信息这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
        {
          id: "1",
          username: "",
          message: "这是一条反馈信息",
          time: "2023-10-08 13:15:00",
        },
      ],
      value: "option1",
      // 下拉框选项
      options: [
        { value: "option1", label: "所有" },
        { value: "option2", label: "未读" },
        { value: "option3", label: "已读" },
      ],
    };
  },
  methods: {
    showDetails(id,pk) {
      console.log(id);
      if(pk==1) {
        this.$router.push({
          name: "FeedbackDetailsDesk",
          params: { id: id },
        });
      } else {
        this.$router.push({
          name: "FeedbackDetailsMoblie",
          params: { id: id },
        });
      }
    },
  },
};
