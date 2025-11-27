# Pywebview-Vue-FastApi项目模板

## 1. 项目结构

```
.
|-- app                      # FastAPI 后端与 pywebview 启动入口
|   |-- main.py              # 桌面端入口，启动 uvicorn 与 webview
|   |-- app.py               # FastAPI 应用、静态资源挂载与路由自动注册
|   |-- routers/             # API 路由模块（示例 test.py）
|   |-- static/              # 前端打包后的静态资源（index.html 与 assets）
|   |-- desktop/             # 桌面端相关适配代码占位
|   |-- pyproject.toml
|   `-- uv.lock
|
|-- web                      # Vue 3 + Vite + Tailwind 前端源码
|   |-- src/
|   |   |-- main.ts, App.vue
|   |   |-- router/          # 前端路由
|   |   |-- stores/          # 状态管理示例
|   |   |-- views/           # 页面组件
|   |   `-- components/      # 通用组件（含图标、UI）
|   |-- public/
|   |-- package.json, package-lock.json, vite.config.ts
|   `-- README.md
|
|-- webdist                  # 前端构建产物（供静态模式加载）
|-- tests/                   # 后端测试
|   `-- test.py
`-- README.md
```

## 2. 安装前端环境(已经配置了TailwindCss样式 与Shadcn组件)
```
cd web
npm install
npm run dev -- 启动前端项目
```

## 3. 安装后端环境
```
cd app
uv sync
uv run main.py -- 启动后端项目
```