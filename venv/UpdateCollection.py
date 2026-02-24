import chromadb

#create persistent client
client = chromadb.PersistentClient(path="~/AI_Resources/ChromaDB/PersistentClient/Data")

#get collection
collection =  client.get_or_create_collection(name="vehicles")

#update a document by id
collection.update(
    ids=["car1"],
    documents=["Car runs on land and typically holds no more than 7 people"]
)

#retrieve the updated document to verify the update
record = collection.get(ids=["car1"])
print(record)