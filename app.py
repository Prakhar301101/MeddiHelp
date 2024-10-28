from flask import Flask, render_template, jsonify, request
import json
from gemini import PillPawChatbot

app = Flask(__name__)
chatbot = PillPawChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/events')
def get_events():
    with open('events.json') as f:
        events = json.load(f)
    return jsonify(events)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = chatbot.get_pillpaw_response(user_message)

    # Ensure response is a string
    if isinstance(response, dict):
        response_message = response.get('message', "Sorry, I didn't understand that.")
    else:
        response_message = response

    # Wrap the response message in a dictionary
    return jsonify({"message": response_message})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
