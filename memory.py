class ConversationMemory:
    def __init__(self):
        # Initialize memory storage for dialogue history, user preferences, and context
        self.dialogue_history = []
        self.user_preferences = {}
        self.context_cache = {}

    def add_dialogue(self, dialogue):
        # Add a dialogue entry to the history
        self.dialogue_history.append(dialogue)

    def set_user_preferences(self, preferences):
        # Set or update user preferences
        self.user_preferences.update(preferences)

    def get_user_preferences(self):
        # Retrieve user preferences
        return self.user_preferences

    def cache_context(self, key, value):
        # Cache a context value associated with a key
        self.context_cache[key] = value

    def get_cached_context(self, key):
        # Retrieve a cached context value by key
        return self.context_cache.get(key)

    def clear_memory(self):
        # Clear dialogue history and context cache
        self.dialogue_history.clear()
        self.context_cache.clear()