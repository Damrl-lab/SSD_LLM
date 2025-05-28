import openai
import gptAPI.api_call as api_call
import gptAPI.prompt as prompt
import RAG.retrieval as ret

def main(api_key: str, query: str, top_k: int):
    # set the key
    openai.api_key = api_key

    # 1) Retrieval
    hits = ret.retrieve(api_key, query, k=top_k)
    retrieved_data = ""
    for i, h in enumerate(hits, 1):
        print(f"=== Result {i} (L2 distance {h['score']:.4f}) ===\n{h['text']}\n")
        retrieved_data += i

    # 2) GPT-4 completion
    response = api_call.gpt4_response(prompt.prompt, api_key, retrieved_data, query)
    print("=== GPT-4 Response ===")
    print(response)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Retrieve similar passages via FAISS RAG and then ask GPT-4 for a response."
    )
    parser.add_argument(
        "--api-key", "-k",
        required=True,
        help="Your OpenAI API key"
    )
    parser.add_argument(
        "--query", "-q",
        required=True,
        help="The user query to retrieve against the document"
    )
    parser.add_argument(
        "--top-k", "-n",
        type=int,
        default=3,
        help="How many similar passages to retrieve (default: 3)"
    )

    args = parser.parse_args()
    main(api_key=args.api_key, query=args.query, top_k=args.top_k)

"""
python main.py \
  --api-key sk-…YOUR_KEY… \
  --query "How does ..." \
  --top-k 2
"""
