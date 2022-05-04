
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    """
    flask post request
    """
    text = request.get_json()["message"]
    print(text)
    message = {"answer": get_response(text)}
    return jsonify(message)


if __name__ == "__main__":
    """
    test main function
    """
    app.run(debug=True, host="0.0.0.0", port=5000)
