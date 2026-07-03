

import os
import cv2

from datetime import datetime

from streamlit import success

from app.core.logger import Logger


class SnapshotService:

    def __init__(self):

        self.snapshot_dir = "data/snapshots"

        os.makedirs(self.snapshot_dir,exist_ok=True)

        self.logger = Logger(log_file="logs/snapshot_service.log")

    def save_snapshot(self,frame):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = (f"snapshot_{timestamp}.jpg")

        filepath = os.path.join(self.snapshot_dir,filename)

        cv2.imwrite(filepath, frame)

        self.logger.info(f"Snapshot Saved: {filepath}")

        if success:
            self.logger.info(f"Snapshot Saved: {filepath}")

        else:
            self.logger.error("Snapshot Save Failed!")

        return filepath

