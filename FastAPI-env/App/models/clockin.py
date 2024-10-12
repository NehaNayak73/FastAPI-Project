from pydantic import BaseModel
from datetime import datetime

class  ClockInRecord(BaseModel):
    email: str
    location: str
    insert_datetime: datetime = None  # Ensure this is included
