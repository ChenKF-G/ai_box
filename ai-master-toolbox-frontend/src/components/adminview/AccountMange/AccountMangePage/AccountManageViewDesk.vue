<template>
  <!-- 查询功能 -->
  <div class="getuser">
    <div class="gets">
      <span style="margin-right: 8px">姓名</span>
      <el-input
        style="width: 150px; height: 35px"
        v-model="searchname"
        placeholder="name"
        aria-valuetext=""
      ></el-input>
    </div>
    <div class="gets">
      <span style="margin-right: 8px">电话</span>
      <el-input
        style="width: 150px; height: 35px"
        v-model="searchphone"
        placeholder="phone"
        aria-valuetext=""
      ></el-input>
    </div>
    <div class="gets">
      <span style="margin-right: 8px">是否是管理员</span>
      <el-select
        style="width: 230px"
        v-model="selectrole"
        clearable
        placeholder="role"
      >
        <el-option
          v-for="item in schoolnameset"
          :key="item"
          :label="item"
          :value="item"
        />
      </el-select>
    </div>
  </div>
  <!-- 表格 -->
  <div class="tableDate">
    <table class="table">
      <thead>
        <tr>
          <th>id</th>
          <th style="width: 130px">账号</th>
          <th>电话</th>
          <th>角色</th>
          <th>创建时间</th>
          <th>状态</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody v-if="allUserList">
        <tr v-for="item in filteredUsers" :key="item.id">
          <td class="centered">{{ item.id }}</td>
          <td class="centered">{{ item.username }}</td>
          <td class="centered">{{ item.phone }}</td>
          <td class="centered">
            {{ item.is_superuser ? "管理员" : "普通用户" }}
          </td>
          <td class="centered">{{ item.date_joined }}</td>
          <td class="centered">
            <el-switch
              v-model="item.is_active"
              active-text="激活"
              inactive-text="失效"
              inline-prompt="true"
              @change="updateSwitchStatus(item.id, item.is_active)"
            />
          </td>
          <td class="centered">
            <button
              class="delete-button"
              style="margin-left: 5px"
              @click="details(item.id,pk)"
            >
              详情
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import AccountMangeJs from "./AccountMange";
import deviceMixin from "@/mixins/deviceMixin.js";
export default {
  mixins: [AccountMangeJs, deviceMixin],
  data() {
    return {
      pk:1
    };
  },
};
</script>

<style scoped>
.getuser {
  height: 100px;
  margin-top: 10px;
  background-color: rgba(239, 239, 239);
  font-family: "\5b8b\4f53";
}
.gets {
  font-size: 15px;
  display: inline-block;
  margin-left: 2%;
  margin-top: 40px;
}
input {
  height: 25px;
}

.search {
  position: absolute;
  top: 110px;
  z-index: 500;
  border: none;
  width: 70px;
  height: 40px;
}

.showdatas {
  background-color: rgba(239, 239, 239);
  height: 700px;
}

.Form {
  margin-left: 17%;
}

.News {
  width: 1%;
  height: 4%;
  border: none;
  margin-left: 0.3%;
  background-color: rgba(52, 124, 175, 1);
  color: aliceblue;
}

.texts {
  font-size: 20px;
  margin-left: 5%;
}

.tableDate {
  width: 100%;
  margin-left: 1%;
  margin-top: 2%;
  overflow: auto;
  max-height: 450px;
  font-family: "\5b8b\4f53";
}
/* 表格美化 */
.table {
  width: 100%;
  border-collapse: collapse;
  background-color: rgb(220, 218, 218);
  border: 1px solid black;
}

.table th,
.table td {
  border: 1px solid #ccc;
  padding: 8px;
}

.table th {
  background-color: #f2f2f2;
}

.delete-button {
  background-color: #50b1d4;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
}
.table td:first-child,
.table td:last-child {
  width: 100px; /* 根据需要调整宽度 */
}

.centered {
  text-align: center;
  /* border: 1px solid black; */
}

/* 新增管理员 */
.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.box {
  margin-top: 10px;
  margin-bottom: 10px;
}

.input-box {
  margin: 0 auto; /* 设置左右外边距为auto实现水平居中 */
}

.table td:last-child {
  width: 150px; /* 根据需要调整宽度 */
}
</style>
