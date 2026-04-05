from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key="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")

@app.route("/")
def home():
    return render_template("Index-home.html")

@app.route("/")
def home():
    return render_template("AI.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    print("User:", user_message)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful visa assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Error ❌"}), 500

if __name__ == "__main__":
    app.run(debug=True)