import pymongo

# Connect to the MongoDB server running on localhost
client = pymongo.MongoClient("mongodb://ttf1cob:T6krof-KrLrlDiBT@si0vm03536.de.bosch.com:30000,si0vm03537.de.bosch.com:30000,si0vm03538.de.bosch.com:30000/dataxpress?replicaSet=PS_Dev&tls=true&tlsCAFile=C%3A%5CUsers%5CQMR1COB%5CDownloads%5CBOSCH-CA-DE_pem_1.cer")

# Access a specific database
db = client["dataxpress"]

# Access a specific collection within that database
collection = db["test"]

# Insert a document into the collection
document = {"name": "John", "age": 30, "city": "New York"}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

# Query the collection
query = {"city": "New York"}
results = collection.find(query)
print("Query results:")
for result in results:
    print(result)
