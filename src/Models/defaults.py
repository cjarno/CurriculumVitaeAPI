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
            subset=["Pandas", "NumPy", "SciPy", "Pydantic", "FastAPI", "Django", "Dash"],
        ),
        Skill(name="SQL", level="Intermediate", subset=None),
        Skill(name="Git", level="Intermediate", subset=["GitLab", "GitHub"]),
        Skill(name="Bash", level="Basic", subset=None),
        Skill(name="CSS", level="Intermediate", subset=None),
        Skill(name="HTML", level="Intermediate", subset=None),
        Skill(name="VBA", level="Basic", subset=None),
    ]
    platforms: List[Skill] = [
        Skill(name="Bloomberg Terminal", level="Advanced", subset=None),
        Skill(name="Refinitiv Eikon", level="Advanced", subset=None),
        Skill(name="GitLab", level="Intermediate", subset=None),
        Skill(name="GitHub", level="Intermediate", subset=None),
        Skill(name="Rundeck", level="Intermediate", subset=None),
        Skill(name="JupyterHub", level="Intermediate", subset=None),
        Skill(name="AWS", level="Basic", subset=["Lambda"]),
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
            title="Associate",
            division="Fixed Income Index Management",
            company="Solactive AG",
            location="Berlin, Germany",
            start=dt.date(year=2023, month=2, day=1),
            finish="Current",
            responsibilities=[
                "Served as lead developer for Python based fixed income quantitative libraries, as well as supporting framework and data retrieval libraries, which are implemented in models covering more than 400 published indices.",
                "Responsible for delegating and executing peer code reviews on 109 index production repositories, with a focus on ensuring the code is of a sufficient quality and adheres to OOP and PEP8 standards.",
                "Managed the model optimisation and technical implementation in Python for more than 30 unique indices with 3 linked to fixed income funds and ETFs.",
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
                "Developed automated daily calculation and data validation processes with Python, SQL, and Bash, resulting in increased team responsiveness in detecting anomalies and a cumulative time-saving of 2 hours per day.",
                "Transitioned 6 existing index production models from VBA and Excel into Python.",
                "Assisted colleagues with various technical queries and bug fixes across Python, Git, and OOP topics.",
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
                "Coordinated a tender for a suite of multi-asset class indices linked to £23.1B in assets under management.",
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
                "Forecasted total returns using linear regression for the United States Investment Grade and High Yield corporate bond market.",
                "Researched and delivered concise daily summaries to the Chief Investment Officer and Investment Team on current economic and financial events occurring across the European region",
            ],
        ),
    ]


class CandidateInterests(BaseModel):
    interests: List[Interest] = [
        Interest(name="Photography"),
        Interest(name="Surfing"),
        Interest(name="Field Hockey"),
    ]
