from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import generate_summary
from utils import extract_text_from_file

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to backend

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        summary_type = request.form.get("type", "extractive")
        size = int(request.form.get("size", 3))
        file = request.files.get("file")
        text = request.form.get("text", "")

        if file:
            content = extract_text_from_file(file)
        elif text:
            content = text
        else:
            return jsonify({"error": "No input provided"}), 400

        summary = generate_summary(content, summary_type, size)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
