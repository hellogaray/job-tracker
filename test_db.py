import psycopg

with psycopg.connect(
    dbname="job_tracker",
    user="hellsketch",
    host="/tmp",
    port=5432,
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT id, company, job_title, status FROM jobs ORDER BY id")

        jobs = cur.fetchall()

        for job in jobs:
            print(job)
