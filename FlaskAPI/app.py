# https://towardsdatascience.com/machine-learning-model-deployment-on-heroku-using-flask-467acb4a34da
# https://www.geeksforgeeks.org/get-post-requests-using-python/

# changes made to deploy from console using gunicorn using ...
# >> gunicorn -w 4 -b 0.0.0.0:5000 app.py:app

import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import numpy as np
import pickle



def load_models():
    file_name = "models/model_file.p"
    try:
        with open(file_name, 'rb') as pickled:
            data = pickle.load(pickled)
            model = data['model']
        return model
    except Exception as e:
        return None

app = Flask(__name__)
# @app.route('/predict', methods=['GET'])
@app.route('/predict', methods=['POST'])    # changed to post for sending JSON

def predict():
    try:
        # stub input features
        request_json = request.get_json()
        x = request_json['input']
        #print(x)
        x_in = np.array(x).reshape(1,-1)

        # load model
        model = load_models()

        if model is None:
            return jsonify({'error': 'Model not found'}), 400

        prediction = model.predict(x_in)[0]

        response = json.dumps({'response': prediction})
        return response, 200
    except Exception as e:
        return jsonify({'error': str(e)}),500

if __name__ == '__main__':
   app.run(host='0.0.0.0')
