

from app.services.database_service import DatabaseService

def test_total_alerts():
    db = DatabaseService()
    total = db.get_total_alerts()
    assert isinstance(total, int)