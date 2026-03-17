from flask import Flask, jsonify, render_template, request
from ai_engine import AIEngine
from memory import ConversationMemory

app = Flask(__name__)

memory = ConversationMemory()
ai_engine = AIEngine(memory=memory)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    payload = request.get_json(silent=True) or {}
    user_input = (payload.get('message') or '').strip()
    if not user_input:
        return jsonify({'error': 'message is required'}), 400

    response = ai_engine.process_input(user_input)
    return jsonify({'reply': response, 'history': memory.dialogue_history[-12:]})


@app.route('/api/reset', methods=['POST'])
def reset():
    memory.clear_memory()
    return jsonify({'message': 'conversation reset'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
