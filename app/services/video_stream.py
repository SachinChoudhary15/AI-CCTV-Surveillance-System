

import cv2
from app.core.config import settings

from app.core.logger import Logger


class VideoStream:

    def __init__(self):

        self.video_source = int(settings.VIDEO_SOURCE)
        self.cap = cv2.VideoCapture(self.video_source)

        if not self.cap.isOpened():
            raise ValueError(f"Unable to open video source {self.video_source}")

        self.frame_width = int(settings.FRAME_WIDTH)
        self.frame_height = int(settings.FRAME_HEIGHT)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

        self.logger = Logger(log_file="logs/video_stream.log")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.logger.error("Failed to read frame from video stream")
            return None
        
        return frame
    
    def show_frame(self, frame):
        cv2.imshow('Video Stream', frame)


    def stop_stream(self):
        self.cap.release()
        cv2.destroyAllWindows()
