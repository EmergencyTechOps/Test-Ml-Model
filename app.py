from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form
        features = [float(x) for x in request.form.values()]
        features_array = np.array([features])
        prediction = model.predict(features_array)
        species = ['Setosa', 'Versicolor', 'Virginica']
        return jsonify({'species': species[prediction[0]]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
