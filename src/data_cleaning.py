import  pandas as pd
from src.data_preparation import load_data

class DataCleaner:
    def __init__(self):
        self.transaction_df, self.customer_df, self.bank_df = load_data()

    def clean_age(self):
        self.customer_df["Age"] = pd.to_numeric(
            self.customer_df["Age"],
            errors="coerce"
        )

        median_age = self.customer_df["Age"].median()
        self.customer_df["Age"] = self.customer_df["Age"].fillna(median_age)
        self.customer_df["Age"] = self.customer_df["Age"].astype(int)

    def run(self):
        self.clean_age()

def main():
    cleaner = DataCleaner()
    cleaner.run()

if __name__ == "__main__":
    main()