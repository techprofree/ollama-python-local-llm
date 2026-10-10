"""
04 - Multimodal (image + text)
Ask a vision-capable model to describe an image.

Run:  python 04_multimodal.py path/to/image.jpg
Needs: ollama pull gemma3:4b   (small multimodal model; llama3.2-vision also works but needs ~8 GB)
Tutorial: https://www.techprofree.com/run-llm-locally-ollama-python/
"""

import sys
import ollama

MODEL = "gemma3:4b"

if len(sys.argv) < 2:
    print("Usage: python 04_multimodal.py <image_path>")
    sys.exit(1)

image_path = sys.argv[1]

response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Describe this image in detail. What objects and text can you see?",
            "images": [image_path],  # file path or raw bytes
        }
    ],
)

print(response["message"]["content"])
