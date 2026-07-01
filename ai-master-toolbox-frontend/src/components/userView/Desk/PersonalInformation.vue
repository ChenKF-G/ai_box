<template>
  <div class="Recharge" v-if="user">
    <div>
      <div class="headline">
        <p>个人信息</p>
      </div>
      <div class="box PersonalInformations">
        <div class="PersonalInformation">
          <p>我的邮箱：</p>
          <span>{{ this.user.email }}</span>
        </div>
        <div class="PersonalInformation">
          <p>我的电话：</p>
          <span>{{ user.phone }}</span>
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
      input: "1111",
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
.box {
  float: left;
  width: 80%;
  min-width: 400px;
  .PersonalInformations {
    margin: 0 20px 20px 20px;
    .PersonalInformation {
      margin: 20px 0;
      p {
        height: 30px;
        line-height: 30px;
        font-weight: 800;
        margin-bottom: 5px;
      }
      span {
        margin: 50px 0;
      }
      .ChangePassword {
        width: 100px;
        height: 30px;
        background: #f0f4f6;
        margin-left: 20px;
        border: #f0f4f6;
        border-radius: 5px;
        cursor: pointer;
      }

      .logoutBox {
        display: flex;
        width: 80%;
        min-width: 550px;
        height: 60px;
        padding: 10px;
        border: 2px solid #f0f4f6;
        border-radius: 5px;
        p {
          font-weight: normal;
        }
        .logoutBut {
          width: 80px;
          height: 30px;
          background: #f0f4f4;
          border: none;
          border-radius: 5px;
          margin: auto 20px;
          cursor: pointer;
        }
      }
    }
  }
}
.Recharge {
  box-sizing: border-box;
  margin: 0 20%;
  width: 60%;
  min-width: 550px;
  height: 500px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  overflow: auto;
  .headline {
    display: flex;
    justify-content: space-between;
    height: 70px;
    line-height: 70px;
    border-bottom: 1px solid #ccc;
    padding: 0 20px 0 10px;
    font-size: 20px;
    font-weight: 700;
    .el-button {
      margin: auto 0;
      cursor: pointer;
      font-size: 25px;
    }
  }
}
.Recharge::-webkit-scrollbar {
  display: none;
}
</style>
