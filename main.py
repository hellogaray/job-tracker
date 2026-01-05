import os
import psycopg
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

@app.post("/jobs")
def jobs(job: Job):
    return job

