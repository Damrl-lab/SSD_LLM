import os
import pickle
import openai
import tiktoken

# 1) set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 2) load the raw text
def load_document(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# 3) chunk into ≈500-token pieces
def chunk_text(text: str, model="text-embedding-ada-002", max_tokens=500):
    encoder = tiktoken.encoding_for_model(model)
    tokens = encoder.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = encoder.decode(tokens[i : i + max_tokens])
        chunks.append(chunk)
    return chunks

# 4) call OpenAI to embed each chunk
def embed_chunks(chunks, model="text-embedding-ada-002"):
    embeddings = []
    for chunk in chunks:
        resp = openai.Embedding.create(input=chunk, model=model)
        embeddings.append(resp["data"][0]["embedding"])
    return embeddings

if __name__ == "__main__":
    doc = load_document("your_document.txt")
    chunks = chunk_text(doc)
    embeddings = embed_chunks(chunks)

    # 5) persist for later
    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    with open("embeddings.pkl", "wb") as f:
        pickle.dump(embeddings, f)

    print(f"Created {len(chunks)} embeddings and saved to disk.")