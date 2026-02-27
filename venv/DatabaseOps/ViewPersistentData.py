import os
import chromadb

#create persistent client
client = chromadb.PersistentClient(path="/home/la-applications/AI_Resources/ChromaDB/PersistentClient/Data")

#get collection
collection =  client.get_collection(name="docs")

#retrieve collection data
data = collection.get()

#display the data in the collection
print(f"Current data in collection '{collection.name}':")

for i, doc in zip(data['ids'], data['documents']):
        print(f"ID: {i}, Document: {doc}")

os._exit(0)