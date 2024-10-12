from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime