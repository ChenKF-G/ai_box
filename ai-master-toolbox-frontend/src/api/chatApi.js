import request from "@/api/request";
//发送消息
export function sendMsg(id, data) {
  return request({
    method: "POST",
    url: "/chat/conv/" + id + "/chat_cont/",
    data,
  });
}
//获取历史聊天集合
export function getConversationList() {
  return request({
    method: "GET",
    url: "/chat/conv/",
  });
}
//新增聊天
export function newChart() {
  return request({
    method: "POST",
    url: "/chat/conv/",
  });
}
//请求历史消息详情
export function getMsgDetil(id) {
  return request({
    method: "GET",
    url: "/chat/conv/" + id + "/chat_cont/",
  });
}
//修改聊天
export function updatedMsg(id, data) {
  return request({
    method: "PUT",
    url: "/chat/conv/" + id + "/",
    data,
  });
}
//删除聊天
export function deleteMsg(id) {
  return request({
    method: "DELETE",
    url: "/chat/conv/" + id + "/",
  });
}

