from pydantic import BaseModel, NameEmail
from typing import Optional, Union, Dict, List
import datetime as dt


class Skill(BaseModel):
    """Simple model for a skill."""

    name: str
    level: str
    subset: Optional[List[str]]


class SkillSet(BaseModel):
    """Model for a set of skills."""

    language: List[Skill]
    technical: List[Skill]
    platforms: List[Skill]


class Candidate(BaseModel):
    """The contact information of the candidate."""

    first_name: str
    last_name: str
    mobile: Dict[str, str]
    email: NameEmail
    website: str
    linkedin: str


class Experience(BaseModel):
    """Model for the experience entity."""

    title: str
    division: str
    company: str
    location: str
    start: Union[dt.date, str]
    finish: Union[dt.date, str]
    responsibilities: List[str]


class Grade(BaseModel):
    """Model for the grade entity."""

    value: Union[str, int, float]
    system: str


class Institution(BaseModel):
    """Model for the institution entity."""

    name: str
    type: str
    location: str


class Education(BaseModel):
    """Model for the education entity."""

    degree: str
    appellations: str
    major: Optional[str]
    minor: Optional[str]
    grade: Grade
    institution: Institution
    coursework: Optional[List[str]]
    start: Union[dt.date, str]
    finish: Union[dt.date, str]


class Interest(BaseModel):
    """Simple Interest model."""

    name: str


class CurriculumVitae(BaseModel):
    """A collection of Candidate Details forming a Curriculum Vitae structure."""

    contact: Candidate
    professional_experiences: List[Experience]
    education_experiences: List[Education]
    skills: SkillSet
    interests: List[Interest]
