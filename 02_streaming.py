"""
02 - Streaming
Print the response as it is generated instead of waiting for the whole answer.
This is how chat apps show text appearing word by word.

Run:  python 02_streaming.py
Needs: ollama pull llama3.2
Tutorial: https://www.techprofree.com/run-llm-locally-ollama-python/
"""

import ollama

MODEL = "llama3.2"

stream = ollama.chat(
    model=MODEL,
    messages=[{"role": "user", "content": "Write a short poem about running AI on your own computer."}],
    stream=True,
)

for chunk in stream:
    # flush=True makes each token appear immediately
    print(chunk["message"]["content"], end="", flush=True)

print()  # final newline
