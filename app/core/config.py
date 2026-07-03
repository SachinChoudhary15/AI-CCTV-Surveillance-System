

from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self):
        self.APP_NAME = os.getenv("APP_NAME")
        self.DEBUG = os.getenv("DEBUG")

        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT")

        self.VIDEO_SOURCE = os.getenv("VIDEO_SOURCE")
        self.FRAME_WIDTH = os.getenv("FRAME_WIDTH")
        self.FRAME_HEIGHT = os.getenv("FRAME_HEIGHT")

        self.YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH")
        self.YOLO_CONFIG_PATH = os.getenv("YOLO_CONFIG_PATH")

        self.TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        self.TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

        self.DB_NAME = os.getenv("DB_NAME")

        self.LOG_LEVEL = os.getenv("LOG_LEVEL")
        self.LOG_FILE = os.getenv("LOG_FILE")

# Create class Object
settings = Settings()


