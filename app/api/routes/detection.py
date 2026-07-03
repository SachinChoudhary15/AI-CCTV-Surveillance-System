

from fastapi import APIRouter

from app.detection.person_detection import PersonDetector
from app.services.video_stream import VideoStream


router = APIRouter(prefix="/detection", tags=["Detection"])

person_detector = PersonDetector()
video_stream = VideoStream()


@router.get("/status")
def detection_status():
    return { "status": "running",
             "detector": "YOLO Person Detector"
            }


@router.get("/person-count")
def get_person_count():
    frame = video_stream.get_frame()
    if frame is None:
        return {"error": "Unable to read frame"}

    detections = person_detector.detect_person(frame)

    return {"total_persons": len(detections)}