from flask import Flask, request, jsonify

app = Flask('TBI API')

@app.route('/')
def ping():
    return ('Hello from TBI API')

@app.route('/completion', methods=['POST'])
def post_completion():
    pass

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