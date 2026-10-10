# Run an LLM Locally with Ollama and Python

Step-by-step Python examples for running large language models locally with [Ollama](https://ollama.com) — no API keys, no cloud costs, works offline.

📖 **Full tutorial with screenshots and error fixes:**
https://www.techprofree.com/run-llm-locally-ollama-python/

## What's inside

| File | What it does |
|------|--------------|
| `01_basic_generate.py` | Send a prompt and get a response |
| `02_streaming.py` | Stream the response word by word |
| `03_chat_loop.py` | Interactive chat with conversation memory |
| `04_multimodal.py` | Describe an image with a vision model |
| `05_openai_compatible.py` | Use Ollama through the OpenAI-compatible API |

## Quick start

1. Install Ollama from https://ollama.com/download and make sure it is running.
2. Pull a model (3B parameters, runs on 8 GB RAM, no GPU needed):
   ```bash
   ollama pull llama3.2
   ```
3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run an example:
   ```bash
   python 01_basic_generate.py
   ```

For the multimodal example you also need a vision model:
```bash
ollama pull gemma3:4b
```

## Requirements

- Python 3.9 or newer
- Ollama installed and running (`ollama serve` starts it manually if needed)
- 8 GB RAM minimum — 16 GB recommended for 7B+ models

## Common errors

Fixes for `connection refused`, `model not found`, CUDA/GPU detection and slow responses are in the
[Common errors section](https://www.techprofree.com/run-llm-locally-ollama-python/#common-errors) of the tutorial.

## License

MIT — free to use in your own projects.
