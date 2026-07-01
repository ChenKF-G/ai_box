import request from "@/api/request";

export function getUserCount() {
  return request({
    method: "GET", 
    url: "statistics/user/total/",
  });
}

export function getNewUserCount() {
  return request({
    method: "GET",
    url: "statistics/user/new_pd/",
  });
}

export function getActiveUserCount() {
  return request({
    method: "GET",
    url: "statistics/user/active_pd/",
  });
}

export function getGptCostCount() {
  return request({
    method: "GET",
    url: "statistics/chat/token_pd/",
  });
}

