

from ultralytics import YOLO
from app.core.config import settings


class PersonDetector:

    def __init__(self):

        self.model = YOLO("yolov8n.pt")

    def detect_person(self, frame):

        results = self.model(frame)
        detected_persons = []

        for result in results:
            boxes = result.boxes

            for box in boxes:
                class_id = int(box.cls[0])
                confidence_score = float(box.conf[0])

                if class_id == 0:

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    detected_persons.append({

                        "bbox": [x1, y1, x2, y2],

                        "confidence": confidence_score,

                        "class_id": class_id

                    })

        return detected_persons
