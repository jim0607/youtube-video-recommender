import run_backend
import sqlite3 as sql

if __name__ == '__main__':
    with sql.connect(run_backend.db_name) as conn:
        cursor = conn.cursor()
        # create table
        cursor.execute("CREATE TABLE videos (title text, video_id text, score real)")
        conn.commit()
    run_backend.update_db()