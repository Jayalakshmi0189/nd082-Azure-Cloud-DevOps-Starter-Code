from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple test route
@app.route('/')
def home():
    return "Flask app is running!"

# Prediction route (example)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # For now, just return input as prediction
    return jsonify({"prediction": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
