# 💳 Kaspi-like Credit Scoring App

Приложение для скоринга клиентов, похожее на Kaspi, разработанное с использованием `Streamlit`, `XGBoost` и `pandas`. Позволяет оценить вероятность одобрения кредита на основе введённых данных.

## Онлайн Демо
[Посмотреть дашборд](https://modelforcredit-wmw6lbygwabtrqrbckcnzp.streamlit.app/)

---

## 🚀 Как запустить

1. Клонируй репозиторий:

```bash
git clone https://github.com/SanzharNauatbek7/Model_For_Credit.git
cd Model_For_Credit
```

2. Установи зависимости:

```bash
pip install -r requirements.txt
```

3. Запусти приложение:

```bash
streamlit run app_v2/app_v2.py
```

---

## 🧠 Описание модели

Модель — `XGBoostClassifier`, обучена на синтетических данных (генератор внутри `train_model_v2.ipynb`). Признаки:

- Возраст
- Доход и доход супруга
- Стаж работы
- Кредитная история
- Тип занятости
- Наличие машины / ипотеки
- Образование, регион, тип жилья и т.д.

### 🎯 Целевая переменная:
`1` — кредит одобрен, `0` — отказ.

---

## 📈 Пример предсказания

После ввода параметров нажмите **"Проверить решение"**:

- ✅ *Кредит одобрен!* — если модель оценивает клиента как платёжеспособного.
- ❌ *Кредит отклонён.* — если есть риски невозврата.

Все предсказания логируются в `logs.csv`.

---

## 🛠 Используемые технологии

- `Streamlit` — фронтенд
- `XGBoost` — ML-модель
- `pandas / numpy` — обработка данных
- `scikit-learn` — препроцессинг
- `pickle` — сериализация

---

## 🧪 Как обучалась модель

В `train_model_v2.ipynb` создаются данные, генерируются признаки и обучается модель. Целевая переменная вычисляется на основе логики "здорового" заемщика.

---

## 👨‍💻 Автор

Разработчик: [Санджар Науатбек](https://github.com/SanzharNauatbek7)

---
