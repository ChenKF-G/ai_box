# AI 大师工具箱 (AI Master Toolbox) 🛠️

## 📖 项目简介

**AI 大师工具箱** 是一个全栈 AI 工具平台，提供智能 AI 对话（ChatGPT）和 AI 证件照生成等核心功能。项目采用前后端分离架构，支持桌面端和移动端自适应布局。

### 🌟 核心功能

| 功能模块 | 描述 |
|---------|------|
| **💬 AI 智能对话** | 集成 OpenAI GPT-3.5/4 API，支持流式实时对话、对话历史管理、自动标题生成、对话重新生成 |
| **📸 AI 证件照生成** | 基于 AI 抠图技术（rembg）实现照片背景替换，支持红色/蓝色/白色背景，一寸/二寸尺寸，带水印保护 |
| **👤 用户系统** | 邮箱注册/登录、JWT 认证、密码找回、用户等级和资产体系 |
| **📊 数据统计** | 用户总量统计、每日新增/活跃用户统计、ChatGPT Token 消耗统计、API 调用统计 |
| **🔧 管理后台** | 用户管理、数据大屏、订单管理、反馈处理 |
| **📝 API 日志** | 中间件自动记录所有 API 调用日志，支持按 API 和时间维度查询 |

---

## 🏗️ 技术栈

### 后端 (Backend)

| 技术 | 用途 |
|------|------|
| **Python 3.10+** | 开发语言 |
| **Django 4.2.4** | Web 框架 |
| **Django REST Framework 3.14** | RESTful API |
| **Channels / Daphne** | WebSocket 支持（流式对话） |
| **SimpleJWT** | JWT 认证 |
| **MySQL 8** | 关系型数据库 |
| **Redis** | 缓存和限流 |
| **Celery / RabbitMQ** | 异步任务队列 |
| **OpenAI Python SDK** | OpenAI API 集成 |
| **rembg** | AI 背景去除 |
| **Pillow** | 图像处理 |
| **drf-yasg** | API 文档生成 |
| **Django Filter** | 查询过滤 |
| **Twisted** | 异步网络引擎 |

### 前端 (Frontend)

| 技术 | 用途 |
|------|------|
| **Vue 3** | 前端框架 |
| **Vue Router 4** | 前端路由 |
| **Vuex 4** | 状态管理 |
| **Element Plus** | UI 组件库 |
| **Axios** | HTTP 请求 |
| **ECharts** | 数据可视化图表 |
| **highlight.js** | 代码高亮 |
| **markdown-it** | Markdown 渲染 |
| **NProgress** | 进度条 |
| **Less** | CSS 预处理器 |

---

## 📁 项目结构

