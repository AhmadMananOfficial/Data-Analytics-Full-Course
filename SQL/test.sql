SELECT job_title_short AS "Job Title",
    salary_year_avg AS "Yearly Salary",
    salary_hour_avg AS "Hourly Salay"
From job_postings_fact
Limit 50;