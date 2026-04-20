# Pywebview-Vue-FastAPI

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.120+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vue](https://img.shields.io/badge/Vue.js-3.5+-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9+-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.1+-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**🖥️ 使用现代 Web 技术栈构建桌面应用的完美起点**

[快速开始](#快速开始) · [项目结构](#项目结构) · [开发指南](#开发指南) · [构建部署](#构建部署)

</div>

---

## ✨ 特性

- 🚀 **FastAPI** - 高性能异步 Python 后端，自动生成 API 文档
- ⚡ **Vue 3 + Vite** - 极速开发体验，Composition API 支持
- 🎨 **Tailwind CSS + Shadcn UI** - 现代化原子化 CSS 与精美组件库
- 🖥️ **Pywebview** - 将 Web 应用打包为原生桌面应用
- 📦 **uv** - 极速 Python 包管理与虚拟环境
- 🔥 **热重载** - 开发模式支持前后端实时刷新
- 🧩 **自动路由注册** - 后端 API 路由自动发现与注册

---

## 📁 项目结构

```
Pywebview-Vue-FastAPI/
├── 📂 app/                          # FastAPI 后端 + Pywebview 桌面端
│   ├── 📄 main.py                   # 桌面端入口：启动 uvicorn + webview
│   ├── 📄 app.py                    # FastAPI 应用、静态资源挂载、路由自动注册
│   ├── 📂 routers/                  # API 路由模块（自动注册）
│   │   └── 📄 test.py               # 示例路由
│   ├── 📂 static/                   # 前端构建产物（index.html + assets）
│   ├── 📂 desktop/                  # 桌面端适配代码
│   ├── 📄 pyproject.toml            # Python 依赖配置
│   └── 📄 uv.lock                   # 锁定依赖版本
│
├── 📂 web/                          # Vue 3 + Vite + Tailwind 前端源码
│   ├── 📂 src/
│   │   ├── 📄 main.ts               # 前端入口
│   │   ├── 📄 App.vue               # 根组件
│   │   ├── 📂 router/               # Vue Router 路由配置
│   │   ├── 📂 stores/               # Pinia 状态管理
│   │   ├── 📂 views/                # 页面组件
│   │   ├── 📂 components/           # 通用组件（含 Shadcn UI）
│   │   └── 📂 assets/               # 静态资源
│   ├── 📄 package.json              # Node.js 依赖
│   └── 📄 vite.config.ts            # Vite 配置
│
├── 📂 webdist/                      # 前端构建产物（供静态模式加载，构建后需手动移动为app/static/）
├── 📂 tests/                        # 后端测试
│   └── 📄 test.py
└── 📄 README.md                     # 本文件
```

---

## 🚀 快速开始

### 环境要求

- **Python** >= 3.12
- **Node.js** ^20.19.0 || >=22.12.0
- **uv** - Python 包管理器 ([安装指南](https://docs.astral.sh/uv/getting-started/installation/))

### 1. 克隆项目

```bash
git clone https://github.com/whitea133/Pywebview-Vue-FastApi.git
cd Pywebview-Vue-FastApi
```

### 2. 安装前端依赖

```bash
cd web
npm install
```

### 3. 安装后端依赖

```bash
cd ../app
uv sync
```

---

## 💻 开发指南

### 模式一：开发模式（推荐）

前后端独立运行，支持热重载，适合开发调试。

**终端 1 - 启动前端：**

```bash
cd web
npm run dev
# 默认运行在 http://localhost:5173
```

**终端 2 - 启动桌面端（开发模式）：**

```bash
cd app
uv run main.py --mode dev
```

### 模式二：静态模式

使用已构建的前端静态文件运行，接近生产环境。

```bash
# 1. 构建前端
cd web
npm run build

# 2. 启动桌面端（静态模式，默认）
cd ../app
uv run main.py
```

### 模式三：仅后端服务

只启动 FastAPI 服务器，可通过浏览器访问。

```bash
cd app
uv run main.py --server
# 访问 http://localhost:8000
# API 文档 http://localhost:8000/docs
```

---

## 🛠️ 常用命令

### 前端命令

```bash
cd web

npm run dev          # 启动开发服务器
npm run build        # 构建生产版本
npm run preview      # 预览生产构建
npm run type-check   # TypeScript 类型检查
```

### 后端命令

```bash
cd app

uv sync              # 同步依赖
uv run main.py       # 启动桌面应用
uv run main.py --server              # 仅启动后端
uv run main.py --mode dev            # 开发模式
uv run main.py --port 8080           # 自定义端口
```

---

## 📦 构建部署

### 构建前端

```bash
cd web
npm run build
# 构建产物输出到 webdist/ 和 app/static/
```

### 打包桌面应用

使用 PyInstaller 或其他工具将 Python 应用打包为可执行文件：

```bash
cd app
# 安装 PyInstaller
uv add --dev pyinstaller

# 打包
uv run pyinstaller --onefile --windowed main.py
```

---

## 🧩 技术栈

| 层级           | 技术         | 版本   | 说明            |
| -------------- | ------------ | ------ | --------------- |
| **后端** | FastAPI      | ^0.120 | 高性能 Web 框架 |
|                | Uvicorn      | ^0.38  | ASGI 服务器     |
|                | Pywebview    | ^6.1   | 桌面应用封装    |
|                | Loguru       | ^0.7   | 日志记录        |
| **前端** | Vue          | ^3.5   | 渐进式框架      |
|                | Vue Router   | ^4.6   | 路由管理        |
|                | Pinia        | ^3.0   | 状态管理        |
|                | TypeScript   | ~5.9   | 类型安全        |
|                | Vite         | ^7.1   | 构建工具        |
| **UI**   | Tailwind CSS | ^4.1   | 原子化 CSS      |
|                | Reka UI      | ^2.6   | 无头组件库      |
|                | Lucide Vue   | ^0.548 | 图标库          |

---

## 📝 开发规范

### 添加新 API 路由

1. 在 `app/routers/` 目录下创建新的 `.py` 文件
2. 创建 `APIRouter` 实例并命名为 `router`
3. 路由会自动注册，无需手动导入

```python
# app/routers/my_api.py
from fastapi import APIRouter

router = APIRouter(prefix="/api/my", tags=["My API"])

@router.get("/hello")
def hello():
    return {"message": "Hello, World!"}
```

### 添加新页面

1. 在 `web/src/views/` 创建 Vue 组件
2. 在 `web/src/router/index.ts` 添加路由配置

---

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

---

## 📄 许可证

本项目基于 [MIT](LICENSE) 许可证开源。

---

<div align="center">

**🌟 如果这个项目对你有帮助，请给个 Star 支持一下！**

Made with ❤️ using Pywebview + Vue 3 + FastAPI

</div>
