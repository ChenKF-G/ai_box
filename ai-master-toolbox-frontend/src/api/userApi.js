import request from "@/api/request";

export function getUser(id) {
  return request({
    method: "GET",
    url: "/user/" + id + "/",
  });
}

export function updataUser(id, data) {
  return request({
    method: "PUT",
    url: "/user/" + id + "/",
    data: data,
  });
}

export function getAllUserList() {
  return request({
    method: "GET",
    url: "/user/",
  });
}

export function getUserAssets(id) {
  return request({
    method: "GET",
    url: "/user/" + id + "/asset/",
  });
}

export function putUserAssets(id, data) {
  return request({
    method: "PUT",
    url: "/user/" + id + "/asset/",
    data: data,
  });
}

export function login(data) {
  return request({
    method: "POST",
    url: "/user/login/",
    data: data,
  });
}

export function logout() {
  return request({
    method: "POST",
    url: "/user/logout/",
  });
}

export function register(data) {
  return request({
    method: "POST",
    url: "/user/register/",
    data: data,
  });
}

export function getVerifyCode(data) {
  return request({
    method: "POST",
    url: "/user/verify_code/",
    data: data,
  });
}

export function resetPassword(data) {
  return request({
    method: "PUT",
    url: "/user/modify_password/",
    data: data,
  });
}

export function getFeedbackList() {
  return request({
    method: "GET",
    url: "/user/feedback/",
  });
}

export function createFeedback(formData) {
  return request({
    method: "POST",
    url: "/user/feedback/",
    data: formData,
    contentType: "multipart/form-data",
  });
}

export function updateFeedback(id) {
  return request({
    method: "PUT",
    url: "/user/feedback/" + id + "/",
    data: {
      handled: handled,
    },
  });
}

export function deleteFeedback(id) {
  return request({
    method: "DELETE",
    url: "/user/feedback/" + id + "/",
  });
}

export function getFeedbackReplyList(feedbackId) {
  return request({
    method: "GET",
    url: "/user/feedback/" + feedbackId + "/reply",
  });
}

export function createFeedbackReply(feedbackId, content) {
  return request({
    method: "POST",
    url: "/user/feedback/" + feedbackId + "/reply/",
    data: {
      content: content,
    },
  });
}

export function updateFeedbackReply(feedbackId, replyId, handled) {
  return request({
    method: "PUT",
    url: "/user/feedback/" + feedbackId + "/reply/" + replyId + "/",
    data: {
      handled: handled,
    },
  });
}

export function deleteFeedbackReply(feedbackId, replyId) {
  return request({
    method: "DELETE",
    url: "/user/feedback/" + feedbackId + "/reply/" + replyId + "/",
  });
}
