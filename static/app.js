const chatEl = document.getElementById('chat');
const formEl = document.getElementById('composer');
const inputEl = document.getElementById('input');
const resetBtn = document.getElementById('resetBtn');
const voiceBtn = document.getElementById('voiceBtn');
const newSessionBtn = document.getElementById('newSessionBtn');
const sessionListEl = document.getElementById('sessionList');

let sessions = ['欢迎来到珊瑚Ai'];

function appendMessage(role, content) {
  const div = document.createElement('div');
  div.className = `msg ${role}`;
  div.textContent = content;
  chatEl.appendChild(div);
  chatEl.scrollTop = chatEl.scrollHeight;
}

function renderSessions() {
  sessionListEl.innerHTML = '';
  sessions.slice(-8).reverse().forEach((item) => {
    const li = document.createElement('li');
    li.textContent = item;
    sessionListEl.appendChild(li);
  });
}

function pushSession(title) {
  sessions.push(title.slice(0, 28));
  renderSessions();
}

appendMessage('assistant', '你好，我是珊瑚Ai。你可以让我做总结、计划、灵感整理。');
renderSessions();

formEl.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = inputEl.value.trim();
  if (!message) return;

  appendMessage('user', message);
  pushSession(message);
  inputEl.value = '';

  const resp = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });

  if (!resp.ok) {
    appendMessage('assistant', '请求失败，请稍后再试。');
    return;
  }

  const data = await resp.json();
  appendMessage('assistant', data.reply);
});

resetBtn.addEventListener('click', async () => {
  await fetch('/api/reset', { method: 'POST' });
  chatEl.innerHTML = '';
  appendMessage('assistant', '上下文已重置，我们重新开始吧。');
  pushSession('新会话');
});

newSessionBtn.addEventListener('click', () => {
  chatEl.innerHTML = '';
  appendMessage('assistant', '新会话已创建。告诉我你现在想解决什么问题？');
  pushSession('手动创建会话');
});

voiceBtn.addEventListener('click', () => {
  appendMessage('assistant', '🎙️ 语音输入功能预留中：后续可接入浏览器语音识别。');
});
