# 珊瑚Ai（Demo）

一个基于 Flask 的智能聊天应用示例，界面风格参考海螺 AI，包含：

- 深色聊天主界面
- 左侧栏历史会话列表
- 语音按钮（预留交互）
- `/api/chat` 对话接口
- `/api/reset` 重置会话接口

## 启动方式

```bash
python main.py
```

默认地址：`http://127.0.0.1:5000`

## API

### `POST /api/chat`

请求：

```json
{ "message": "帮我拆解今天的任务计划" }
```

响应：

```json
{ "reply": "...", "history": [{"role":"user","content":"..."}] }
```

### `POST /api/reset`

重置历史对话。
