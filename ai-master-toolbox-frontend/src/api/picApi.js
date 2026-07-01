import request from "@/api/request";

export function changephotobackground(formData) {
  return request({
    method: "POST",
    url: "ai_pic/id_photo/",
    data: formData,
    contentType: "multipart/form-data",
  });
}

export function downloadphoto() {
  return request({
    method: "Get",
    url: "ai_pic/id_photo/",
    responseType: "blob",
  });
}
