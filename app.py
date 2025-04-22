from flask import Flask, request, jsonify
import openai  # atau logika chatbot buatan sendiri

app = Flask(__name__)

# Konfigurasi API Key jika pakai OpenAI
openai.api_key = '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'

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json['message']
    
    # Jika pakai OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    chatbot_reply = response['choices'][0]['message']['content']
    
    return jsonify({"reply": chatbot_reply})

if __name__ == "__main__":
    app.run(debug=True)
