# ❤️ Heart Disease Prediction with Multiple Classification Models

This project combines multiple machine learning classification models with a modern, responsive web interface built using Flask to predict the presence of heart disease.

The app provides an end-to-end solution—from training the models to deploying the prediction tool online.

---

## 🧠 Models Used

- Logistic Regression  
- Decision Tree  
- Random Forest  
- K-Nearest Neighbors  
- Support Vector Machine (SVM)  
- Naive Bayes  
- Gradient Boosting  
- Neural Network (MLP)

> The model with the highest F1-Score and accuracy is saved and used in the Flask app.

---

## 📊 Dataset

**File:** `Heart Prediction Quantum Dataset.csv`

### Features:
- **Age**
- **Gender** (0 = Female, 1 = Male)
- **BloodPressure**
- **Cholesterol**
- **HeartRate**
- **QuantumPatternFeature**
- **Target**: HeartDisease (0 = No, 1 = Yes)

---

## 🧪 ML Workflow

1. Load and preprocess the dataset  
2. Train multiple models  
3. Evaluate with Accuracy, Precision, Recall, F1-Score  
4. Compare models with visualizations  
5. Save the best-performing model as `model.pkl`

---

## 🌐 Web App Features

- Built with **Flask + Bootstrap 5**
- Vertical input form with animations
- Dynamic background color (green for low risk, red for high)
- Responsive layout for mobile and desktop
- Inputs retain values after prediction
- Includes a **"Clear All"** button
- Medical disclaimer included

---

## 📁 Project Structure

