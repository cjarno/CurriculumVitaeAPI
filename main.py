from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
import datetime as dt
from loguru import logger

from src.Data import DetaDB
from src.Models import Message, CurriculumVitae
from src.Models import (
    CandidateContact,
    CandidateExperiences,
    CandidateEducation,
    CandidateInterests,
    CandidateSkillSet,
)
from src.Telegram import Telegram


app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Christopher Arnold's CV",
        version="1.0.1",
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


@app.get("/", include_in_schema=False)
def read_root():
    return {"Welcome": "This is the API for Christopher Arnold's curriculumn vitae."}


@app.get("/contact")
async def get_candidate_contact_info(candidate_id: str = "CJA") -> CandidateContact:
    """Get the contact details for the candidate."""
    candidate_cv = DetaDB().candidate_db.get(key=candidate_id)
    candidate_contact_info = CandidateContact(**candidate_cv)
    return candidate_contact_info.model_dump(mode="json")


@app.get("/experience")
async def get_candidate_experience(candidate_id: str = "CJA") -> CandidateExperiences:
    """Get details regarding the professional experience of the candidate."""
    candidate_cv = DetaDB().candidate_db.get(key=candidate_id)
    candidate_experience = CandidateExperiences(**candidate_cv)
    return candidate_experience.model_dump(mode="json")


@app.get("/education")
async def get_candidate_education(candidate_id: str = "CJA") -> CandidateEducation:
    """Get the education details for the candidate."""
    candidate_cv = DetaDB().candidate_db.get(key=candidate_id)
    candidate_education = CandidateEducation(**candidate_cv)
    return candidate_education.model_dump(mode="json")


@app.get("/skills")
async def get_candidate_skills(candidate_id: str = "CJA") -> CandidateSkillSet:
    """Get details regarding the skillset of the candidate."""
    candidate_cv = DetaDB().candidate_db.get(key=candidate_id)
    candidate_skills = CandidateSkillSet(**candidate_cv)
    return candidate_skills.model_dump(mode="json")


@app.get("/interests")
async def get_candidate_interests(candidate_id: str = "CJA") -> CandidateInterests:
    """Get the interests for the candidate."""
    candidate_cv = DetaDB().candidate_db.get(key=candidate_id)
    candidate_interests = CandidateInterests(**candidate_cv)
    return candidate_interests.model_dump(mode="json")


@app.get("/full")
async def get_candidate_curriculum_vitae(candidate_id: str = "CJA") -> CurriculumVitae:
    """Get the full Curriculumn Vitae for the candidate."""
    candidate_cv = DetaDB().candidate_db.get(key=candidate_id)
    candidate_cv = CurriculumVitae(**candidate_cv)
    return candidate_cv.model_dump(mode="json")


@app.post("/message")
async def send_a_message_to_candidate_via_telegram(mes: Message) -> dict:
    """Send a message directly to the candidate."""
    message_payload = dict(
        full_name=mes.full_name,
        email=mes.email.email,
        mobile=mes.mobile,
        company=mes.company,
        message=mes.message,
    )
    message_payload = {
        "timestamp": dt.datetime.now().strftime("%Y%m%d%H%M%S%Z%f"),
        **message_payload,
    }

    db_response = DetaDB().message_db.put(message_payload)

    telegram_response = Telegram(
        auth_key=DetaDB().admin_db.get(key="TELEGRAM_BOT_KEY").get("value"),
        group_id=DetaDB().admin_db.get(key="TELEGRAM_BOT_GROUP_ID").get("value"),
    ).send_message(payload=message_payload)
    if telegram_response.status_code != 200:
        logger.critical(telegram_response)
        raise HTTPException(status_code=404, detail="The Message could not be sent!")

    return {"response": "Message Sent."}
