import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from decimal import Decimal

load_dotenv()

def get_db_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        row_factory=dict_row,
    )

app = FastAPI()

@app.get("/")

def root():
    return {
    "name": "Job Tracker",
    "version": "1.0"
}

class Job(BaseModel):
    company: str
    job_title: str
    status: str = "Saved"
    location: str
    salary_min: Decimal = 0.00
    salary_max: Decimal = 0.00
    url: str = ""
    date_applied: date | None = None
    notes: str = ""
    interview_date: date | None = None

class JobUpdate(BaseModel):
    company: str | None = None
    job_title: str | None = None
    status: str | None = None
    location: str | None = None
    salary_min: Decimal | None = None
    salary_max: Decimal | None = None
    url: str | None = None
    date_applied: date | None = None
    notes: str | None = None
    interview_date: date | None = None

@app.post("/jobs")

def jobs(job: Job):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO jobs (company, job_title, status, location)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (
                    job.company,
                    job.job_title,
                    job.status,
                    job.location,
                ),
            )
            new_id = cur.fetchone()[0]
    return {"id": new_id, **job.model_dump()}

@app.get("/jobs")
def get_jobs():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM jobs ORDER BY id")
            jobs = cur.fetchall()
    return jobs

@app.patch("/jobs/{job_id}")
def update_job(job_id: int, updates: JobUpdate):
    changes = updates.model_dump(exclude_unset=True)
    return {"job_id": job_id, "changes": changes}