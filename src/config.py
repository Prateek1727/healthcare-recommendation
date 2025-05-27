import os

class Config:
    RAW_DATA_PATH = os.getenv("RAW_DATA_PATH", "data/raw/")
    PROCESSED_DATA_PATH = os.getenv("PROCESSED_DATA_PATH", "data/processed/")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))