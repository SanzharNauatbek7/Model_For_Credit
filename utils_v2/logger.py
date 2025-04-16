import pandas as pd
import os

def log_input(user_input: dict, result: int):
    log_path = "logs.csv"
    user_input["Prediction"] = result
    df = pd.DataFrame([user_input])
    if os.path.exists(log_path):
        df.to_csv(log_path, mode='a', index=False, header=False, encoding='utf-8-sig')
    else:
        df.to_csv(log_path, index=False, encoding='utf-8-sig')
