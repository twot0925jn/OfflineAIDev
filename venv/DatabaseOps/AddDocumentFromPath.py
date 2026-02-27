import ollama
import chromadb

client = chromadb.PersistentClient(path="~/AI_Resources/ChromaDB/PersistentClient/Data")
collection = client.create_collection(name="docs")

document = open("~/AI_Resources/ChromaDB/PersistentClient/Documents/demotextfile.txt")

collection.update(
    ids=["100"],
    documents=[document.read()]
)

document.close()
