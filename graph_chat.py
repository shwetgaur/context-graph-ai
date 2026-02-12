import ollama
from context_graph import ContextGraph

cg = ContextGraph()

# Initialize user context
cg.add_user("student_1", "student")
cg.add_goal("ml_assignment", "Finish ML assignment")
cg.link_user_goal("student_1", "ml_assignment")
cg.add_deadline("ml_assignment", "Friday")
cg.set_screen("student_1", "assignment_page")

chat_history = []

def build_graph_context():
    context = cg.get_user_context("student_1")

    context_text = """
You are an AI assistant inside an education platform.

Use the following structured context to answer the user.
Do NOT ignore it. Always use it when relevant.

CONTEXT:
"""

    for node, relation in context.items():
        context_text += f"{relation}: {node}\n"

    context_text += """
If the user asks about their work, deadlines, or assignments,
use this context to respond specifically.
"""

    return context_text



def graph_chat(user_input):
    chat_history.append({"role": "user", "content": user_input})

    graph_context = build_graph_context()

    messages = [
    {
        "role": "system",
        "content": graph_context
    },
    {
        "role": "system",
        "content": "You must use the context graph information in your answers."
    }
] + chat_history


    response = ollama.chat(
        model="mistral",
        messages=messages
    )

    reply = response["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})

    return reply


if __name__ == "__main__":
    print("Graph chatbot. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break

        reply = graph_chat(user_input)
        print("AI:", reply)
