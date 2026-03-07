class AIEngine:
    def __init__(self):
        self.context = {}  # Stores conversation context

    def process_input(self, user_input):
        # Process user input and update context
        self.update_context(user_input)
        response = self.generate_response(user_input)
        return response

    def update_context(self, user_input):
        # Update the context based on user input
        self.context['last_input'] = user_input

    def generate_response(self, user_input):
        # Generate a response based on the input and context
        response = f'You said: {user_input}. How can I assist you further?'
        return response  

# Example usage:
if __name__ == '__main__':
    ai_engine = AIEngine()
    user_input = input('Say something: ')
    print(ai_engine.process_input(user_input))