# Context Graph–Driven Conversational AI Assistant

## Overview

This project implements a context graph–driven conversational AI assistant for a domain-specific education SaaS platform. The system demonstrates how structured contextual memory improves the relevance, continuity, and decision-making of AI responses compared to a baseline chatbot that relies only on flat conversation history.

The assistant simulates a student-facing AI copilot that helps users manage assignments, goals, and deadlines within a learning platform.

The key objective of this project is to show how context graphs can be used to structure, persist, retrieve, and apply contextual information during conversations to produce more relevant responses.

---

## Motivation

Traditional LLM chatbots rely only on recent conversation history. This approach has several limitations:

- Context is unstructured and easily lost  
- User goals and state are not persisted  
- Responses become generic  
- Prompt size grows quickly  
- No structured memory across sessions  

To address this, modern AI systems use structured context representations such as graphs.

A context graph allows the system to:
- Store user roles and goals
- Track workflow state
- Maintain deadlines and resources
- Retrieve only relevant context
- Improve response consistency

This project demonstrates the transition from a naive baseline chatbot to a context-aware AI assistant.

---

## System Architecture

The system consists of three main components:

### 1. Baseline Chatbot
A simple conversational model that relies only on chat history.

Flow:
User message → LLM → Response

Limitations:
- No structured memory
- Forgets important details
- Generic responses

---

### 2. Context Graph Model

The context graph stores structured information about:

- User role
- User goals
- Deadlines
- Current application screen
- Conversation context

This information is stored as nodes and relationships in a graph structure.

Example graph:

![Context Graph](C:\Users\shwet\context-graph-ai\diagrams\internshi_assignment.png)


During runtime:
1. The system queries the graph
2. Retrieves relevant nodes
3. Injects structured context into the LLM prompt
4. Generates more relevant responses

This improves continuity and relevance.

---

### 3. LangGraph Orchestration

LangGraph is used to manage conversation state and workflow.

Responsibilities:
- Manage conversation state
- Retrieve context from graph
- Construct prompts dynamically
- Call the LLM
- Maintain structured flow

Workflow:

User Input  
→ Update context graph  
→ Retrieve relevant subgraph  
→ Build context prompt  
→ Call LLM  
→ Return response  

This reflects a production-style conversational AI pipeline.

---

## Tech Stack

- Python
- LangGraph
- NetworkX (context graph)
- Ollama (local LLM)
- Mistral model
- VS Code

Optional extensions:
- Vector store for semantic retrieval
- Neo4j for persistent graph storage

---

## Context Graph Design

### Nodes
- User
- Goal
- Deadline
- Screen
- Course
- Conversation

### Relationships
- HAS_GOAL
- HAS_DEADLINE
- VIEWING
- WORKING_ON

The graph stores structured data rather than raw text.

This allows efficient querying and better prompt construction.

---

## Implementation Files

### `context_graph.py`
Implements the context graph structure and operations for storing and retrieving structured user context.

### `baseline_chat.py`
A simple chatbot that relies only on conversation history and does not use structured context.

### `graph_chat.py`
Chatbot that integrates the context graph to retrieve relevant user information and generate more context-aware responses.

### `langgraph_flow.py`
Implements the LangGraph workflow for orchestrating conversation flow, context retrieval, and LLM response generation.

### `examples/demo.txt`
Contains a comparison between baseline chatbot responses and context graph–enhanced responses to demonstrate improvements in relevance and continuity.


## Baseline vs Context Graph Comparison

### Baseline Model

User: When is my assignment due?  
AI: I cannot determine the due date. Please check your syllabus.

Characteristics:
- Relies only on chat history
- No structured memory
- Generic responses

---

### Context Graph Model

User: Help me finish my assignment.  
AI: Based on your current context, you are working on an ML assignment.

User: When is it due?  
AI: Based on our current context, you are viewing an assignment page within the Machine Learning (ml_assignment) goal. The due date for your assignment should be displayed on this page. If you cannot find it, I recommend checking the assignment details or reaching out to your instructor for clarification.

Characteristics:
- Uses structured graph memory
- Tracks user workflow
- Produces more relevant responses

---


---


## Running the Project

### Install Dependencies
```bash
pip install langgraph networkx ollama
````

### Run Ollama Model

```bash
ollama run mistral
```

### Run Baseline Chatbot

```bash
python baseline_chat.py
```

### Run Context Graph Chatbot

```bash
python graph_chat.py
```

### Run LangGraph Workflow

```bash
python langgraph_flow.py
```



---

## Evaluation Notes

### Improvements Observed
- More relevant responses
- Better continuity
- Structured context usage
- Reduced prompt clutter

### Limitations
- In-memory graph only
- Single user simulation
- Limited intent detection
- No persistent storage

### Future Improvements
- Persistent graph database (Neo4j)
- Multi-user support
- Vector search integration
- Advanced intent detection
- UI integration
- Multi-tenant SaaS scaling

---

## Scaling to Production

For a multi-tenant SaaS system:

- Each user gets a separate context graph
- Graph stored in persistent DB
- Context retrieval optimized
- Role-based access control
- Streaming responses
- Tool integrations

This design can scale into a production AI copilot.

---

## Conclusion

This project demonstrates how context graphs significantly improve conversational AI systems by structuring and retrieving relevant contextual information. Compared to a baseline chatbot, the graph-driven approach produces more relevant, continuous, and context-aware responses.

The implementation showcases how graph-based memory and LangGraph orchestration can be combined to build scalable domain-specific AI assistants.

---




