# WX-DEMO-20261111-01 · 偏好不等于授权

交互原型，非已上线功能。全部人物、偏好、活动与日历均为虚构。仅本地实现，不含客户案例或真实使用效果。

## 运行

直接用浏览器打开本目录 `index.html` 即可，无构建、无依赖。
也可在本目录运行 `python3 -m http.server 8080 --bind 127.0.0.1`，访问 http://127.0.0.1:8080 。

## 体验与授权规则

1. 左栏只读虚拟偏好，中栏自动展示三个备选，右栏承诺数为 0。
2. 选择备选，核对对象、完整日期、时间、活动与范围。未勾选批准时，确认按钮禁用。
3. 勾选批准并点击“确认这一次安排”，才会写入一条模拟记录。
4. 改选会清除待批准状态。同一备选不能重复创建；已确认记录不会因改选而消失。
5. “模拟撤销”清空本次页面全部承诺；“重置演示”或刷新恢复初始假数据。

只使用页面内存，不使用持久存储、真实账号或日历 API。批准范围始终仅限本页模拟记录，不能外推为邀请、预订、发消息或未来行动的授权。

## 交付物

- `index.html`：可运行 Demo。
- `artifacts/03-confirmed.png`：1600×900 真实 Demo 截图，三栏呈现偏好、待决定与确认记录，适合作为 X 配图。
- `artifacts/01-preference.png`、`02-pending.png`、`03-confirmed.png`：三帧真实演示截图。
- `storyboard.md`：3 帧故事板与 20 秒演示脚本。
- `verify.cjs`、`artifacts/verification.json`：浏览器验证脚本与实际结果。

## 复验

需 Node.js、Playwright 及 Chromium；这是开发验证依赖，Demo 本身无需安装。

```sh
npm install --prefix /tmp/wakenx-tools --cache /tmp/wakenx-npm-cache playwright
PLAYWRIGHT_BROWSERS_PATH=/tmp/wakenx-browsers /tmp/wakenx-tools/node_modules/.bin/playwright install chromium
PLAYWRIGHT_BROWSERS_PATH=/tmp/wakenx-browsers PLAYWRIGHT_MODULE=/tmp/wakenx-tools/node_modules/playwright node verify.cjs
```

## 局限与交付阶段

- 接单与本地实现单独记录；实际验收以 verification.json 为准。
- 无真实日历冲突检测、身份验证、服务端并发控制、持久化审计或真实撤销。仅用于说明交互和权限边界。
- 去重限当前页面内的同一备选，撤销后可以重新批准。改选清除的是待批准状态，不撤回已经确认的记录。
- 撤销为全部清空的简化演示，不含逐条撤销；无外部消息或通知。
- 未进行跨浏览器或辅助技术全面验收。
- 代码通过 PR 交付审阅；未部署运行站点或向社交平台发送内容。图文只是交付素材，社交平台公开发布需另行授权。

## 本次实际验收记录

2026-11-11，Chromium 158.0.8127.18，11 项浏览器检查通过；实际记录见 `artifacts/verification.json`。截图为 1600×900，同时检查 390×844 视口无横向溢出。已人工查看确认态截图，主要文案与控件完整可见。

本环境 Playwright 自动下载浏览器多次遇到连接中断，改为从相同官方包的 Google Storage 地址下载 Chrome Headless Shell。实际执行命令（浏览器和工具位于临时目录，不包含在交付包）：

```sh
PLAYWRIGHT_MODULE=/tmp/wakenx-tools/node_modules/playwright CHROMIUM_PATH=/tmp/wakenx-headless/chrome-headless-shell-linux-arm64/chrome-headless-shell node wakenx-demo/verify.cjs
```

以上命令在仓库根目录运行。未执行跨浏览器测试；截图与验收不代表生产环境的可靠性或授权安全保证。
