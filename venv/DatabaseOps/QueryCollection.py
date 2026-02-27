import os
import ollama
import chromadb

#create persistent client
client = chromadb.PersistentClient(path="/home/la-applications/AI_Resources/ChromaDB/PersistentClient/Data")

#get collection
collection =  client.get_collection(name="docs")

query = "Who is the project leader?"

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