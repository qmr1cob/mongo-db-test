import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import uvicorn
import asyncio

# os.environ["http_proxy"] = "http://10.143.16.65:8080"
# os.environ["https_proxy"] = "http://10.143.16.65:8080"
# os.environ["HTTP_PROXY"] = "http://10.143.16.65:8080"
# os.environ["HTTPS_PROXY"] ="http://10.143.16.65:8080"
# os.environ["NO_PROXY"] = "si0vm03536.de.bosch.com, si0vm03537.de.bosch.com, si0vm03538.de.bosch.com"
# Initialize FastAPI app
app = FastAPI()

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
print(db)
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
