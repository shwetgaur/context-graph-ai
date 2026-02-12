from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import ollama
from context_graph import ContextGraph

# ---------- STATE ----------
class ChatState(TypedDict):
    messages: List[dict]
    user_input: str


# ---------- GRAPH ----------
cg = ContextGraph()

cg.add_user("student_1", "student")
cg.add_goal("ml_assignment", "Finish ML assignment")
cg.link_user_goal("student_1", "ml_assignment")
cg.add_deadline("ml_assignment", "Friday")
cg.set_screen("student_1", "assignment_page")


# ---------- FUNCTIONS ----------

def build_context(state: ChatState):
    context = cg.get_user_context("student_1")

    context_text = "Context:\n"
    for node, relation in context.items():
        context_text += f"{relation}: {node}\n"

    state["messages"].append({
        "role": "system",
        "content": context_text
    })

    return state


def call_llm(state: ChatState):
    response = ollama.chat(
        model="mistral",
        messages=state["messages"]
    )

    reply = response["message"]["content"]

    state["messages"].append({
        "role": "assistant",
        "content": reply
    })

    print("\nAI:", reply)
    return state


# ---------- BUILD GRAPH ----------
workflow = StateGraph(ChatState)

workflow.add_node("context", build_context)
workflow.add_node("llm", call_llm)

workflow.set_entry_point("context")
workflow.add_edge("context", "llm")
workflow.add_edge("llm", END)

app = workflow.compile()


# ---------- RUN ----------
if __name__ == "__main__":
    print("LangGraph chatbot. Type exit to stop.\n")

    messages = []

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        state = {
            "messages": messages,
            "user_input": user_input
        }

        app.invoke(state)
