# ❤️ Heart Disease Prediction Web App

An end-to-end **Heart Disease Prediction** web application built using **Machine Learning** and **Flask**. This project takes in essential medical inputs and predicts whether an individual is at high or low risk of heart disease. The model was trained on a custom dataset featuring a unique `QuantumPatternFeature`, achieving an accuracy of **95%**.

---

## 🔍 Features

- 📊 ML pipeline trained on multiple classifiers
- ✅ Automatically selects the best model based on accuracy
- 💡 Clean and modern UI with animations
- 🧠 Predicts risk of heart disease from 6 key health features
- 🎨 Dynamic theme based on prediction result
- 🌐 Deployed using Render (free & simple deployment)

---

## 🚀 Technologies Used

- Python 3
- Scikit-learn
- Pandas
- NumPy
- Flask (Backend & API)
- Bootstrap 5 (Frontend)
- HTML/CSS
- Render (Deployment)

---

## 🧪 ML Model & Features

### Input Features:
- `Age` (in years)
- `Gender` (0 = Female, 1 = Male)
- `BloodPressure` (in mmHg)
- `Cholesterol` (mg/dL)
- `HeartRate` (bpm)
- `QuantumPatternFeature` (engineered numerical feature)

### Model Training:
- Logistic Regression
- Random Forest
- SVM
- KNN
- XGBoost  
✅ The best model is **automatically selected** and saved using **joblib**.

---

## 🖥️ App Preview

![UI Preview](https://your-screenshot-url.com) *(optional: add preview gif or image)*

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart-disease-predictor.git
   cd heart-disease-predictor

