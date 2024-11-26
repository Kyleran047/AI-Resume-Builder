from flask import render_template, request, jsonify
import openai

openai.api_key = "your_openai_api_key"

def init_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/generate", methods=["POST"])
    def generate_resume():
        data = request.json
        prompt = data.get("prompt", "")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300
        )
        return jsonify({"content": response.choices[0].text})
