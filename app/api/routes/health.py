

import cv2
from fastapi import APIRouter
from app.services.database_service import DatabaseService

router = APIRouter()
db_service = DatabaseService()

@router.get("/database-health")
def database_health_check():
    try:
        total_alerts = db_service.get_total_alerts()
        return {"status": "healthy", "total_alerts": total_alerts}
    
    except:
        return {"status": "unhealthy"}

@router.get("/camera-health")
def camera_health_check():
    camera = cv2.VideoCapture(0)
    if camera.isOpened():
        camera.release()
        return {"camera_status": "operational"}

    return {"camera_status": "unhealthy"}