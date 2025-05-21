"""
Developer tool to update any database changes.
"""

import json
import sqlite3

data = {
    "CandidateContact": {
        "contact": {
            "first_name": "Christopher",
            "last_name": "Arnold",
            "mobile": {
                "AU": "+61 08 6555 7040",
                "DE": "+49 1573 8186 550",
            },
            "email": "cjarnold93@gmail.com",
            "website": "https://christopherarnold.au/",
            "linkedin": "https://www.linkedin.com/in/cjarno/"
        }
    },
    "CandidateSkillSet": {
        "language": [
            {"name": "English", "level": "Native", "subset": None},
            {"name": "German", "level": "A2", "subset": None}
        ],
        "technical": [
            {"name": "Python", "level": "Proficient",
             "subset": ["Pandas", "NumPy", "SciPy", "Pydantic", "FastAPI", "Django", "pytest"]},
            {"name": "SQL", "level": "Intermediate", "subset": None},
            {"name": "Excel", "level": "Proficient", "subset": None},
            {"name": "Docker", "level": "Intermediate", "subset": None},
            {"name": "Git", "level": "Intermediate", "subset": ["GitLab", "GitHub"]},
            {"name": "Bash", "level": "Basic", "subset": None},
            {"name": "CSS", "level": "Intermediate", "subset": None},
            {"name": "HTML", "level": "Intermediate", "subset": None},
            {"name": "VBA", "level": "Basic", "subset": None}
        ],
        "platforms": [
            {"name": "Bloomberg", "level": "Advanced", "subset": None},
            {"name": "Refinitiv", "level": "Advanced", "subset": None},
            {"name": "Factset", "level": "Advanced", "subset": None},
            {"name": "GitLab", "level": "Intermediate", "subset": None},
            {"name": "GitHub", "level": "Intermediate", "subset": None},
            {"name": "Rundeck", "level": "Intermediate", "subset": None},
            {"name": "JupyterHub", "level": "Intermediate", "subset": None},
            {"name": "Artifactory", "level": "Intermediate", "subset": None},
            {"name": "AWS", "level": "Basic", "subset": ["Lambda", "EC2", "S3"]},
            {"name": "Kubernetes", "level": "Intermediate", "subset": None},
            {"name": "DigitalOcean", "level": "Basic", "subset": ["Droplets"]},
            {"name": "Jira", "level": "Advanced", "subset": None},
        ]
    },
    "CandidateEducation": {
        "education_experience": [
            {
                "degree": "Master of Professional Accounting and Finance",
                "appellations": "MPAF",
                "major": "Finance",
                "minor": "Accounting",
                "grade": {"value": 78.375, "system": "Weighted Average Mark"},
                "institution": {"name": "Deakin University", "type": "University", "location": "Melbourne, Australia"},
                "coursework": [
                    "Investments and Portfolio Management", "Modelling Techniques for Finance", "Analytical Methods",
                    "Applied Corporate Finance",
                    "Financial Markets", "Economics for Managers", "Finance",
                    "Advanced Accounting Principles and Practice", "Financial Accounting",
                    "Governance and Fraud", "Principles of Income Tax Law"
                ],
                "start": "2019-02-01",
                "finish": "2021-02-01"
            },
            {
                "degree": "Bachelor of Business",
                "appellations": "BBusMgt",
                "major": "Management",
                "minor": "Psychology",
                "grade": {"value": 68.8, "system": "Weighted Average Mark"},
                "institution": {"name": "Edith Cowan University", "type": "University", "location": "Perth, Australia"},
                "coursework": None,
                "start": "2011-02-01",
                "finish": "2014-11-30"
            }
        ]
    },
    "CandidateExperiences": {
        "professional_experience": [
            {
                "title": "Senior Associate",
                "division": "Fixed Income Index Management",
                "company": "Solactive AG",
                "location": "Berlin, Germany",
                "start": "2025-02-01",
                "finish": "Current",
                "responsibilities": [
                    "Directed the design and release of 10 Python packages for financial models covering 621 published indices, streamlining data handling, selection, weighting, and reporting to provide development efficiency, maintainability, and extensibility.",
                    "Optimised index methodologies to enhance risk-adjusted returns and replicability, across indices acting as benchmark for €39.9B AuM, collaborating with portfolio managers to align holdings with fund objectives and risk constraints.",
                    "Managed and performed code reviews across 116 index production repositories, fostering a positive review culture and ensuring high quality code through enforcing OOP principles, PEP8 standards, and internal code guidelines.",
                    "Spearheaded the department-wide migration of the production environment from local machines to a cloud-based Rundeck server with Docker and Poetry, automating image builds and publishing to Artifactory via Gitlab CI/CD pipelines, enhanced by pytest, mypy, black, and SonarQube."
                ]
            },
            {
                "title": "Associate",
                "division": "Fixed Income Index Management",
                "company": "Solactive AG",
                "location": "Berlin, Germany",
                "start": "2023-02-01",
                "finish": "2025-02-01",
                "responsibilities": [
                    "Engineered a real-time financial analysis pipeline for fixed income index portfolios in Python and SQL, automating performance tracking, risk metric calculations (duration, yield), credit rating monitoring, and data validation. This enhanced team responsiveness to portfolio changes and improved turnaround time for client reporting, while providing a cumulative time-saving of 2 hours daily.",
                    "Provided expert analytical support to leading financial institutions, resolving complex inquiries related to index calculations, portfolio compositions, guideline methodologies, and corporate action events.",
                    "Mentored colleagues on Python, Git, and OOP topics, providing guidance and resolving technical challenges."
                ]
            },
            {
                "title": "Analyst",
                "division": "Fixed Income Index Management",
                "company": "Solactive AG",
                "location": "Berlin, Germany",
                "start": "2021-09-01",
                "finish": "2023-01-31",
                "responsibilities": [
                    "Converted 6 legacy VBA/Excel index models to Python, slashing rebalance time by 87.5%, and driving team-wide adoption as a proven pilot.",
                    "Enhanced the Python codebase for 27 index products as well as implementing unit and regression tests to ensure accuracy and consistency."
                ]
            },
            {
                "title": "Intern",
                "division": "Institutional Sales",
                "company": "Solactive AG",
                "location": "Frankfurt, Germany",
                "start": "2021-02-01",
                "finish": "2021-08-31",
                "responsibilities": [
                    "Computed financial metrics (historical returns, tracking error, Sharpe ratio) of multi-asset indices for institutional clients."
                ]
            },
            {
                "title": "Intern",
                "division": "Investment Team",
                "company": "Oreana Financial Services",
                "location": "Hong Kong, Hong Kong",
                "start": "2019-11-01",
                "finish": "2019-12-31",
                "responsibilities": [
                    "Delivered daily briefings for the CIO and Investment Team, distilling European economic and financial events into concise, actionable updates."
                ]
            },
        ]
    },
    "CandidateInterests": {
        "interests": [
            {"name": "Photography"},
            {"name": "Surfing"},
            {"name": "Field Hockey"}
        ]
    }
}

# Connect to SQLite database (or create it)
conn = sqlite3.connect('src/Data/candidate_data.db')
cursor = conn.cursor()

# Create table with columns for each section of the candidate data
cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
                    key TEXT PRIMARY KEY,
                    CandidateContact JSON,
                    CandidateSkillSet JSON,
                    CandidateEducation JSON,
                    CandidateExperiences JSON,
                    CandidateInterests JSON
                )''')

# Insert data into the table, storing each section in its respective column
cursor.execute('''INSERT INTO candidates 
                (key, CandidateContact, CandidateSkillSet, CandidateEducation, CandidateExperiences, CandidateInterests) 
                VALUES (?, ?, ?, ?, ?, ?)''', (
    'CJA',
    json.dumps(data['CandidateContact']),
    json.dumps(data['CandidateSkillSet']),
    json.dumps(data['CandidateEducation']),
    json.dumps(data['CandidateExperiences']),
    json.dumps(data['CandidateInterests'])
))

# Commit and close the connection
conn.commit()
conn.close()
