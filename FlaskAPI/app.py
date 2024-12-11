# https://towardsdatascience.com/machine-learning-model-deployment-on-heroku-using-flask-467acb4a34da
# https://www.geeksforgeeks.org/get-post-requests-using-python/

# changes made to deploy from console using gunicorn using ...
# >> gunicorn -w 4 -b 0.0.0.0:5000 app.py:app

import flask
from flask import Flask, render_template, request, jsonify
from models.models_utils import  load_model, make_prediction
import numpy as np
from data_input import data_in


app = Flask(__name__)

model = load_model()

@app.route('/')
def main():
    """Render the main page/prediction input form"""
    return render_template('main.html', data_in=data_in)


@app.route('/selections')
def selections():
    """Render the selections page"""
    return render_template('selections.html')



@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction and display the result."""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
    #original prediction code for array input
        # Retrieve input data from the form
        input_data = request.form.get('input_data')

        # Check if input_data is empty
        if not input_data:
            return jsonify({'error': 'No input data provided'}), 400

        # Convert input data to a list of floats
        input_data = [float(i) for i in input_data.split(',')]

        # Run prediction
        prediction = model.predict(np.array(input_data).reshape(1, -1))
        # Render result on the same page
        return render_template('main.html', prediction=round(prediction[0],1))
    except ValueError as ve:
        return jsonify({'error': f'Invalid input data: {ve}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
   app.run(host='0.0.0.0')
