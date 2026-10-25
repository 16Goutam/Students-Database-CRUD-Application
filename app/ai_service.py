import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"

async def ask_student_assistant(question: str, records: list):
    context = "\n".join([
        f"- ID: {r.id}, Name: {r.name}, DOB: {r.date_of_birth}, Course: {r.course}, Email: {r.email}"
        for r in records
    ])
    
    prompt = f"""You are a helpful assistant answering queries about a student database.
Answer the user's question accurately using ONLY the records provided below.

STUDENT RECORDS:
{context}

QUESTION: {question}
ANSWER:"""

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                OLLAMA_URL,
                json={"model": "llama3.2:1b", "prompt": prompt, "stream": False}
            )
            if response.status_code == 200:
                return response.json().get("response", "No response generated.")
            return "Local Ollama service returned an error."
    except Exception:
        return "Local Ollama service is unavailable. Please ensure Ollama is running locally with 'ollama run llama3.2:1b'."