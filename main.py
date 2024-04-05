import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import uvicorn
import asyncio

os.environ["http_proxy"] = "http://10.143.16.65:8080"
os.environ["https_proxy"] = "http://10.143.16.65:8080"
os.environ["HTTP_PROXY"] = "http://10.143.16.65:8080"
os.environ["HTTPS_PROXY"] ="http://10.143.16.65:8080"
os.environ["NO_PROXY"] = ".de.bosch.com,.bosch.com,.cluster.local,.svc,10.140.180.0/23,10.140.214.0/24,10.140.249.0/24,10.140.250.30,10.140.254.0/24,10.40.0.0/24,127.0.0.1,169.254.169.254,192.168.0.0/17,192.168.128.0/17,api-int.de3pro.osh.ipz001.internal.bosch.cloud,etcd-0.de3pro.osh.ipz001.internal.bosch.cloud,etcd-1.de3pro.osh.ipz001.internal.bosch.cloud,etcd-2.de3pro.osh.ipz001.internal.bosch.cloud,internal.bosch.cloud,localhost,osh.ipz001.internal.bosch.cloud"
os.environ["PROXY_URL"] = "http://rb-proxy-sl.bosch.com:8080"
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
