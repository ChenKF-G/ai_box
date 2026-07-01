<template>
  <div class="bank">
    <button class="btu" @click="banked">←</button>
    <span class="user">用户{{ getuserdetails.username }}的详情页面</span>
  </div>
  <div class="boxs tableDate">
    <!-- 信息展示 -->
    <div class="divs">
      <span>ID：{{ getuserdetails.id }}</span>
    </div>
    <!-- 姓名 -->
    <div class="divs">
      <span>用户名：{{ getuserdetails.username }}</span>
    </div>
    <!-- 邮箱 -->
    <div class="divs">
      <span>邮箱：{{ getuserdetails.email }}</span>
    </div>
    <!-- 手机号 -->
    <div class="divs">
      <span>手机号：{{ getuserdetails.phone }} </span>
    </div>
    <div class="divs">
      <span>创建时间：{{ getuserdetails.date_joined }}</span>
    </div>
    <div class="divs"   v-if="userAssets">
      <span v-if="userAssets">余额：{{ userAssets.balance }}</span>
      <!-- <span v-else="userAssets">余额：</span> -->
    </div>
    <div class="divs"   v-if="userAssets">
      <span v-if="userAssets"
        >剩余次数：{{ userAssets.chatgpt_left_count }}</span
      >
      <!-- <span v-else="userAssets">剩余次数：</span> -->
    </div>
    <div class="divs"   v-if="userAssets">
      <span v-if="userAssets">到期时间：</span>
      <!-- <span v-else="userAssets">到期时间：</span> -->
      <span v-if="userAssets"
        ><el-input
          @blur="timesting"
          style="width: 200px; margin-left: 10px"
          placeholder="null"
          v-model="userAssets.chatgpt_expired_time"
          :disabled="true"
      /></span>
      <span   v-if="userAssets">
        <el-button
          style="margin-left: 2%; border: 1px solid skyblue"
          @click="Modifyadminemail"
          id="myButton"
        >
          修改
        </el-button>
      </span>
    </div>
    <div class="divs"   v-if="userAssets">
      <span v-if="userAssets">邀请码：{{ userAssets.invite_code }}</span>
      <!-- <span v-else="userAssets">邀请码：</span> -->
    </div>
  </div>
  <!-- 修改过期时间窗口 -->
  <div style="height: 40px">
    <el-dialog v-model="bool" width="90%" center>
      <div class="container">
        <div class="box" style="text-align: center">设置过期时间</div>
        <div style="text-align: center">
          <el-date-picker
            v-model="selectedDate"
            type="date"
            placeholder="选择日期"
            style="width: 45%"
          ></el-date-picker>
        </div>
        <div style="text-align: center">
          <el-time-picker
            v-model="selectedTime"
            type="fixed-time"
            placeholder="选择时间"
            style="width: 45%; margin-top: 5%"
          ></el-time-picker>
        </div>
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button
            class="adds"
            style="background-color: rgba(64, 149, 229, 1); margin-top: 5px"
            @click="modify"
          >
            修改
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import UserDetailsJs from "./UserDetailsJs";
import deviceMixin from "@/mixins/deviceMixin.js";
export default {
  mixins: [UserDetailsJs, deviceMixin],
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped>
.boxs {
  margin-top: 5%;
  height: 520px;
  width: 100%;
  background-color: rgb(255, 255, 255);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  margin-left: 1%;
  //   max-height: 450px;
}
.but {
  margin-right: -100px;
  margin-top: -40px;
}
.center {
  margin-left: 50px;
  margin-top: 50px;
}
.box {
  margin-top: 20px;
  margin-bottom: 10px;
  margin-left: -1%;
}
/* 表格美化 */
.table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 10px;
}
.divs {
  margin-left: 2%;
  margin-top: 1%;
  padding-top: 20px;
}
.bank {
  margin-left: 1%;
  margin-top: 5px;
}
.user {
  margin-left: 15.5%;
}
.btu {
  width: 5%;
  height: 2%;
  font-size: 30px;
  border-radius: 15px;
  border: 0px solid rgb(106, 146, 188);
}
</style>
