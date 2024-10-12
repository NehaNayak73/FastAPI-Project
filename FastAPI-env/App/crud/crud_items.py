from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from datetime import datetime
from App.models.item import Item  # Assuming this is a Pydantic model for item schema
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the MongoDB client
MONGODB_URI = "mongodb+srv://Neha:Neha45%40@cluster0.ve118.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGODB_URI)

# Access the database and collections
db = client['fastapi-db']
items_collection = db['items']


# CRUD operations for items
async def create_item(item: Item):
    """Insert a new item into the items collection."""
    result = await items_collection.insert_one(item.dict())
    return str(result.inserted_id)

async def get_item(item_id: str):
    """Get an item by its ObjectId."""
    item = await items_collection.find_one({"_id": ObjectId(item_id)})
    if item:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string for easier JSON handling
    return item

async def filter_items(email=None, expiry_date=None, insert_date=None, quantity=None):
    """Filter items based on optional parameters."""
    query = {}
    if email:
        query['email'] = email
    if expiry_date:
        query['expiry_date'] = {'$gt': expiry_date}  # Find items with expiry_date greater than the provided one
    if insert_date:
        query['insert_date'] = {'$gt': insert_date}  # Find items with insert_date greater than the provided one
    if quantity is not None:
        query['quantity'] = {'$gte': quantity}  # Find items with quantity greater than or equal to the provided one
        
    items = await items_collection.find(query).to_list(length=None)
    return items

async def delete_item(item_id: str):
    """Delete an item by its ObjectId."""
    result = await items_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count

async def update_item(item_id: str, item_data: dict):
    """Update an item by its ObjectId."""
    await items_collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_data})
    return await get_item(item_id)

async def aggregate_items():
    """Aggregate items by grouping them by email and counting occurrences."""
    pipeline = [
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ]
    result = await items_collection.aggregate(pipeline).to_list(length=None)
    return result
