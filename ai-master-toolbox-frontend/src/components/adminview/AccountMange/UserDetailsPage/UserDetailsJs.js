import { mapState } from "vuex";
import axios from "axios";
import { putUserAssets, getUserAssets } from "@/api/userApi";
import { ElMessageBox } from "element-plus";
import { ElMessage } from "element-plus";

export default {
  name: "Userdetails",
  data() {
    return {
      userAssets: null,
      bool: false,
      selectedDate: new Date(2022, 0, 1, 12, 0, 0),
      selectedTime: new Date(0, 0, 0),
      userbody: null,
    };
  },
  // 在组件挂载时调用fetchData方法来获取资产数据
  mounted() {
    this.fetchUserAssetData();
  },
  computed: {
    ...mapState(["user", "allUserList"]),

    // 获取到当前用户信息
    getuserdetails() {
      const user = this.allUserList?.find((t) => t.id == this.$route.params.id);
      return user ?? {};
    },
  },

  methods: {
    banked() {
      this.$router.push("../AccountManages/AccountManage");
    },

    fetchUserAssetData() {
      const id = this.$route.params.id;
      const user = this.allUserList?.find((t) => t.id == id);
      if (user.is_superuser) {
        this.userbody = "系统管理员";
      } else {
        this.userbody = "普通用户";
        getUserAssets(id)
          .then((response) => {
            this.userAssets = response;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },

    // 窗口显示
    Modifyadminemail() {
      this.bool = true;
    },
    // 修改
    modify() {
      const date =
        this.selectedDate.getFullYear() +
        "-" +
        (this.selectedDate.getMonth() + 1).toString().padStart(2, "0") +
        "-" +
        this.selectedDate.getDate().toString().padStart(2, "0");
      const time =
        this.selectedTime.getHours().toString().padStart(2, "0") +
        ":" +
        this.selectedTime.getMinutes().toString().padStart(2, "0") +
        ":" +
        this.selectedTime.getSeconds().toString().padStart(2, "0");
      console.log(date + " " + time);
      const datetime = date + " " + time;

      // 调API修改
      putUserAssets(this.$route.params.id, {
        chatgpt_expired_time: datetime,
      })
        .then(() => {
          // 添加成功的处理逻辑
          ElMessageBox.alert("修改成功", "提示", {
            confirmButtonText: "确定",
            type: "success",
            showClose: false,
          });
          this.fetchUserAssetData();
        })
        .catch((error) => {
          if (error) {
            ElMessage({
              message: error.error,
              type: "warning",
            });
          }
        });

      this.bool = false;
    },
  },
};
