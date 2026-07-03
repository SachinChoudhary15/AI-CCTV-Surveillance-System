from app.services.database_service import DatabaseService
from datetime import datetime


class AnalyticsService:

    def __init__(self):
        self.db_service = DatabaseService()

    def get_total_alerts(self):
        return self.db_service.get_total_alerts()

    def get_alerts_by_type(self):
        alerts = self.db_service.get_alerts_as_dict()

        alert_counts = {}
        for alert in alerts:
            alert_type = alert['alert_type']

            if alert_type in alert_counts:
                alert_counts[alert_type] += 1

            else:
                alert_counts[alert_type] = 1

        return alert_counts

    def get_alerts_by_event_type(self):
        alerts = self.db_service.get_alerts_as_dict()

        event_type_counts = {}
        for alert in alerts:
            event_type = alert['event_type']

            if event_type in event_type_counts:
                event_type_counts[event_type] += 1

            else:
                event_type_counts[event_type] = 1

        return event_type_counts

    def get_total_people_detected(self):
        return self.db_service.get_total_people_detected()

    def get_latest_alerts(self):
        return self.db_service.get_latest_alerts()
    
    def get_todays_alerts(self):
        alerts = self.db_service.get_alerts_as_dict()
        today = datetime.now().date()
        todays_alerts = [alert for alert in alerts if datetime.strptime(alert['timestamp'], "%Y-%m-%d %H:%M:%S").date() == today]

        return todays_alerts