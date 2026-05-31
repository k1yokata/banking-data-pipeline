import  pandas as pd

from src.config import PROCESSED_DATA_DIR, CUSTOMER_CLEANED_PATH
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

    def save_cleaned_data(self):
        PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

        self.customer_df.to_csv(CUSTOMER_CLEANED_PATH, index=False)
        print("Cleaned data saved to {}".format(CUSTOMER_CLEANED_PATH))

    def run(self):
        self.clean_age()
        self.save_cleaned_data()

def main():
    cleaner = DataCleaner()
    cleaner.run()

if __name__ == "__main__":
    main()