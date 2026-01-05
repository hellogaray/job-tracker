import psycopg
import os
from dotenv import load_dotenv
from main import get_db_connection

load_dotenv()

with get_db_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(
 	   "SELECT id, company, job_title, status FROM jobs WHERE company = %s ORDER BY id",
	    ("Google",)
	)
        jobs = cur.fetchall()

        for job in jobs:
            print(job)
