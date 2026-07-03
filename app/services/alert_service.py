
import time
from datetime import datetime

from app.services.telegram_alert import TelegramAlert
from app.services.database_service import DatabaseService
from app.core.logger import Logger


class AlertService:

    def __init__(self):
        self.db_service = DatabaseService()
        self.telegram_alert = TelegramAlert()
        self.logger = Logger(log_file="logs/alert_service.log")

        # Alert Cooldown (seconds)
        self.alert_cooldown = 20
        self.last_alert_time = 0

    def can_send_alert(self):
        current_time = time.time()
        if current_time - self.last_alert_time >= self.alert_cooldown:
            self.last_alert_time = current_time
            return True

        return False

    def send_alert(self, total_people):
        if not self.can_send_alert():
            return False

        message = ("SURVEILLANCE ALERT \n\n"
            f"People Detected : {total_people}\n"
            f"Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        self.logger.info(f"Alert Triggered | People Detected: {total_people}")

        telegram_sent = self.telegram_alert.send_message(message)
        if telegram_sent:
            self.logger.info("Telegram alert sent successfully.")

        else:
            self.logger.warning("Telegram alert could not be sent.")

        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.db_service.insert_alert(
                event_type="person_detection",
                total_people=total_people,
                timestamp=current_timestamp,
                alert_type="telegram_alert",
                description="Person detected by AI CCTV Surveillance System"
            )

            self.logger.info("Alert saved to database successfully.")

        except Exception as e:
            self.logger.error(f"Database Error: {e}")
        return True
        