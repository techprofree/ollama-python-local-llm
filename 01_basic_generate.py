"""
01 - Basic generation
Send a single prompt to a local model and print the full response.

Run:  python 01_basic_generate.py
Needs: ollama pull llama3.2
Tutorial: https://www.techprofree.com/run-llm-locally-ollama-python/
"""

import ollama

MODEL = "llama3.2"  # change to any model you have pulled, e.g. "mistral", "gemma3:4b"

response = ollama.generate(
    model=MODEL,
    prompt="Explain what a large language model is in two sentences.",
)

print(response["response"])
