import { mapState } from "vuex";
import { updataUser } from "@/api/userApi";
import { ElMessageBox } from "element-plus";

export default {
  async created() {
    this.$fetchData.fetchAllUserList(false);
  },
  data() {
    return {
      schoolnameset: [true, false],
      searchphone: "",
      searchname: "",
      selectrole: "",
    };
  },
  computed: {
    ...mapState(["user", "allUserList"]),

    filteredUsers() {
      return this.allUserList.filter((item) => {
        // 根据筛选条件过滤数据
        if (
          this.searchname !== "" &&
          (item.username === null || !item.username.includes(this.searchname))
        ) {
          return false; // 不符合姓名筛选条件的数据将被过滤掉
        }
        if (
          this.searchphone !== "" &&
          (item.phone === null || !item.phone.includes(this.searchphone))
        ) {
          return false; // 不符合手机号筛选条件的数据将被过滤掉
        }
        if (this.selectrole !== "" && item.is_superuser !== this.selectrole) {
          return false; // 不符合角色筛选条件的数据将被过滤掉
        }

        return true; // 其他情况均保留数据
      });
    },
  },
  methods: {
    // CrestUser() {
    //   console.log(this.Userlist);
    // },
    // 编辑
    modifyadminshow() {},
    // 详情跳转
    details(id, pk) {
      console.log(id);
      if (pk == 1) {
        this.$router.push({
          name: "UserDetailsDesk",
          params: { id: id },
        });
      } else {
        this.$router.push({
          name: "UserDetailsMoblie",
          params: { id: id },
        });
      }
    },
    // 状态修改
    updateSwitchStatus(id, is_active) {
      const data = {
        is_active: is_active,
      };
      updataUser(id, data)
        .then(() => {
          // 更新成功的处理逻辑
          ElMessageBox.alert("修改成功", "提示", {
            confirmButtonText: "确定",
            type: "success",
            showClose: false,
            
          });
        })
        .catch((error) => {
          // 更新失败的处理逻辑
          if (error) {
            error = error.error;
          }
          ElMessageBox.alert("修改失败, " + error, "错误提示", {
            confirmButtonText: "确定",
            type: "error",
            showClose: false,
          }).catch((error) => {
            console.error(error);
          });
        });
    },
  },
};
