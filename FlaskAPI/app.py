# https://towardsdatascience.com/machine-learning-model-deployment-on-heroku-using-flask-467acb4a34da
# https://www.geeksforgeeks.org/get-post-requests-using-python/

# changes made to deploy from console using gunicorn using ...
# >> gunicorn -w 4 -b 0.0.0.0:5000 app.py:app

import os
from flask import Flask, jsonify, request, render_template
import json
from transform_input import transform_input
import numpy as np
import pickle



def load_models():
    file_name = os.path.join(os.path.dirname(__file__), 'models', 'model_file.p')
    try:
        with open(file_name, 'rb') as pickled:
            data = pickle.load(pickled)
            model = data['model']
        return model
    except Exception as e:
        return None

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])    # changed to post for sending JSON
def predict():
    try:
        # stub input features
        request_json = request.get_json()
        x = transform_input(request_json)
        print("Transformed:", len(x), "features")
        x_in = np.array(x).reshape(1,-1)

        # load model
        model = load_models()

        if model is None:
            return jsonify({'error': 'Model not found'}), 400

        prediction = model.predict(x_in)[0]
        print("Prediction:", prediction)

        ## return jsonify({'salary', round(float(prediction), 2)}), 200     ## np type could not be serialized
        return jsonify({'salary': round(float(prediction), 2)}), 200
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}),500

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
