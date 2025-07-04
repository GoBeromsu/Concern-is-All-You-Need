import openai
from typing import Any, Dict

COMMIT_TYPES = [
    "docs",
    "test",
    "cicd",
    "build",
    "style",
    "refactor",
    "feat",
    "fix",
]

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "types": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": COMMIT_TYPES,
            },
        },
        "count": {"type": "integer"},
        "reason": {"type": "string"},
    },
    "required": ["types", "count", "reason"],
    "additionalProperties": False,
}

STRUCTURED_OUTPUT_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "commit_classification_response",
        "schema": RESPONSE_SCHEMA,
        "strict": True,
    },
}


def openai_api_call(
    api_key: str,
    diff: str,
    system_prompt: str,
    model: str = "gpt-4.1-2025-04-14",  # State of art openai model https://platform.openai.com/docs/models/gpt-4.1
    temperature: float = 0.0,  # for greedy decoding to remove potential randomness
) -> str:
    client = openai.OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": diff},
            ],
            temperature=temperature,
            response_format=STRUCTURED_OUTPUT_FORMAT,
        )
        return response.choices[0].message.content or "No response from API."
    except openai.APIError as e:
        return f"An OpenAI API error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
