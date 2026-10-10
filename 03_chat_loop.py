"""
03 - Chat loop with memory
A terminal chatbot that remembers the conversation.
Every message (yours and the model's) is appended to the history,
so the model can answer follow-up questions in context.

Run:  python 03_chat_loop.py   (type 'exit' to quit)
Needs: ollama pull llama3.2
Tutorial: https://www.techprofree.com/run-llm-locally-ollama-python/
"""

import ollama

MODEL = "llama3.2"

# The system message sets the assistant's behaviour
history = [
    {"role": "system", "content": "You are a helpful, concise assistant."}
]

print(f"Chatting with {MODEL}. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    print("AI: ", end="", flush=True)
    reply = ""
    for chunk in ollama.chat(model=MODEL, messages=history, stream=True):
        token = chunk["message"]["content"]
        reply += token
        print(token, end="", flush=True)
    print("\n")

    # Save the assistant's reply so the next turn has context
    history.append({"role": "assistant", "content": reply})
