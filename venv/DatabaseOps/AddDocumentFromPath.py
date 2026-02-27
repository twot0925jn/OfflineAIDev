import os
import chromadb
import ollama



client = chromadb.PersistentClient(path="/home/la-applications/AI_Resources/ChromaDB/PersistentClient/Data/")
collection = client.get_collection(name="docs")

with open("/home/la-applications/AI_Resources/ChromaDB/PersistentClient/Documents/ToLoad/demotextfile.txt") as document:
    text = document.read()
    response = ollama.embed(model="minilm", input=text)
    embeddings = response["embeddings"]

    collection.add(
        ids=["101"],
        embeddings=embeddings,
        documents=[text]
    )

#Test insertion

query = "Who is the project leader and what are they like?"
print(f"Query: {query}")

# generate an embedding for the input and retrieve the most relevant doc
response = ollama.embed(
  model="minilm",
  input=query
)

results = collection.query(
  query_embeddings=response["embeddings"],
  n_results=1
)
data = results['documents'][0][0]

# generate a response combining the prompt and data we retrieved
output = ollama.generate(
 model="phi3",
 prompt=f"Using this data: {data}. Respond to this prompt: {query}"
)

print(output['response'])

os._exit(0)