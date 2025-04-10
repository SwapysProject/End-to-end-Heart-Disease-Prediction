from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        features = [
            float(request.form['age']),
            int(request.form['gender']),
            float(request.form['bloodpressure']),
            float(request.form['cholesterol']),
            float(request.form['heartrate']),
            float(request.form['quantum'])
        ]
        input_data = np.array(features).reshape(1, -1)
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "High risk of heart disease"
        else:
            result = "Low risk of heart disease"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
