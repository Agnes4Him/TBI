from flask import Flask, request, jsonify
from huggingface_hub import HfApi
import os

app = Flask(__name__)

api = HfApi()
HF_API_TOKEN = os.getenv('HF_API_TOKEN')
api.set_access_token(HF_API_TOKEN)
org_name = 'ML Demos'

@app.route('/')
def ping():
    return ('Hello from TBI API')

@app.route('/completion', methods=['POST'])
def completion():
    try:
        data = request.json()
        if not data:
            raise ValueError("Missing data in request body")
        return jsonify({
            "status": "success",
            "response": [ {"role": "assistant", "message": "response"} ]
        })
    except:
        return jsonify({
            "status": "error",
            "message": "error message"
        })

@app.route('/status', methods=['GET'])
def get_status():
    pass

@app.route('/model', methods=['GET'])
def get_model():
    pass

@app.route('/model', methods=['POST'])
def post_model():
    pass

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)