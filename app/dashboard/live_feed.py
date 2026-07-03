import cv2

from app.detection.tracker import Tracker
from app.detection.person_detection import PersonDetector
from app.detection.face_detection import FaceDetector

from app.services.video_stream import VideoStream
from app.services.alert_service import AlertService
from app.services.snapshot_service import SnapshotService

from app.utils.draw_boxes import draw_boxes

class LiveFeedService:

    def __init__(self):

        self.video_stream = VideoStream()
        self.person_detector = PersonDetector()
        self.face_detector = FaceDetector()
        self.tracker = Tracker()
        self.alert_service = AlertService()
        self.snapshot_service = SnapshotService()

    def get_live_frame(self):
        frame = self.video_stream.get_frame()

        if frame is None:
            return None

        # Person Detection
        detections = self.person_detector.detect_person(frame)

        rects = []
        for detection in detections:
            x1, y1, x2, y2 = detection["bbox"]
            rects.append([x1, y1, x2, y2])

        # Face Detection
        faces = self.face_detector.detect_faces(frame)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Tracking
        tracked_objects = self.tracker.update(rects)

        frame = draw_boxes(frame, tracked_objects)

        # Alerts
        alert_sent = False
        total_persons = len(detections)

        if total_persons > 0:
            alert_sent = self.alert_service.send_alert(total_persons)

        # Snapshot
        if alert_sent:
            self.snapshot_service.save_snapshot(frame)

        return frame

    def stop(self):
        self.video_stream.stop_stream()




