<template>
  <el-scrollbar class="tab">
    <!-- 反馈表格 -->
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>用户名</th>
          <th>反馈信息</th>
          <th>时间</th>
          <th>
            <el-select
              v-model="value"
              class="m-2"
              placeholder="Select"
              size="small"
            >
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="feedback in feedbacks" :key="feedback.id">
          <td>{{ feedback.id }}</td>
          <td>{{ feedback.username }}</td>
          <td class="feedback-info">{{ feedback.message }}</td>
          <td>{{ feedback.time }}</td>
          <td>{{}}</td>
          <td>
            <button @click="showDetails(feedback.id,pk)">详情</button>
          </td>
        </tr>
      </tbody>
    </table>
  </el-scrollbar>
</template>

<script>
import FeedbackJs from "./Feedback";
import deviceMixin from "@/mixins/deviceMixin.js";
export default {
  mixins: [FeedbackJs,deviceMixin],
  data() {
    return {
      pk:1
    };
  },
};
</script>

<style lang="less" scoped>
.tab {
  height: 100vh; /* 设置容器高度为视口高度的100% */
  overflow: auto; /* 当内容溢出容器时显示滚动条 */
}
table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  /* 字体样式 */
  font-family: "Arial", sans-serif;
  font-size: 14px;
  font-weight: bold;
  color: #333;

  /* 文本对齐方式 */
  text-align: center;

  /* 内边距 */
  padding: 8px;
}
th {
  /* 背景颜色 */
  background-color: #f2f2f2;
}
thead th {
  background-color: #f2f2f2;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}
/* 行间隔颜色 */
tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}
.feedback-info {
  max-width: 50px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
button {
  padding: 8px 16px;
  background-color: skyblue;
  border: none;
  border-radius: 4px;
  color: #333;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #ccc;
}
</style>
