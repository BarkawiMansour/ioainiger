from pydantic import BaseModel
from typing import Optional

class Candidate(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    phone: str
    email: Optional[str] = ""
    category: str
    token: str
    date: str

class Token(BaseModel):
    id: Optional[int]
    token: str
    used: bool = False
