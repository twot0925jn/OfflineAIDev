import chromadb

#create persistent client
client = chromadb.PersistentClient(path="~/AI_Resources/ChromaDB/PersistentClient/Data")

#get collection
collection =  client.get_collection(name="docs")

#delete one document by id

collection.delete(ids=[""])

#retrieve stored data to verify deletion
data=collection.get()

#print remaining records
print("Remaining records:")

for i, doc in zip(data['ids'], data['documents']):
    print(f"ID: {i}, Document: {doc}")