from pydantic import BaseModel, EmailStr
from typing import List, Optional

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str
    context_used: Optional[List[str]] = None
    booking_confirmation: Optional[str] = None

class BookingInfo(BaseModel):
    name: str
    email: EmailStr
    date: str  
    time: str  
