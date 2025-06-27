# 🤖 Agentic RAG System

This project implements a **Retrieval-Augmented Generation (RAG)** system using an agentic workflow. Built with **LangGraph** and **LangChain**, it demonstrates a modular and iterative approach to information retrieval and generation. The system is seeded with information on major geopolitical trade developments, specifically:

- The recent **US-China trade war**
- The **US-China trade deal**
- The upcoming **US-India trade deal**

## 🧠 Objective

To explore and implement how agent-based architectures can improve the flow and accuracy of RAG systems using intelligent control over query resolution and context relevance.

## 🛠️ Architecture Overview

The agent is composed of five interconnected nodes that collaboratively determine the most effective path to generate a contextually accurate response:

### 1. **LLM Decision Maker**
- Acts as the controller node.
- Analyzes user query and initiates the reasoning process.
- Determines whether to proceed with retrieved information or revise the query.

### 2. **Vector Data Retriever (ToolNode)**
- Interfaces with a pre-built vector store containing domain-specific documents.
- Fetches semantically relevant context chunks based on the user query.

### 3. **Grader Function**
- Evaluates the relevancy of the retrieved context to the original query.
- Based on LLM feedback:
  - `'YES'`: Proceeds to **Generator Node**.
  - `'NO'`: Redirects to **Query Rewriter Node**.

### 4. **Generator Node**
- Utilizes the approved context and original query to synthesize a final, human-like response.
- Terminates the agent loop.

### 5. **Query Rewriter Node**
- Refines and reformulates the user query for improved relevance.
- Loops the flow back to the **LLM Decision Maker** for another decision cycle.

## 🧰 Tech Stack

| Component   | Technology       |
|------------|------------------|
| Agent Flow | LangGraph        |
| LLM Tools  | LangChain        |
| Storage    | Vector Store     |
| Language Model | OpenAI / Custom |

## 📌 Use Case

This system can be adapted for domains where:
- Large, fragmented knowledge bases exist
- Precision in context extraction is critical
- Queries need adaptive reformulation (e.g., legal, trade, research)

## 🚧 Future Enhancements
- Introduce feedback loop for user corrections
- Support for multiple domain-specific corpora
- Dynamic ranking of context chunks pre-grading

## 📄 License

This repository is for research and educational purposes.

---

Happy experimenting with agentic intelligence! 🧩
