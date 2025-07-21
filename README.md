# 🏦 Bank Term Deposit Prediction App

A professional web application built using Machine Learning to predict whether a customer will subscribe to a term deposit. This project was developed as part of a Data Analytics Internship.

---

## 📌 Project Overview

This project leverages a **Random Forest Classifier** trained on the popular Bank Marketing Dataset. The model is deployed through a Streamlit web application for interactive use.

Users can input customer information, and the model predicts the likelihood of term deposit subscription based on historical campaign data.

---

## 🚀 Features

✅ Real-time prediction  
📊 User-friendly Streamlit interface  
🧠 Trained ML model (Random Forest)  
📂 Proper file and folder structure  
💾 Encoders and feature order stored for consistent prediction  
🖼️ Visually enhanced UI with image & emojis

---

## 🧠 Technologies Used

- Python 3.10  
- Pandas, NumPy  
- Scikit-learn  
- Joblib  
- Streamlit  
- Matplotlib (for optional visualization)

---

## 📂 Project Structure

```
bank_term_deposit_app/
│
├── app.py                     # Streamlit web application
├── bankmarketing.csv          # Original dataset
├── random_forest_model.pkl    # Trained model
├── label_encoders.pkl         # Label encoders for categorical data
├── feature_names.pkl          # Ordered feature names used during training
├── .gitignore                 # Files/directories to ignore in Git
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 💻 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bank_term_deposit_app.git
   cd bank_term_deposit_app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

> ⚠️ Ensure all the `.pkl` files (`random_forest_model.pkl`, `feature_names.pkl`, `label_encoders.pkl`) are present in the same directory as `app.py`.

---

## 🧪 Model Details

- **Algorithm**: Random Forest Classifier  
- **Target Variable**: `y` – whether the client has subscribed to a term deposit  
- **Evaluation Metrics**: Accuracy, Precision, Recall

---

## 📸 Screenshots

> _[Optional]_ You can take a screenshot of your running web app and include here:
```
🖼️ ![App Screenshot](assets/screenshot.png)
```

---

## 🔒 .gitignore (recommended content)

```
__pycache__/
*.pkl
*.csv
.env
*.DS_Store
*.pyc
```

---

## 📦 Generate requirements.txt

After installing all needed packages:

```bash
pip freeze > requirements.txt
```

---

## 🙋‍♂️ Developed By

**Sandeep Yelikatte**  
_Data Analyst & Machine Learning Intern_  
📧 sandeepgoud1215@gmail.com  
🔗 [GitHub](https://github.com/sandeepgoud1215)

---

## 📚 Dataset Source

[UCI Machine Learning Repository – Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

---

## ✅ Internship Submission Status

- [x] Data Preprocessing  
- [x] Model Training  
- [x] Web App Development  
- [x] Model Integration  
- [x] Deployment Ready  
- [x] Professional README  
