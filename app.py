from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():

    area = float(request.json['area'])

    input_data = pd.DataFrame({
        'Area_sqft': [area]
    })

    prediction = model.predict(input_data)

    return jsonify({
        'price': float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)