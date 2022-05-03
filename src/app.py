from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_response
import os

# while True:
#    print('Bot: ' + get_response(input('You: ')))

app = Flask(__name__)
CORS(app)

"""
@app.get('/')
def index_get():
    return render_template('./frontend/index.html')
"""


@app.post('/predict')
def predict():
    text = request.get_json()['message']
    print(text)
    message = {'answer': get_response(text)}
    return jsonify(message)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(debug=True, host='0.0.0.0', port=port)
