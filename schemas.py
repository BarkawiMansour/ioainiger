from pydantic import BaseModel

class CandidateCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str = ""
    category: str
