from app.services.video_stream import VideoStream

from app.detection.person_detection import PersonDetector
from app.detection.tracker import Tracker

from app.utils.draw_boxes import draw_boxes
from app.utils.fps_counter import FPSCounter

from app.services.alert_service import AlertService
from app.services.snapshot_service import SnapshotService

from app.core.logger import Logger

import cv2
from app.detection.face_detection import FaceDetector


# Video Stream
video_stream = VideoStream()

# Logger
logger = Logger()

# Detector
person_detector = PersonDetector()

# Tracker
tracker = Tracker()

# FPS Counter
fps_counter = FPSCounter()

# Alert Service
alert_service = AlertService()

# Snapshot Service
snapshot_service = SnapshotService()

# Face Detector
face_detector = FaceDetector()
while True:

    # Read Frame
    frame = video_stream.get_frame()

    if frame is None:
        break

    # Person Detection
    detections = person_detector.detect_person(frame)

    # Store Bounding Boxes
    rects = []
    for detection in detections:

        x1, y1, x2, y2 = detection["bbox"]

        rects.append([x1, y1, x2, y2])

    # Tracking
    tracked_objects = tracker.update(rects)

    # Draw Bounding Boxes
    frame = draw_boxes(frame,tracked_objects)

    # FPS
    fps = fps_counter.update_fps()

    frame = fps_counter.draw_fps(frame,fps)

    # Alert Flag
    alert_sent = False

    # Total Persons
    total_persons = len(detections)

    # Alert Logic
    if total_persons > 0:

        logger.info(f"Total Persons: {total_persons}")
        alert_sent = False

        alert_sent = alert_service.send_alert(total_persons)
        logger.info(f"Alert Sent: {alert_sent}")

    faces = face_detector.detect_faces(frame)

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Snapshot Logic
    if alert_sent:
        logger.info("Saving Snapshot...")
        snapshot_service.save_snapshot(frame)

    # Show Frame
    video_stream.show_frame(frame)

    # Exit Key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Release Resources
video_stream.stop_stream()




