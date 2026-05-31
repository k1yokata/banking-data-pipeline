from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

TRANSACTION_DATA_PATH = RAW_DATA_DIR / "transaction_data.csv"
CUSTOMER_DATA_PATH = RAW_DATA_DIR / "customer_data.csv"
BANK_DATA_PATH = RAW_DATA_DIR / "bank_data.csv"

TRANSACTION_CLEANED_PATH = PROCESSED_DATA_DIR / "transaction_cleaned.csv"
CUSTOMER_CLEANED_PATH = PROCESSED_DATA_DIR / "customer_cleaned.csv"
BANK_CLEANED_PATH = PROCESSED_DATA_DIR / "bank_cleaned.csv"