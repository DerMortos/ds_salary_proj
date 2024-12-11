import pickle
import numpy as np

def load_model():
    file_name = "models/model_file.p"
    try:
        with open(file_name, 'rb') as pickled:
            data = pickle.load(pickled)
            model = data['model']
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def make_prediction(input_data, model):
    try:
        x_in = np.array(input_data).reshape(1, -1)
        prediction = model.predict(x_in)[0]
        return prediction
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None