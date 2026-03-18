class ConversationMemory:
    def __init__(self):
        self.dialogue_history = []

    def add_dialogue(self, dialogue):
        self.dialogue_history.append(dialogue)

    def clear_memory(self):
        self.dialogue_history.clear()
