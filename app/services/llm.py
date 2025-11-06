
import re
from typing import List, Optional
from dateutil.parser import parse
from app.models import BookingInfo
from app.services.memory import r 
from app.db.sql_client import save_booking as save_booking_to_db

def generate_response(user_message: str, session_id: str, context: List[str]) -> tuple[str, Optional[BookingInfo]]:

    existing_booking_json = r.get(f"{session_id}_booking")
    if "remind" in user_message.lower() and existing_booking_json:
        existing_booking = BookingInfo.parse_raw(existing_booking_json)
        return (
            f"Your booking is on {existing_booking.date} at {existing_booking.time} for {existing_booking.name}.",
            existing_booking
        )


    if "book" in user_message.lower():
        booking = extract_booking(user_message)
        if booking:
            
            save_booking_to_db(booking.name, booking.email, booking.date, booking.time)
           
            r.set(f"{session_id}_booking", booking.json())
            return f"✅ Booking confirmed for {booking.name} on {booking.date} at {booking.time}.", booking

    
    return f"Here's what I found based on context:\n{context[:1]}", None


def extract_booking(msg: str) -> Optional[BookingInfo]:

    name_match = re.search(
        r"(?:my name is|i am|i'm|this is)\s+([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)",
        msg,
        re.I
    )
    name = name_match.group(1) if name_match else None


    email_match = re.search(r"[\w\.-]+@[\w\.-]+", msg)
    email = email_match.group(0) if email_match else None


    date_match = re.search(
        r"\b(?:\d{4}-\d{2}-\d{2}|\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s+\d{4}|[A-Za-z]+\s+\d{1,2},\s+\d{4})\b",
        msg
    )
    try:
        date = parse(date_match.group(0), fuzzy=True).strftime("%Y-%m-%d") if date_match else None
    except:
        date = None

    time_match = re.search(r"\b\d{1,2}(:\d{2})?\s*(?:AM|PM|am|pm)?\b", msg)
    try:
        time = parse(time_match.group(0), fuzzy=True).strftime("%H:%M") if time_match else None
    except:
        time = None

    if all([name, email, date, time]):
        return BookingInfo(name=name, email=email, date=date, time=time)
    return None
