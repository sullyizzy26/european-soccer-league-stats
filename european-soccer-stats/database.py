import os
import psycopg2

class DatabaseConnection:
        def __init__(self):
                # Connection settings come from environment variables so no
                # credentials are stored in the repo.
                self.host = os.getenv("DB_HOST", "localhost")
                self.dbname = os.getenv("DB_NAME", "soccer_db")
                self.user = os.getenv("DB_USER", "postgres")
                self.password = os.getenv("DB_PASSWORD")
                self.conn = None
        def connect(self):
                self.conn = psycopg2.connect(host = self.host, dbname = self.dbname, user = self.user, password = self.password)
                print("Connected to soccer database successfully!")
        def disconnect(self):
                if self.conn:
                        self.conn.close()
                        print("Disconnected from database!")
        def execute_query(self, sql, params = None, fetchable=True):
                cur = self.conn.cursor()
                cur.execute(sql,params)
                self.conn.commit()
                if fetchable:
                        return cur.fetchall()
