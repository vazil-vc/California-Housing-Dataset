# 🏠 California House Price Prediction

A Machine Learning web application that predicts the median house price in California based on housing characteristics using **Linear Regression**. The application is built with **Scikit-learn** and deployed using **Streamlit**.

---

## 📌 Project Overview

This project uses the **California Housing Dataset** from Scikit-learn to predict the median house value based on features such as income, house age, number of rooms, population, and location.

The project demonstrates the complete Machine Learning workflow:

- Data Exploration (EDA)
- Data Preprocessing
- Feature Scaling
- Model Training
- Model Evaluation
- Model Serialization
- Streamlit Deployment

---

## 🚀 Demo

Enter the housing details and the application predicts the estimated median house price.

---

## 📂 Project Structure

```
California-Housing-Prediction/
│
├── dataset/
│   └── housing.csv
│
├── California_Housing.ipynb
├── app.py
├── house_price_model.pkl
├── house_price_scaler.pkl
├── requirements.txt
├── README.md
└── images/
```

---

## 📊 Dataset

**Dataset:** California Housing Dataset

Features:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

Target:

- Median House Value

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Joblib

---

## 📈 Machine Learning Workflow

1. Load Dataset
2. Perform Exploratory Data Analysis
3. Check Missing Values
4. Correlation Analysis
5. Feature Scaling using StandardScaler
6. Train-Test Split
7. Train Linear Regression Model
8. Evaluate Model
9. Save Model using Joblib
10. Deploy using Streamlit

---

## 📊 Model Performance

| Metric | Score |
|---------|--------|
| MAE | 0.5272 |
| MSE | 0.5306 |
| RMSE | 0.7284 |
| R² Score | 0.5958 |

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/California-Housing-Prediction.git
```

Move into the project directory

```bash
cd California-Housing-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add screenshots here.

Example:

```
images/home.png
images/prediction.png
```

---

## 📚 Concepts Learned

- Exploratory Data Analysis (EDA)
- Correlation Matrix
- Linear Regression
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Feature Scaling
- Model Serialization with Joblib
- Streamlit Deployment

---

## 🔮 Future Improvements

- Decision Tree Regression
- Random Forest Regression
- XGBoost Regression
- Hyperparameter Tuning
- Interactive Visualizations
- Model Comparison Dashboard

---

## 👨‍💻 Author

**Abdulla Zayn**

MCA Student | Aspiring AI & Machine Learning Engineer

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ If you found this project useful, consider giving it a star!