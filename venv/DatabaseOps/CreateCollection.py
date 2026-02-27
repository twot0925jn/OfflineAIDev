import chromadb

#create persistent client
client = chromadb.PersistentClient(path="~/AI_Resources/ChromaDB/PersistentClient/Data")

#get or create collection
collection = client.get_or_create_collection(name="docs")

print ("Collection ready: ", collection)

#add some documents to the collection
collection.add(
    documents=["", 
               "", 
               "",
               ""
               ],
    ids=["", "", "", ""],
    
    )

print("Data added")

#retrieve and print out the contents of the collection
data=collection.get()

print("Current data:")

for i, doc in zip(data['ids'], data['documents']):
    print(f"ID: {i}, Document: {doc}")