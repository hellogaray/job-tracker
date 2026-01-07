# Job Tracker

A full-stack web application for tracking job applications, managing application statuses, and monitoring the job search process.

## Features

### Implemented
- Create job application records
- Retrieve saved job applications
- Store application data in PostgreSQL
- REST API built with FastAPI

### Planned
- Update and delete job applications
- Search and filter applications
- Track application statuses, interviews, and offers
- Dashboard with application statistics and salary metrics
- Web interface built with HTML, CSS, and JavaScript
- Automated tests with pytest

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Database driver:** Psycopg
- **Validation:** Pydantic
- **Frontend:** HTML, CSS, JavaScript (planned)
- **Testing:** pytest (planned)
- **Version control:** Git and GitHub

## Getting Started

### Prerequisites
- Python
- PostgreSQL

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/hellogaray/job-tracker.git
   cd job-tracker
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install fastapi "uvicorn[standard]" "psycopg[binary]" python-dotenv
   ```

4. Create a `.env` file in the project root:

   ```dotenv
   DB_NAME=job_tracker
   DB_USER=your_postgres_username
   DB_HOST=/tmp
   DB_PORT=5432
   ```

5. Create the PostgreSQL database and configure the `jobs` table using the project's schema.

6. Start the development server:

   ```bash
   uvicorn main:app --reload
   ```

7. Open the interactive API documentation:

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Goals

This project is an opportunity to practice REST API development, relational database design, SQL, input validation, automated testing, and frontend integration while building a practical tool for managing a job search.

## Security

- Keep `.env` out of version control.
- Never commit database credentials or other secrets.

