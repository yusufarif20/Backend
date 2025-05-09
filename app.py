from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return "Chat endpoint is working! Use POST to send a message."
    
    try:
        if not request.json or 'message' not in request.json:
            return jsonify({"error": "Missing 'message' in request"}), 400
        
        user_message = request.json['message']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            timeout=10  # Set timeout untuk OpenAI request
        )
        chatbot_reply = response['choices'][0]['message']['content']
        return jsonify({"reply": chatbot_reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500