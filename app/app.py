import os
from pymongo import MongoClient

def main():
    # Retrieve MongoDB connection URI from environment variable
    mongo_uri = os.environ.get("MONGODB_URI")

    if not mongo_uri:
        print("Error: MONGODB_URI environment variable is not set.")
        return

    try:
        # Connect to MongoDB
        client = MongoClient(mongo_uri)
        print("Connected to MongoDB successfully!")

        # Access a specific database
        db = client.get_database("your_database_name")

        # Access a specific collection
        collection = db.get_collection("your_collection_name")

        # Example query
        result = collection.find_one({"key": "value"})
        print(result)

    except Exception as e:
        print("Error connecting to MongoDB:", e)

if __name__ == "__main__":
    main()
