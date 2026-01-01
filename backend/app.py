from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "CloudForge Backend is running!"

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/projects')
def projects():
    return jsonify([
        {
            "name": "CloudForge Portfolio",
            "description": "Cloud-native portfolio with CI/CD and cloud hosting",
            "tech": ["Python","AWS S3", "Flask", "Cloudflare", "GitHub Actions"]
        }
    ])
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
# Random comment to trigger backend CI workflow