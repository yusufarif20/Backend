from flask import Flask, request, jsonify
import openai 

app = Flask(__name__)

# Konfigurasi API Key jika pakai OpenAI
openai.api_key = 'sk-...'

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json['message']
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    chatbot_reply = response['choices'][0]['message']['content']
    
    return jsonify({"reply": chatbot_reply})