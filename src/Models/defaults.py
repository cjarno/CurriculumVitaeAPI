from pydantic import BaseModel
from typing import List
import datetime as dt

from src.Models import (
    Candidate,
    Skill,
    Education,
    Institution,
    Grade,
    Experience,
    Interest,
)


class CandidateContact(BaseModel):
    """The contact information of the candidate."""

    contact: Candidate = Candidate(
        first_name="Christopher",
        last_name="Arnold",
        mobile=dict(AU="+61 403 934 257", DE="+49 1573 8186 550"),
        email="cjarnold93@gmail.com",
        website="https://christopherarnold.au/",
        linkedin="https://www.linkedin.com/in/cjarno/",
    )


class CandidateSkillSet(BaseModel):
    """Details regarding the candidates current skill set."""

    language: List[Skill] = [
        Skill(name="English", level="Native", subset=None),
        Skill(name="German", level="A2", subset=None),
    ]
    technical: List[Skill] = [
        Skill(
            name="Python",
            level="Proficient",
            subset=["Pandas", "NumPy", "SciPy", "Pydantic", "FastAPI", "Django", "pytest"],
        ),
        Skill(name="SQL", level="Intermediate", subset=None),
        Skill(name="Git", level="Intermediate", subset=["GitLab", "GitHub"]),
        Skill(name="Bash", level="Basic", subset=None),
        Skill(name="CSS", level="Intermediate", subset=None),
        Skill(name="HTML", level="Intermediate", subset=None),
        Skill(name="VBA", level="Basic", subset=None),
    ]
    platforms: List[Skill] = [
        Skill(name="Bloomberg", level="Advanced", subset=None),
        Skill(name="Refinitiv", level="Advanced", subset=None),
        Skill(name="Factset", level="Advanced", subset=None),
        Skill(name="GitLab", level="Intermediate", subset=None),
        Skill(name="GitHub", level="Intermediate", subset=None),
        Skill(name="Rundeck", level="Intermediate", subset=None),
        Skill(name="Artifactory", level="Intermediate", subset=None),
        Skill(name="JupyterHub", level="Intermediate", subset=None),
        Skill(name="AWS", level="Basic", subset=["Lambda"]),
        Skill(name="Jira", level="Advanced", subset=None),
        Skill(name="DigitalOcean", level="Basic", subset=["Droplets"]),
    ]


class CandidateEducation(BaseModel):
    """Details regarding the education history of the candidate."""

    education_experience: List[Education] = [
        Education(
            degree="Master of Professional Accounting and Finance",
            appellations="MPAF",
            major=None,
            minor=None,
            grade=Grade(
                value=78.375,
                system="Weighted Average Mark",
            ),
            institution=Institution(
                name="Deakin University",
                type="University",
                location="Melbourne, Australia",
            ),
            coursework=[
                "Investments and Portfolio Management",
                "Modelling Techniques for Finance",
                "Analytical Methods",
                "Applied Corporate Finance",
                "Financial Markets",
                "Economics for Managers",
                "Finance",
                "Advanced Accounting Principles and Practice",
                "Financial Accounting",
                "Governance and Fraud",
                "Principles of Income Tax Law",
            ],
            start=dt.date(year=2019, month=2, day=1),
            finish=dt.date(year=2021, month=2, day=1),
        ),
        Education(
            degree="Bachelor of Business",
            appellations="BBusMgt",
            major="Management",
            minor="Psychology",
            grade=Grade(
                value=68.8,
                system="Weighted Average Mark",
            ),
            institution=Institution(
                name="Edith Cowan University",
                type="University",
                location="Perth, Australia",
            ),
            coursework=None,
            start=dt.date(year=2011, month=2, day=1),
            finish=dt.date(year=2014, month=11, day=30),
        ),
    ]


class CandidateExperiences(BaseModel):
    """Details regarding the professional history of the candidate."""

    professional_experience: List[Experience] = [
        Experience(
            title="Senior Associate",
            division="Fixed Income Index Management",
            company="Solactive AG",
            location="Berlin, Germany",
            start=dt.date(year=2025, month=2, day=1),
            finish="Current",
            responsibilities=[
                "Directed the design, development, and release of 10 Python packages for models covering 621 published indices, streamlining data handling, selection, weighting, and reporting to enhance development efficiency, maintainability, and extensibility.",
                "Managed and performed code reviews across 116 index production repositories, which benchmark €39.9B in assets, fostering a positive review culture and ensuring high code quality by enforcing OOP principles, PEP8 standards, and internal guidelines.",
                "Spearheaded the department-wide migration of the production environment from local machines to a cloud- based Rundeck instance with Docker and Poetry, automating image builds and publishing to Artifactory via Gitlab CI/CD pipelines, enhanced by pytest, mypy, black, and SonarQube for testing and code quality."
            ],
        ),
        Experience(
            title="Associate",
            division="Fixed Income Index Management",
            company="Solactive AG",
            location="Berlin, Germany",
            start=dt.date(year=2023, month=2, day=1),
            finish=dt.date(year=2025, month=2, day=1),
            responsibilities=[
                "Developed automated daily calculation, data validation, and reporting processes with Python, SQL, and Bash, resulting in increased team responsiveness in detecting anomalies and a cumulative time-saving of 2 hours daily.",
                "Mentored colleagues on Python, Git, and OOP topics, providing guidance and resolving technical challenges.",
            ],
        ),
        Experience(
            title="Analyst",
            division="Fixed Income Index Management",
            company="Solactive AG",
            location="Berlin, Germany",
            start=dt.date(year=2021, month=9, day=1),
            finish=dt.date(year=2023, month=1, day=31),
            responsibilities=[
                "Converted 6 legacy VBA/Excel index models to Python, slashing rebalance time by 87.5%, driving team-wide adoption as a proven pilot.",
                "Enhanced the Python codebase for 27 index products as well as implementing unit and regression tests to ensure accuracy and consistency.",
            ],
        ),
        Experience(
            title="Intern",
            division="Institutional Sales",
            company="Solactive AG",
            location="Frankfurt, Germany",
            start=dt.date(year=2021, month=2, day=1),
            finish=dt.date(year=2021, month=8, day=31),
            responsibilities=[
                "Computed financial metrics (historical returns, tracking error, Sharpe ratio) of multi-asset indices for institutional clients.",
            ],
        ),
        Experience(
            title="Intern",
            division="Investment Management",
            company="Oreana Financial Services",
            location="Hong Kong, Hong Kong",
            start=dt.date(year=2019, month=11, day=1),
            finish=dt.date(year=2019, month=12, day=31),
            responsibilities=[
                "Delivered daily briefings for the CIO and Investment Team, distilling European economic and financial events into concise, actionable updates.",
            ],
        ),
    ]


class CandidateInterests(BaseModel):
    interests: List[Interest] = [
        Interest(name="Photography"),
        Interest(name="Surfing"),
        Interest(name="Field Hockey"),
    ]
