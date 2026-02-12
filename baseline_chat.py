import ollama

chat_history = []

def baseline_chat(user_input):
    chat_history.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="mistral",
        messages=chat_history
    )

    reply = response["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})

    return reply


if __name__ == "__main__":
    print("Baseline chatbot. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break

        reply = baseline_chat(user_input)
        print("AI:", reply)
