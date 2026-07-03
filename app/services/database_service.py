

import sqlite3
from app.core.config import settings

class DatabaseService:
    def __init__(self):
        self.db_path = settings.DB_NAME
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT,
                total_people INTEGER,
                timestamp TEXT NOT NULL,
                alert_type TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.conn.commit()

    def insert_alert(self, event_type, total_people, timestamp, alert_type, description=None):
        self.cursor.execute('''
            INSERT INTO alerts (event_type, total_people, timestamp, alert_type, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (event_type, total_people, timestamp, alert_type, description))
        self.conn.commit()

    

    # def get_all_alerts(self):
    #     self.cursor.execute('SELECT * FROM alerts')
    #     return self.cursor.fetchall()

    def get_alerts_as_dict(self):
        self.cursor.execute('SELECT * FROM alerts')
        rows = self.cursor.fetchall()
        alerts = []
        for row in rows:
            alert = {
                "id": row[0],
                "event_type": row[1],
                "total_people": row[2],
                "timestamp": row[3],
                "alert_type": row[4],
                "description": row[5]
            }
            alerts.append(alert)
        return alerts
    
    def get_total_alerts(self):

        self.cursor.execute("SELECT COUNT(*) FROM alerts")
        return self.cursor.fetchone()[0]

    def get_latest_alerts(self, limit=5):
        self.cursor.execute(
            '''
            SELECT * FROM alerts
            ORDER BY id DESC
            LIMIT ?
            ''',
            (limit,))

        rows = self.cursor.fetchall()

        alerts = []
        for row in rows:
            alert = {
                "id": row[0],
                "event_type": row[1],
                "total_people": row[2],
                "timestamp": row[3],
                "alert_type": row[4],
                "description": row[5]
            }
            alerts.append(alert)

        return alerts
    
    def get_total_people_detected(self):

        self.cursor.execute(
            '''
            SELECT SUM(total_people)
            FROM alerts
            ''' )
        result = self.cursor.fetchone()[0]
        return result if result else 0

    def close(self):
        self.conn.close()
        self.cursor.close()

    

