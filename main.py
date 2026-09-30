from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from decimal import Decimal

app = FastAPI()
@app.get("/")

def root():
    return {
    "name": "Job Tracker",
    "version": "1.0"
}

class Job(BaseModel):
    id: int
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

CREATE TABLE jobs (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    company text NOT NULL,
    job_title text NOT NULL,
    status text NOT NULL,
    location text NOT NULL,
    salary_min DEC CHECK (salary_min >= 0),
    salary_max DEC CHECK (salary_max >= 0),
    url text,
    date_applied DATE,
    notes text,
    interview_date DATE
);