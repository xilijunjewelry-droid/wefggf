class AIEngine:
    """A lightweight chat engine that mimics a helpful assistant style."""

    def __init__(self, memory):
        self.memory = memory

    def process_input(self, user_input):
        self.memory.add_dialogue({'role': 'user', 'content': user_input})
        response = self.generate_response(user_input)
        self.memory.add_dialogue({'role': 'assistant', 'content': response})
        return response

    def generate_response(self, user_input):
        text = user_input.lower()

        if any(word in text for word in ['你好', 'hello', 'hi']):
            return '你好，我是珊瑚Ai。很高兴见到你！你想聊点什么？'

        if any(word in text for word in ['总结', 'summary']):
            recent = [d['content'] for d in self.memory.dialogue_history if d['role'] == 'user'][-3:]
            if not recent:
                return '还没有可总结的内容。你可以先告诉我一些信息。'
            joined = '；'.join(recent)
            return f'这是你最近提到的重点：{joined}。如果需要，我可以继续整理成行动清单。'

        if any(word in text for word in ['计划', 'todo', '任务']):
            return '好的，给你一个简单行动方案：\n1. 明确目标\n2. 拆分步骤\n3. 设定截止时间\n4. 每天复盘 5 分钟。'

        return f'我理解你的意思是：「{user_input}」。如果你愿意，我可以继续深入：给你建议、总结要点，或生成执行计划。'
