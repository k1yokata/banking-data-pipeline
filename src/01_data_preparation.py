import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

TRANSACTION_DATA_PATH = RAW_DATA_DIR / 'transaction_data.csv'
CUSTOMER_DATA_PATH = RAW_DATA_DIR / 'customer_data.csv'
BANK_DATA_PATH = RAW_DATA_DIR / 'bank_data.csv'

def load_data():
    transaction_df = pd.read_csv(TRANSACTION_DATA_PATH)
    customer_df = pd.read_csv(CUSTOMER_DATA_PATH)
    bank_df = pd.read_csv(BANK_DATA_PATH)

    return transaction_df, customer_df, bank_df

def show_basic_info(df: pd.DataFrame, name: str):
    print("=" * 80)
    print(f"Name: {name}")
    print("=" * 80)

    print("\nПервые 5 строк")
    print(df.head(5))

    print("\nРазмер Таблицы")
    print(df.shape)

    print("\nТипы Данных")
    print(df.dtypes)

    print("\nНазвания колонок")
    print(df.columns.tolist())

    print("\nКоличество пропусков")
    print(df.isnull().sum())

    print("\nКоличество дубликатов")
    print(df.duplicated().sum())

    print("\nБазовая статистика")
    print(df.describe(include='all'))

    print("\n")

def main():
    transaction_df, customer_df, bank_df = load_data()

    print("\nДанные успешно загружены.\n")

    show_basic_info(transaction_df, "Transaction Data")
    show_basic_info(customer_df, "Customer Data")
    show_basic_info(bank_df, "Bank Data")

if __name__ == '__main__':
    main()