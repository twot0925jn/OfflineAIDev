import chromadb

#create persistent client
client = chromadb.PersistentClient(path="~/AI_Resources/ChromaDB/PersistentClient/Data")

#get collection
collection =  client.get_collection(name="docs")

#query the collection
results = collection.query(
    query_texts=[""],
    n_results=1
)

#print the results
print(results)