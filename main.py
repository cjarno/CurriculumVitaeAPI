import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from typing import Any

from src.Data import CandidateDB
from src.Models import CurriculumVitae
from src.Models import (
    CandidateContact,
    CandidateExperiences,
    CandidateEducation,
    CandidateInterests,
    CandidateSkillSet,
    Candidate,
    Experience,
    Interest,
    Education,
    SkillSet
)

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Christopher Arnold's CV",
        version="1.1.0",
        summary="An API that allows you to access Christopher Arnold's Curriculum Vitae details and provides a contact endpoint.",
        description=None,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

candidate_db = CandidateDB(f'{os.getcwd()}/src/Data/candidate_data.db')
candidate_db.connect()


@app.get("/", include_in_schema=False)
def read_root():
    return {"Welcome": "This is the API for Christopher Arnold's curriculumn vitae."}


@app.get("/contact")
async def get_candidate_contact_info(candidate_id: str = "CJA") -> CandidateContact:
    """Get the contact details for the candidate."""
    candidate_contact_data = candidate_db.simple_query(table='candidates', column='CandidateContact', key=candidate_id)
    candidate_contact_model = CandidateContact(**candidate_contact_data)
    return candidate_contact_model.model_dump(mode="json")


@app.get("/experience")
async def get_candidate_experience(candidate_id: str = "CJA") -> CandidateExperiences:
    """Get details regarding the professional experience of the candidate."""
    candidate_experiences_data = candidate_db.simple_query(table='candidates', column='CandidateExperiences', key=candidate_id)
    candidate_experiences_model = CandidateExperiences(**candidate_experiences_data)
    return candidate_experiences_model.model_dump(mode="json")


@app.get("/education")
async def get_candidate_education(candidate_id: str = "CJA") -> CandidateEducation:
    """Get the education details for the candidate."""
    candidate_education_data = candidate_db.simple_query(table='candidates', column='CandidateEducation', key=candidate_id)
    candidate_education_model = CandidateEducation(**candidate_education_data)
    return candidate_education_model.model_dump(mode="json")


@app.get("/skills")
async def get_candidate_skills(candidate_id: str = "CJA") -> CandidateSkillSet:
    """Get details regarding the skillset of the candidate."""
    candidate_skills_data = candidate_db.simple_query(table='candidates', column='CandidateSkillSet', key=candidate_id)
    candidate_skills_model = CandidateSkillSet(**candidate_skills_data)
    return candidate_skills_model.model_dump(mode="json")


@app.get("/interests")
async def get_candidate_interests(candidate_id: str = "CJA") -> CandidateInterests:
    """Get the interests for the candidate."""
    candidate_interests_data = candidate_db.simple_query(table='candidates', column='CandidateInterests', key=candidate_id)
    candidate_interests_model = CandidateInterests(**candidate_interests_data)
    return candidate_interests_model.model_dump(mode="json")


@app.get("/full")
async def get_candidate_curriculum_vitae(candidate_id: str = "CJA") -> dict[str, Any]:
    """Get the full Curriculumn Vitae for the candidate."""

    contact = await get_candidate_contact_info(candidate_id=candidate_id)
    professional_experiences = await get_candidate_experience(candidate_id=candidate_id)
    education_experiences = await get_candidate_education(candidate_id=candidate_id)
    skills = await get_candidate_skills(candidate_id=candidate_id)
    interests = await get_candidate_interests(candidate_id=candidate_id)

    candidate_cv_data = dict(
        contact=Candidate(**contact['contact']),
        professional_experiences=[Experience(**exp) for exp in professional_experiences['professional_experience']],
        education_experiences=[Education(**edu) for edu in education_experiences['education_experience']],
        skills=SkillSet(**skills),
        interests=[Interest(**interest) for interest in interests['interests']],
    )
    candidate_cv_model = CurriculumVitae(**candidate_cv_data)
    return candidate_cv_model.model_dump(mode="json")
