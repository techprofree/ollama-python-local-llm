"""
05 - OpenAI-compatible API
Ollama exposes an OpenAI-style endpoint at http://localhost:11434/v1.
That means any code written for the OpenAI SDK can point at your local
model by changing just the base_url and api_key.

Run:  python 05_openai_compatible.py
Needs: ollama pull llama3.2   and   pip install openai
Tutorial: https://www.techprofree.com/run-llm-locally-ollama-python/
"""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required by the SDK but ignored by Ollama
)

completion = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give me three tips for learning Python faster."},
    ],
)

print(completion.choices[0].message.content)
