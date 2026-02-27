import chromadb

#create persistent client
client = chromadb.PersistentClient(path="~/AI_Resources/ChromaDB/PersistentClient/Data")

#get collection
collection =  client.get_or_create_collection(name="docs")

#update a document by id
collection.update(
    ids=[""],
    documents=[""]
)

#retrieve the updated document to verify the update
record = collection.get(ids=[""])
print(record)