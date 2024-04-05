import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import uvicorn
import asyncio
import socks

# Initialize FastAPI app
app = FastAPI()

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# SOCKS5 Proxy configuration
PROXY_HOST = os.getenv("SOCKS5_PROXY_HOST")
PROXY_PORT = os.getenv("SOCKS5_PROXY_PORT")

# Connect to MongoDB through SOCKS5 proxy
proxy = socks.socksocket()
proxy.set_proxy(socks.SOCKS5, PROXY_HOST, int(PROXY_PORT))
client = MongoClient(MONGO_URI, socket=proxy)
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
        import traceback
        traceback.print_exc()
        return JSONResponse(content={"message": f"MongoDB connection failed: {str(e)}"}, status_code=500)


# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
