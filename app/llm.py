from groq import Groq


MODEL_NAME = "openai/gpt-oss-20b"


def generate_answer(
    question: str,
    context: list[str],
    api_key: str,
) -> str:
    client = Groq(api_key=api_key)

    context_text = "\n\n".join(context)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer only using the supplied resume context. "
                    "Do not invent information. "
                    "If the answer is not in the context, say so."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Question:\n{question}\n\n"
                    f"Resume context:\n{context_text}"
                ),
            },
        ],
    )

    answer = response.choices[0].message.content

    if not answer:
        raise RuntimeError("The LLM returned an empty answer.")

    return answer