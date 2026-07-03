

from fastapi import FastAPI

from app.api.routes.alerts import router as alerts_router
from app.api.routes.health import router as health_router
from app.api.routes.detection import router as detection_router


app = FastAPI(title="AI CCTV Surveillance API")

app.include_router(alerts_router)
app.include_router(health_router)
app.include_router(detection_router)

@app.get("/")
def hone():
    return {"message": ("AI CCTV Surveillance System Running")}