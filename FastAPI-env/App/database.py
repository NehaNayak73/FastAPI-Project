from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection string with embedded password
uri = "mongodb+srv://Neha:Neha45%40@cluster0.ve118.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server with ServerApi version 1
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the database (replace 'your_database' with the actual database name)
db = client['fastapi_db']
# Example: Access a collection (replace 'your_collection' with your collection name)
items_collection = db["items"]
clockin_collection = db["clock_in_records"]