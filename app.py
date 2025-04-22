from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return "Chat endpoint is working! Use POST to send a message."
    
    user_message = request.json['message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    chatbot_reply = response['choices'][0]['message']['content']
    return jsonify({"reply": chatbot_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)