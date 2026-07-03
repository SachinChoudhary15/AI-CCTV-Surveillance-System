    
import requests
from requests.exceptions import RequestException

from app.core.config import settings
from app.core.logger import Logger

class TelegramAlert:
    def __init__(self):

        self.bot_token = settings.TELEGRAM_BOT_TOKEN
        self.chat_id = settings.TELEGRAM_CHAT_ID

        self.logger = Logger(log_file="logs/telegram_alert.log")


    def send_message(self, message):

        url = (f"https://api.telegram.org/" f"bot{self.bot_token}/sendMessage")
        payload = {"chat_id": self.chat_id,"text": message,}

        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            self.logger.info("Telegram alert sent successfully.")
            return True

        except RequestException as e:
            self.logger.error(f"Telegram Error: {e}")
            print(f"Telegram Error: {e}")
            return False