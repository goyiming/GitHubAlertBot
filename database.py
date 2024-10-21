import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='github_monitor.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sent_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_name TEXT,
            keyword TEXT,
            sent_at TIMESTAMP
        )
        ''')
        self.conn.commit()

    def record_sent_message(self, repo_name, keyword):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO sent_messages (repo_name, keyword, sent_at)
        VALUES (?, ?, ?)
        ''', (repo_name, keyword, datetime.now()))
        self.conn.commit()

    def get_statistics(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT 
            COUNT(*) as total_messages,
            COUNT(DISTINCT repo_name) as unique_repos,
            COUNT(DISTINCT keyword) as unique_keywords
        FROM sent_messages
        ''')
        return cursor.fetchone()

    def get_detailed_statistics(self, limit=50):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT repo_name, keyword, sent_at
        FROM sent_messages
        ORDER BY sent_at DESC
        LIMIT ?
        ''', (limit,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()
