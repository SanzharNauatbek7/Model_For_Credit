import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils_v2.predictor_v2 import predict_default 
from utils_v2.logger import log_input

st.set_page_config(page_title="💳 Credit Checker", layout="centered")

st.title("Kaspi-like Кредитный Скоринг 💸")
st.write("Введите данные клиента, чтобы узнать — одобрен ли кредит.")

# 🎛 Ввод данных
age = st.slider("Возраст", 18, 65, 30)
gender = st.selectbox("Пол", ["Мужчина", "Женщина"])
marital_status = st.selectbox("Семейное положение", ["Не женат/не замужем", "Женат/Замужем"])

income = st.number_input("Уровень дохода (₸)", min_value=0, step=10000, value=250000)

spouse_income = 0
if marital_status == "Женат/Замужем":
    spouse_income = st.number_input("Доход супруга/супруги (₸)", min_value=0, step=10000, value=0)

experience = st.slider("Стаж работы (лет)", 0, 40, 5)
children = st.selectbox("Количество детей", [0, 1, 2, 3])
employment_type = st.selectbox("Тип занятости", ["Сотрудник", "Фрилансер", "Безработный"])
housing = st.selectbox("Тип жилья", ["Собственное", "Аренда"])
mortgage = st.radio("Есть ли ипотека?", [0, 1], format_func=lambda x: "Да" if x == 1 else "Нет")
car = st.radio("Есть ли автомобиль?", [0, 1], format_func=lambda x: "Да" if x == 1 else "Нет")
credit_history = st.selectbox("Кредитная история", ["Хорошая", "Плохая" , "Нет"])
education = st.selectbox("Образование", ["Среднее", "Высшее", "Магистратура", "Другое"])
region = st.selectbox("Регион проживания", ["Алматы", "Астана", "Шымкент", "Другой"])
current_loans = st.slider("Текущие кредиты", 0, 5, 0)
loan_amount = st.number_input("Желаемая сумма кредита (₸)", min_value=10000, max_value=2000000, step=10000, value=500000)
loan_term_months = st.selectbox("Срок кредита (в месяцах)", [6, 12, 24, 36, 48, 60], index=2)


# 👶 Учёт детей: отнимаем 30,000 за каждого
adjusted_income = income + spouse_income - (children * 30000)

# 📦 Сбор данных
user_input = {
    "Age": age,
    "Gender": gender,
    "Income": adjusted_income,
    "Work_experience": experience,
    "Children": children,
    "Has_mortgage": mortgage,
    "Has_car": car,
    "Credit_history": credit_history,
    "Education": education,
    "Region": region,
    "Current_loans": current_loans,
    "Marital_status": marital_status,
    "Spouse_income": spouse_income,
    "Employment_type": employment_type,
    "Housing_type": housing,
    "Loan_amount": loan_amount,
    "Loan_term_months": loan_term_months
}

# 🔍 Предсказание
if st.button("Проверить решение"):
    result = predict_default(user_input)
    log_input(user_input, result)

    if result == 1:
        st.success("✅ Кредит одобрен!")
    else:
        st.error("❌ Кредит отклонён.")
