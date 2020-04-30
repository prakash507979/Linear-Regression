from flask import Flask
from flask import request
from flask_cors import CORS
import random
import pickle


app = Flask(__name__)
CORS(app)

@app.route("/")
def model_response():
    textMessage = request.args.get('textMessage')
    loaded_model = pickle.load(open('finalized_model.pkl', 'rb'))
    response = loaded_model.predict([[int(textMessage)]])
    return str(response)
	
    if __name__ == '__main__':
        #app.run(debug = False)
        app.run(host='0.0.0.0', port=80)