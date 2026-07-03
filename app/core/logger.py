import logging
import os


class Logger:
    def __init__(self, log_file="logs/app.log", log_level=logging.INFO):
        self.logger = logging.getLogger("AI_CCTV_Logger")

        # Prevent duplicate handlers
        if self.logger.handlers:
            return

        self.logger.setLevel(log_level)

        log_directory = os.path.dirname(log_file)

        if log_directory and not os.path.exists(log_directory):
            os.makedirs(log_directory)

        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

        file_handler = logging.FileHandler(log_file, encoding="utf-8")

        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)