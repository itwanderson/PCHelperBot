import requests

def ask_llm(context, question):
    prompt = f"""You are a PC troubleshooting assistant.
Answer ONLY based on the following manuals and instructions.
If you don't know, say you don't know.

Context:
{context}

Question:
{question}
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]
