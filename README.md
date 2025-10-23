# 🤖 LangGraph Modular AI Chat System

An end-to-end modular AI chatbot project built using **LangGraph**, **LangChain**, and **Streamlit**, integrating multiple LLMs and tools for interactive AI applications.  
This project demonstrates how to design **stateful conversational AI systems** using **industry-standard modular architecture**, with clean code organization, extendability, and deployment readiness.

---

## 🚀 Project Overview

This project marks the transition from basic LangGraph experimentation (in Jupyter notebooks) to a **complete, deployable AI application** with modular structure and frontend integration.

It includes:
- A **Streamlit frontend** for user interaction.
- **LangGraph** backend for graph-based conversational flow.
- Support for **multiple LLMs (Groq, OpenAI)**.
- **Tool-enabled agents** and dynamic chat experiences.
- Deployment-ready setup (tested and hosted on **Hugging Face Spaces**).

---

## 🧩 Features

### 1. LLM Selection
Choose between different supported frameworks:
- **Groq**
- **OpenAI**

### 2. Model Selection
If **Groq** is selected as the LLM, you can pick from:
- `openai/gpt-oss`
- `llama3.3-70b`
- `whisper-large`

### 3. API Key Input
Securely provide your API key for the selected LLM directly in the Streamlit UI.

### 4. Use Case Selection
Select your desired AI module:
- **Basic Chatbot** – A simple conversational agent.
- **Chatbot with Tools** – An enhanced chatbot that integrates external tools for advanced responses.
- *(More use cases are under active development.)*

### 5. Interactive Input Section
Type your prompts or questions directly into the chat window and receive real-time AI responses.

---

## 🧱 Project Architecture

The application follows a **modular coding approach**, making it scalable and easy to maintain.  
Each component, including graphs, nodes, and workflows, is implemented as a **separate module or class**.

### Core Sections:
- **StateGraph Management** – Defines and controls chatbot logic.
- **Nodes and Reducers** – Handle message flow and memory.
- **Frontend Integration (Streamlit)** – Provides user interaction interface.
- **Modular Project Structure** – Enables easy addition of new features or use cases.

---

## 📦 Technologies & Libraries Used

Listed in `requirements.txt`:

    langchain
    langgraph
    langchain_community
    langchain_core
    langchain_groq
    langchain_openai
    faiss-cpu
    streamlit
    tavily-python

---

## 🧠 Concepts Demonstrated

This project puts into practice many core LangGraph concepts:
- Building **Stateful Chatbots** using `StateGraph`.
- Defining **modular nodes** and **graph flows**.
- Integrating **human-in-the-loop** for interaction control.
- Combining **LangChain** tools with **LangGraph workflows**.
- Deploying **Streamlit-based AI apps** with LLM backends.

---

## 🧰 Use Cases Implemented

| Use Case | Description |
|-----------|-------------|
| **Basic Chatbot** | A simple conversational agent powered by selected LLM. |
| **Chatbot with Tools** | Integrates multiple tools to enhance the chatbot’s capabilities. |
| **AI News (Upcoming)** | A news summarization and AI content generator module (in progress). |

---

## 🖥️ Demo and Deployment

The project is fully deployable and tested on:
- **Hugging Face Spaces** (for public hosting)
- **Streamlit Cloud** (for quick internal deployment)

Each module can be extended independently, making it ideal for real-world AI agent development workflows.

---

## ⚙️ How to Run Locally

1. Create Virtual Environment

python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows

2. Install Dependencies

pip install -r requirements.txt

3. Run the Streamlit App

streamlit run app.py

4. Interact with the Chatbot
	•	Select your preferred LLM and model.
	•	Enter your API key.
	•	Choose the chatbot type.
	•	Start chatting!

⸻

