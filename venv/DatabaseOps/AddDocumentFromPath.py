import ollama
import chromadb

client = chromadb.PersistentClient(path="~/AI_Resources/ChromaDB/PersistentClient/Data")
collection = client.create_collection(name="docs")

collection.update(
    ids=["100"],
    documents=[open(path="~/AI_Resources/ChromaDB/PersistentClient/Documents/demotextfile.txt").read()]
)