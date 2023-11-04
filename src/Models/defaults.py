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
        website="https://www.christopherarnold.au/",
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
            subset=["Pandas", "NumPy", "SciPy", "Pydantic", "FastAPI", "Django"],
        ),
        Skill(name="SQL", level="Intermediate", subset=None),
        Skill(name="Git", level="Intermediate", subset=["GitLab", "GitHub"]),
        Skill(name="Bash", level="Basic", subset=None),
        Skill(name="CSS", level="Intermediate", subset=None),
        Skill(name="HTML", level="Intermediate", subset=None),
        Skill(name="VBA", level="Basic", subset=None),
        Skill(name="C#", level="Basic", subset=None),
    ]
    platforms: List[Skill] = [
        Skill(name="Bloomberg Terminal", level="Advanced", subset=None),
        Skill(name="Refinitiv Eikon", level="Advanced", subset=None),
        Skill(name="GitLab", level="Intermediate", subset=None),
        Skill(name="GitHub", level="Intermediate", subset=None),
        Skill(name="Rundeck", level="Intermediate", subset=None),
        Skill(name="JupyterHub", level="Intermediate", subset=None),
        Skill(name="Amazon Web Service", level="Basic", subset=["Lambda"]),
        Skill(name="Google Cloud Platform", level="Basic", subset=None),
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
            title="Associate",
            division="Fixed Income Index Management",
            company="Solactive AG",
            location="Berlin, Germany",
            start=dt.date(year=2023, month=2, day=1),
            finish="Current",
            responsibilities=[
                "Developed and maintained Python based fixed income quantitative libraries, as well as supporting libraries.",
                "Responsible for delegating and executing peer reviews on over 40 cross-team production repositories, focusing specifically on newly developed index models, to ensure optimal quality and alignment to standards.",
                "Managed the ongoing model optimization and client relations for more than 20 indices linked to fixed income funds and ETFs.",
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
                "Developed automated calculation and data validation process using Python, SQL, APIs, and Bash, amplifying team responsiveness in detecting anomalies while delivering an average cumulative daily timesaving of 2 hours.",
                "Implemented existing index production models into Python from VBA.",
                "Assisting colleagues with technical queries and bugfixes on Python, Git, and Object-Orientated Programming topics.",
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
                "Coordinated a multi-asset class index tender linked to £23.1B in assets under management.",
                "Responsible for calculating index performance statistics for clients, including historical performance, correlation, and tracking error.",
            ],
        ),
        Experience(
            title="Intern",
            division="Investment Management",
            company="Oreana Financial Services",
            location="Hong Kong, Hong Kong",
            start=dt.date(year=2019, month=10, day=1),
            finish=dt.date(year=2019, month=12, day=31),
            responsibilities=[
                "Developed a model to forecast total returns for the United States Investment Grade and High Yield corporate bond market.",
                "Researched and delivered concise daily summaries to the Chief Investment Officer and Investment Team on current economic and financial events occurring across the European region.",
            ],
        ),
    ]


class CandidateInterests(BaseModel):
    interests: List[Interest] = [
        Interest(name="Photography"),
        Interest(name="Surfing"),
        Interest(name="Field Hockey"),
    ]
