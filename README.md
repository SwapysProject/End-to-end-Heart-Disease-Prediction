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

```
Heart_Prediction_Project/
│
├── app.py                  # Flask app
├── train_best_model.py     # ML model training script
├── model.pkl               # Saved best model
├── requirements.txt
├── Procfile                # Required for Render deployment
├── .render.yaml            # Render's optional configuration file
├── .gitignore
├── README.md
│
├── data/
│   └── Heart Prediction Quantum Dataset.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   └── models.ipynb

├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
```

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Heart_Prediction_Project.git
cd Heart_Prediction_Project
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model (Optional)
```bash
python train_best_model.py
```

### 5. Run the Web App
```bash
python app.py
```

### 6. Visit the App
Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Deploying to Render (Free Hosting)

1. **Add a `Procfile`** (already included):
   ```
   web: python app.py
   ```

2. **Push code to GitHub**

3. **Go to [https://render.com](https://render.com)** → Click **"New Web Service"**

4. Connect your GitHub repo

5. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python app.py`
   - **Region:** Asia → Singapore (closest to India)

6. Click **Deploy** and wait for your public URL.

---
## ⚠️ Disclaimer

> This project is built using a machine learning-based approach for **educational and demonstration purposes** only. It is **not a substitute for professional medical advice**. Please consult a qualified doctor for any health concerns.
---


