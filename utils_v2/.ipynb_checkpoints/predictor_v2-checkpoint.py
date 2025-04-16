# 📁 utils/predictor.py

import pickle
import numpy as np
import pandas as pd

# 📦 Загрузка модели и энкодеров
with open("model_v2/xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_v2/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

# 🔮 Основная функция предсказания
def predict_default(user_input: dict) -> int:
    # 📐 Расчёт adjusted_income
    income = user_input.get("Income", 0)
    spouse_income = user_input.get("Spouse_income", 0)
    children = user_input.get("Children", 0)
    adjusted_income = income + spouse_income - children * 30000
    loan_amount = user_input.get("Loan_amount", 500000)
    loan_term = user_input.get("Loan_term_months", 36)

    monthly_payment = loan_amount / loan_term
    payment_to_income = monthly_payment / (adjusted_income + 1)


    # 🔧 Подготовка признаков
    features = {
        "Age": user_input.get("Age", 30),
        "Gender": user_input.get("Gender", "Мужчина"),
        "Spouse_income": spouse_income,
        "Marital_status": user_input.get("Marital_status", "Не женат/не замужем"),
        "Work_experience": user_input.get("Work_experience", 5),
        "Children": children,
        "Loan_amount": loan_amount,
        "Loan_term_months": loan_term,
        "Has_mortgage": user_input.get("Has_mortgage", 0),
        "Has_car": user_input.get("Has_car", 1),
        "Credit_history": user_input.get("Credit_history", "Хорошая"),
        "Education": user_input.get("Education", "Высшее"),
        "Region": user_input.get("Region", "Алматы"),
        "Employment_type": user_input.get("Employment_type", "Сотрудник"),
        "Housing_type": user_input.get("Housing_type", "Собственное"),
        "Current_loans": user_input.get("Current_loans", 0),
        "adjusted_income": adjusted_income,
        "Monthly_payment": monthly_payment,
        "Payment_to_income_ratio": payment_to_income
    }

    # 🧠 Кодируем категориальные признаки
    for col, enc in encoders.items():
        val = features.get(col)
        if val in enc.classes_:
            features[col] = enc.transform([val])[0]
        else:
            features[col] = 0  # default if unseen

    # 🧮 Вектор признаков
    df_input = pd.DataFrame([features])
    prediction = model.predict(df_input)[0]

    return int(prediction)
