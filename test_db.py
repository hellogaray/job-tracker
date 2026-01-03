import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(
	dbname=os.getenv("DB_NAME"),
	user=os.getenv("DB_USER"),
	host=os.getenv("DB_HOST"),
	port=os.getenv("DB_PORT"),
) as conn:
    with conn.cursor() as cur:
        cur.execute(
	    "SELECT id, company, job_title, status FROM jobs WHERE company = %s ORDER BY id",
	    ("Google",)
	)
        jobs = cur.fetchall()

        for job in jobs:
            print(job)
