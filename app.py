from flask import Flask, render_template, request, jsonify
from chatbot import get_response

#while True:
#    print('Bot: ' + get_response(input('You: ')))
    
app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template('./frontend/index.html')

@app.post('/predict')
def predict():
   text = request.get_json().get('message')
   response = get_response(text)
   message = {'response': response}
   return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)