# Heart Disease Prediction with Multiple Classification Models

This project applies multiple machine learning classification models to predict the presence of heart disease based on features such as age, blood pressure, cholesterol, and a quantum-based feature.

## Models Used

- Logistic Regression  
- Decision Tree  
- Random Forest  
- K-Nearest Neighbors  
- Support Vector Machine (SVM)  
- Naive Bayes  
- Gradient Boosting  
- Neural Network (MLP)

## Dataset

The dataset used is `Heart Prediction Quantum Dataset.csv` with the following features:
- Age
- Gender
- BloodPressure
- Cholesterol
- HeartRate
- QuantumPatternFeature
- Target: HeartDisease (0 = No, 1 = Yes)

## Steps

1. Load and preprocess the dataset  
2. Train each model individually  
3. Evaluate with Accuracy, Precision, Recall, and F1-Score  
4. Display results in a comparative table  
5. Visualize confusion matrices for all models  

## Best Performing Models

Logistic Regression and Random Forest achieved the highest F1-Scores and accuracy on this dataset.

## Requirements

To install all required packages, use the provided `requirements.txt` file:

```bash
pip install -r requirements.txt

