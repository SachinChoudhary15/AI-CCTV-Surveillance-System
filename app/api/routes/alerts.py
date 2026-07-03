

from fastapi import APIRouter
from app.services.database_service import DatabaseService

router = APIRouter()

db_service = DatabaseService()

@router.get("/alerts")
def get_alerts():

    alerts = db_service.get_alerts_as_dict()

    return alerts