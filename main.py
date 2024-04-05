import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from urllib.parse import urlparse
import uvicorn
import asyncio

# Initialize FastAPI app
app = FastAPI()

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Parse proxy URL from environment variable
proxy_url = os.getenv("PROXY_URL")

# If proxy URL is provided, set up proxy for MongoDB connection
if proxy_url:
    proxy_parsed = urlparse(proxy_url)
    proxy_host = proxy_parsed.hostname
    proxy_port = proxy_parsed.port
    
    # Configure MongoDB client to use proxy
    client = MongoClient(MONGO_URI, connect=False, serverSelectionTimeoutMS=20000, socketTimeoutMS=20000)
    client.address = (proxy_host, proxy_port)
else:
    # Connect to MongoDB directly without proxy
    client = MongoClient(MONGO_URI)

# Access database and collection
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Routes
@app.get('/')
def index():
    return {'data': 'Backend is running'}

@app.get("/check_mongodb_connection")
async def check_mongodb_connection():
    try:
        # Check if MongoDB is reachable
        client.server_info()
        return JSONResponse(content={"message": "MongoDB connection successful"})
    except Exception as e:
        return JSONResponse(content={"message": f"MongoDB connection failed: {str(e)}"}, status_code=500)

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