```
ai-master-toolbox/
├── ai-master-toolbox-backend/          # 后端项目（Django）
│   ├── ai_master_toolbox/              # 主项目配置
│   │   ├── settings_common.py          #   通用配置
│   │   ├── settings_debug.py           #   开发环境配置
│   │   ├── settings_production.py      #   生产环境配置
│   │   ├── urls.py                     #   主路由
│   │   ├── asgi.py / wsgi.py           #   ASGI/WSGI 入口
│   │   └── routing.py                  #   WebSocket 路由
│   ├── chatgpt/                        # AI 对话模块
│   │   ├── models.py                   #   对话/聊天内容模型
│   │   ├── views/
│   │   │   ├── conversation_view.py    #   对话 CRUD
│   │   │   ├── chat_content_view.py    #   聊天内容 + OpenAI 调用
│   │   │   ├── chat_websocket.py       #   WebSocket 流式对话
│   │   │   ├── chat_websocket_util.py  #   WebSocket 工具函数
│   │   │   └── chat_errors.py          #   自定义异常
│   │   ├── serializers.py              #   序列化器
│   │   ├── chatgpt_throttling.py       #   自定义限流
│   │   └── urls.py                     #   路由
│   ├── ai_pic/                         # AI 图片处理模块
│   │   ├── models.py                   #   照片 URL 模型
│   │   ├── views/photo_view.py         #   照片背景替换 + 水印
│   │   ├── permissions.py              #   权限控制
│   │   └── urls.py                     #   路由
│   ├── users/                          # 用户模块
│   │   ├── models.py                   #   用户/资产/反馈模型
│   │   ├── views/
│   │   │   ├── login_view.py           #   登录（JWT）
│   │   │   ├── register_view.py        #   注册（邮箱验证码）
│   │   │   ├── logout_view.py          #   退出
│   │   │   ├── modifyuser_view.py      #   修改密码/信息
│   │   │   ├── user_view.py            #   用户详情/列表
│   │   │   ├── user_assets_view.py     #   用户资产
│   │   │   └── feedback_view.py        #   反馈管理
│   │   └── urls.py
│   ├── api_log/                        # API 日志模块
│   │   ├── api_log_middleware.py       #   日志中间件
│   │   ├── models.py
│   │   ├── views.py                    #   API 使用统计
│   │   └── urls.py
│   ├── data_statistics/                # 数据统计模块
│   │   ├── views/
│   │   │   ├── user_statistics_view.py #   用户统计
│   │   │   └── chatgpt_statistics_view.py  # Token 统计
│   │   └── urls.py
│   ├── utils/                          # 工具类
│   │   ├── cache_util.py               #   缓存工具
│   │   └── utils.py                    #   通用工具（IP、Token计数）
│   ├── config.py                       # ChatGPT 配置常量
│   ├── docker-compose.yml              # Docker 编排
│   ├── docker/                         # Dockerfile
│   └── requirements.txt                # Python 依赖
│
├── ai-master-toolbox-frontend/         # 前端项目（Vue 3）
│   ├── src/
│   │   ├── main.js                     #   入口
│   │   ├── App.vue                     #   根组件
│   │   ├── router/                     #   路由配置
│   │   │   ├── index.js                #     路由聚合
│   │   │   ├── homeRouter.js           #     首页路由
│   │   │   ├── gptRouter.js            #     AI对话路由
│   │   │   ├── idPhotoRouter.js        #     证件照路由
│   │   │   ├── loginRouter.js          #     登录注册路由
│   │   │   ├── adminRouter.js          #     管理后台路由
│   │   │   └── userCenterRouter.js     #     个人中心路由
│   │   ├── store/index.js              #   Vuex 状态管理
│   │   ├── views/                      #   页面组件
│   │   │   ├── home/                   #     首页（桌面/移动端）
│   │   │   ├── gpt/                    #     AI对话页面
│   │   │   ├── idPhoto/                #     证件照页面
│   │   │   ├── login/                  #     登录注册页面
│   │   │   ├── admin/                  #     管理后台页面
│   │   │   └── user/                   #     个人中心页面
│   │   ├── components/                 #   组件
│   │   │   ├── gpt/                    #     AI对话组件
│   │   │   │   ├── ChatContentComponent.vue   # 聊天内容区
│   │   │   │   ├── LeftListComponent.vue      # 对话列表
│   │   │   │   ├── ChatContentMixin.js        # 聊天逻辑混入
│   │   │   │   └── markdownInterpreter.js     # Markdown渲染
│   │   │   ├── idphoto/                #     证件照组件
│   │   │   │   ├── Mobile/
│   │   │   │   │   ├── SelectPhotoViewMobile.vue   # 选择照片
│   │   │   │   │   ├── DownloadPhotoViewMobile.vue # 预览下载
│   │   │   │   │   └── TakePhotoViewMobile.vue     # 拍照
│   │   │   │   └── Desk/
│   │   │   ├── home/                   #     首页组件
│   │   │   ├── adminview/              #     管理后台组件
│   │   │   └── userView/               #     个人中心组件
│   │   ├── api/                        #   API 请求封装
│   │   │   ├── request.js              #     Axios 实例（拦截器）
│   │   │   ├── chatApi.js              #     对话 API
│   │   │   ├── picApi.js               #     图片 API
│   │   │   ├── userApi.js              #     用户 API
│   │   │   └── statisticsApi.js        #     统计 API
│   │   ├── plugins/fetchDataPlugin.js  #   数据获取插件
│   │   ├── mixins/deviceMixin.js       #   设备类型混入
│   │   ├── util/utilFunctions.js       #   工具函数
│   │   └── config.json                 #   环境配置（URL、WS）
│   ├── vue.config.js                   #   Vue CLI 配置
│   └── package.json                    #   前端依赖
```

---

## 🚀 快速开始

### 环境要求

- Python 3.10+
- Node.js 16+
- MySQL 8.0+
- Redis

### 后端启动

```bash
# 1. 进入后端目录
cd ai-master-toolbox-backend

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 数据库迁移
python manage.py migrate

# 5. 创建超级管理员（可选）
python manage.py createsuperuser

# 6. 启动开发服务器
python manage.py runserver 0.0.0.0:8000
```

### 前端启动

```bash
# 1. 进入前端目录
cd ai-master-toolbox-frontend

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run serve

# 4. 构建生产包
npm run build
```

### Docker 部署

```bash
cd ai-master-toolbox-backend
docker-compose up -d
```

---

## 🧩 API 接口概览

所有 API 均以 `/api/` 为前缀，需要 JWT Token 认证（除登录/注册外）。

