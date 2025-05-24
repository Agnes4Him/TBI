from flask import Flask, request, jsonify
from huggingface_hub import HfApi
import os
import requests

app = Flask(__name__)

HF_API_TOKEN = os.getenv('HF_API_TOKEN')
if not HF_API_TOKEN:
    raise EnvironmentError("HF_API_TOKEN is not set in environment variables.")

api = HfApi()
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
    try:
        result = []
        each_model = {}
        models = api.list_models(author=org_name)
        for model in models:
            #print(f"{model.modelId} | {model.private} | {model.tags}")
            each_model["model_id"] = model.modelId
        result.append(each_model)
        return jsonify({
            "status": "success",
            "result": result
        })
    except:
        pass

@app.route('/model', methods=['POST'])
def post_model():
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json"
    }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)