import pandas as pd

from src.config import (
    TRANSACTION_DATA_PATH,
    CUSTOMER_DATA_PATH,
    BANK_DATA_PATH,
)


def load_data():
    transaction_df = pd.read_csv(TRANSACTION_DATA_PATH)
    customer_df = pd.read_csv(CUSTOMER_DATA_PATH)
    bank_df = pd.read_csv(BANK_DATA_PATH)

    return transaction_df, customer_df, bank_df


def show_basic_info(transaction_df, customer_df, bank_df):
    print("Transaction data:")
    print(transaction_df.info())
    print(transaction_df.head())

    print("\nCustomer data:")
    print(customer_df.info())
    print(customer_df.head())

    print("\nBank data:")
    print(bank_df.info())
    print(bank_df.head())


def main():
    transaction_df, customer_df, bank_df = load_data()
    show_basic_info(transaction_df, customer_df, bank_df)


if __name__ == "__main__":
    main()