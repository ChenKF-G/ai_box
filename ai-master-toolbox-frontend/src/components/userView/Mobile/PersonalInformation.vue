<template>
  <div class="Recharge">
    <div class="PersonalInformations">
      <div class="PersonalInformation">
        <p>我的邮箱：</p>
        <!-- <span>{{ this.user.email }}</span> -->
        <span>2333333333</span>
      </div>
      <div class="PersonalInformation">
        <p>我的电话：</p>
        <span>15845692351</span>
      </div>
      <div class="PersonalInformation">
        <p>登录密码：</p>
        <span>
          <el-input
            type="papassword"
            v-model="input"
            show-password
            placeholder="Please input"
            disabled
            style="width: 150px"
          />
        </span>
        <el-button
          text
          @click="open"
          style="margin-left: 20px; background: #f0f4f4"
        >
          修改密码
        </el-button>
      </div>
    </div>
  </div>
</template>


<script >
import { mapState } from "vuex";
import Cookies from "js-cookie";
import { ElMessage, ElMessageBox } from "element-plus";

export default {
  created() {
    // 如果token存在则取获取user数据
    if (Cookies.get("token")) {
      this.$fetchData.fetchUser(false);
    }
  },
  data() {
    return {
      radio: 6,
      demand: "",
      description: "",
      activeName: "first",
      input: "11111",
    };
  },

  computed: {
    ...mapState(["user"]),
  },

  methods: {
    open() {
      ElMessageBox.prompt("请输入您的旧密码", "修改密码", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          if (value === "1111") {
            setTimeout(() => {
              ElMessageBox.prompt("请输入您的新密码", "修改密码", {
                confirmButtonText: "确认",
                cancelButtonText: "取消",
              })
                .then(({ value }) => {
                  console.log(value);
                  if (value != null) {
                    value = value.replaceAll(" ", "");
                    this.input = value;
                    ElMessage({
                      type: "success",
                      message: "您的密码已经更新 请查看",
                    });
                  } else {
                    ElMessage({
                      type: "info",
                      message: "请输入合法的密码",
                    });
                  }
                })
                .catch(() => {
                  ElMessage({
                    type: "info",
                    message: "您已取消密码更新",
                  });
                });
            }, 1000);
          } else {
            ElMessage({
              type: "info",
              message: "密码输入错误请重新输入",
            });
            setTimeout(() => {
              this.open();
            }, 1000);
          }
        })
        .catch(() => {
          ElMessage({
            type: "info",
            message: "您已取消密码更新",
          });
        });
    },
  },
};
</script>


<style lang="less" scoped>
.Recharge {
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  .PersonalInformations {
    font-size: 18px;
    margin: 0 20px;
    .PersonalInformation {
      margin: 30px 0;
      p {
        font-weight: 600;
        margin-bottom: 10px;
      }
    }
  }
}
</style>