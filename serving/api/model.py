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

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

@app.route('/')
def ping():
    return ('Hello from TBI API')

@app.route('/completion', methods=['POST'])
def completion():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("Missing data in request body")
        return jsonify({
            "status": "success",
            "response": [ {"role": "assistant", "message": "response"} ]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

@app.route('/status', methods=['GET'])
def get_status():
    try:
        req_body = request.get_json()
        model_name = req_body['model_name']
        endpoint_name = f"{org_name}/{model_name}"
        response = requests.get(
            f"https://api.endpoints.huggingface.cloud/v1/endpoints/{endpoint_name}",
            headers=headers
        )

        result = response.json()
        #print(f"Status: {result['status']}")
        return jsonify({
            "status": result['status']
        })
    except Exception as e:
        return jsonify({
            "message": str(e)
        })

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
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

@app.route('/model', methods=['POST'])
def deploy_model():
    try:
        req_body = request.get_json()
        model_name = req_body['model_name']
        endpoint_payload = {
            "provider": "aws",
            "region": "us-east-1",
            "instance_type": "ml.m5.large",
            "scaling": {"min_replicas": 1, "max_replicas": 1},
            "task": model_name,
            "model": f"{org_name}/{model_name}"
        }

        response = requests.post(
            "https://api.endpoints.huggingface.cloud/v1/endpoints",
            headers=headers,
            json=endpoint_payload
        )
        #print(response.json())

        return jsonify({
            "status": "success",
            "model_id": model_name
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)