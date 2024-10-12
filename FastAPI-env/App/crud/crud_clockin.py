# crud/crud_clockin.py
from bson import ObjectId
from datetime import datetime
from App.models.clockin import ClockInRecord
from App.database import clockin_collection
from motor.motor_asyncio import AsyncIOMotorClient

# Create the MongoDB client
MONGODB_URI = "mongodb+srv://Neha:Neha45%40@cluster0.ve118.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGODB_URI)

# Access the database and collections
db = client['fastapi-db']
clockin_collection = db['clock_in_records']

async def create_clockin(clockin: ClockInRecord):
    clockin.insert_datetime = datetime.utcnow()  # Set insert datetime to current time
    result = await clockin_collection.insert_one(clockin.dict())
    return str(result.inserted_id)

async def get_clockin(clockinid: str):
    clockin = await clockin_collection.find_one({"_id": ObjectId(clockinid)})
    if clockin:
        clockin["_id"] = str(clockin["_id"])  # Convert ObjectId to string for easier JSON handling
    return clockin
    

async def filter_clockins(email: str = None, location: str = None, 
                          insert_datetime: str = None):
    query = {}
    if email:
        query['email'] = email
    if location:
        query['location'] = location
    if insert_datetime:
        query['insert_datetime'] = {'$gt': datetime.fromisoformat(insert_datetime)}

    clockins = await clockin_collection.find(query).to_list(length=100)
    return clockins

async def delete_clockin(clockin_id: str):
    result = await clockin_collection.delete_one({"_id": ObjectId(clockin_id)})
    return result.deleted_count

async def update_clockin(clockinid: str, clockin_data: dict):
    result = await clockin_collection.update_one({"_id": ObjectId(clockinid)}, {"$set": clockin_data})
    return result.modified_count

