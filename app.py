from flask import Flask, request, jsonify
import openai

openai.api_key = "your_openai_api_key"

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_message}]
    )

    bot_response = response["choices"][0]["message"]["content"]
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
