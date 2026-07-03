

from app.services.alert_service import AlertService

def test_can_send_alert():
    alert_service = AlertService()
    assert alert_service.can_send_alert() is True