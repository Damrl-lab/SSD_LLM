import os
import pickle
import numpy as np
import faiss
import openai


# 2) load your precomputed chunks & embeddings
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)
with open("embeddings.pkl", "rb") as f:
    embs = pickle.load(f)

# 3) build a FAISS index
emb_np = np.array(embs).astype("float32")   # (N, D)
dim = emb_np.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(emb_np)

def retrieve(api_key, query: str, k: int = 5, model="text-embedding-ada-002"):
    # a) embed the query
    qresp = openai.Embedding.create(input=query, model=model)
    qemb = np.array(qresp["data"][0]["embedding"], dtype="float32")

    # b) search the FAISS index
    D, I = index.search(qemb.reshape(1, -1), k)

    # c) return the top-k chunks + distances
    results = []
    for dist, idx in zip(D[0], I[0]):
        results.append({
            "text": chunks[idx],
            "score": float(dist)
        })
    return results


