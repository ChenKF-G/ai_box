export default {
  name: "FeedbackDetails",
  methods: {
    banked(pk) {
      if(pk==1) {
        this.$router.push({
          name: "FeedbacksDesk",
        });
      } else {
        this.$router.push({
          name: "FeedbacksMoblie",
        });
      }
    },
  },
};