### 用户模块 (`/api/user/`)

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/user/login/` | 用户登录（返回 JWT Token） |
| POST | `/api/user/verify_code/` | 获取邮箱验证码 |
| POST | `/api/user/register/` | 用户注册 |
| PUT | `/api/user/modify_password/` | 修改密码 |
| GET/PUT | `/api/user/<id>/` | 用户详情/修改 |
| GET | `/api/user/<id>/asset/` | 用户资产详情 |
| GET/POST | `/api/user/feedback/` | 反馈列表/创建 |
| PUT/DELETE | `/api/user/feedback/<id>/` | 修改/删除反馈 |
| GET/POST | `/api/user/feedback/<id>/reply/` | 反馈回复 |

### AI 对话 (`/api/chat/`)

| 方法 | 路径 | 说明 |
|------|------|------|
| GET/POST | `/api/chat/conv/` | 会话列表/新建会话 |
| PUT/DELETE | `/api/chat/conv/<id>/` | 修改/删除会话 |
| GET/POST | `/api/chat/conv/<id>/chat_cont/` | 聊天内容列表/发送消息 |
| POST | `/api/chat/conv/<id>/chat_resp/` | 获取 AI 回复 |
| POST | `/api/chat/conv/<id>/chat_title/` | AI 自动生成标题 |
| WebSocket | `ws://host/ws/chat_socket/` | 流式实时对话 |

### 证件照 (`/api/ai_pic/`)

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/ai_pic/id_photo/` | 上传照片并处理（换背景+水印） |
| GET | `/api/ai_pic/id_photo/` | 下载处理后的高清照片 |

### 数据统计 (`/api/statistics/`)

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/statistics/user/total/` | 用户总数 |
| GET | `/api/statistics/user/new_pd/` | 每日新增用户 |
| GET | `/api/statistics/user/active_pd/` | 每日活跃用户 |
| GET | `/api/statistics/chat/token_pd/` | Token 消耗统计 |

### 日志管理 (`/api/log/`)

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/log/apis/` | API 调用排行 |
| GET | `/api/log/api_usage/` | API 每日使用统计 |

### 其他

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/token/` | 获取 JWT Token |
| POST | `/api/token/refresh/` | 刷新 JWT Token |
| GET | `/api/docs/` | API 文档（drf-yasg） |
|    | `/api/admin/` | Django Admin 后台 |

---

## 🔐 权限与限流

### 用户等级
- **普通用户 (level 0)** — 默认，免费使用次数有限
- **付费用户** — 会员期限内无限使用
- **超级管理员** — 无限制

### 限流规则
| 限制项 | 限制值 |
|--------|--------|
| 每日免费 AI 对话次数 | 5 次 |
| 每小时 AI 对话上限 | 30 次 |
| 每日 AI 对话上限 | 200 次 |
| 匿名用户 API 限流 | 10 次/分钟 |
| 认证用户 API 限流 | 30 次/分钟 |

### AI 对话计费
| 套餐 | 价格 |
|------|------|
| 月卡 | ¥4.9 |
| 季卡 | ¥12.9 |
| 年卡 | ¥40.9 |

---

## 🔄 核心业务流程

### AI 对话流程
```
用户输入消息 → 保存到 ChatContent → 拼接历史消息（前5+后5条）
  → 调用 OpenAI API → 流式返回（WebSocket）→ 实时展示
  → 完成后保存助手回复 → 自动生成对话标题
```

### 证件照处理流程
```
用户上传照片 → 选择颜色（红/蓝/白）+ 尺寸（1寸/2寸）
  → rembg 去除背景 → 替换背景色 → 调整尺寸
  → 添加水印 → 返回水印预览图 → 付费下载高清原图
```

---

## ⚙️ 环境配置

### 后端环境变量
| 变量 | 说明 |
|------|------|
| `DEBUG` | 调试模式（True/False） |
| `dbuser` | 数据库用户名 |
| `dbpassword` | 数据库密码 |
| `prject_media` | 媒体文件存储路径 |
| `prject_logs` | 日志文件存储路径 |

### 配置文件位置
- 通用配置：`settings_common.py`
- 开发配置：`settings_debug.py`（本地 MySQL + Redis）
- 生产配置：`settings_production.py`（Docker 容器化）

### 前端配置
- 后端地址和 WebSocket 地址：`src/config.json`
- API 代理（开发环境）：`vue.config.js` 中 `/api` 代理到 `http://127.0.0.1:8000/api/`

---

## 📝 开发说明

### 桌面端/移动端适配
项目通过 `deviceMixin.js` 检测设备宽度（阈值 680px），自动切换"desk"和"mobile"路由视图，为不同设备提供最佳体验。

### WebSocket 通信协议
```json
// 认证
{"eventType": "auth", "user_id": 1, "token": "xxx"}

// 发送消息
{"eventType": "send_message", "content": "你好", "conversation_id": 1}

// 重新生成
{"eventType": "re_generate", "conversation_id": 1}

// 服务端响应（流式）
{"eventType": "response_message", "content": "你好！", "conversation_id": 1, "role": "assistant"}

// 响应结束
{"eventType": "response_finished"}
```

### 水印保护
证件照预览图会自动添加"AI大师工具箱"文字水印，用户需付费后通过 GET 请求下载无水印高清原图。
