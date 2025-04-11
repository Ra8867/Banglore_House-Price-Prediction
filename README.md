# 🏠 Bangalore House Price Prediction
This project predicts house prices in Bangalore based on features like location, square footage, number of bedrooms (BHK), and bathrooms using machine learning models. It covers the full pipeline from preprocessing to model training and deployment with a simple Flask web app.

📊 Dataset
Source: Kaggle - Bengaluru House Data

Key columns: location, size, total_sqft, bath, price

🧹 Data Cleaning Overview
Removed irrelevant columns and handled missing values

Engineered features like bhk and price_per_sqft

Grouped rare locations into "other"

Removed outliers for more accurate modeling

🧠 Models Used
Model	Description
Linear Regression	Baseline ML model
Lasso Regression	L1-regularized model to prevent overfit
Ridge Regression	Final deployed model with best R² score
✅ Best performance with Ridge Regression
📈 Evaluation Metric: R² Score

💻 Web App (Flask)
Built a web interface using Flask where users can:

Select location

Enter total square feet, BHK, and bathrooms

Get the predicted house price instantly

The backend uses a trained Ridge model (RidgeModel.pkl) to generate predictions.

🔧 Tech Stack
Python: Data processing & modeling

Scikit-learn: ML pipeline

Pandas, NumPy: Data wrangling

Flask: Web app backend

HTML (Jinja): Frontend template

Pickle: Model serialization

📌 Highlights
End-to-end ML pipeline: preprocessing → modeling → deployment

Outlier removal for more reliable predictions

Interactive web UI with Flask
