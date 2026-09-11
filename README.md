# custom-AI-Chatbot-with-memory-
this i smy assignment work in which i used LLM with memory in python

# 🤖 Custom AI Chatbot with Memory

A stateful AI Chatbot application built using **Streamlit** and the **Google Gemini API** (`google-genai` SDK). Unlike standard stateless LLM implementations, this project maintains conversation history in session state and utilizes a **Sliding Window Algorithm** to manage context limits efficiently.

---

## 🚀 Key Features

* **Stateful Context Memory:** Maintains back-and-forth chat history so the AI remembers previous user inputs.
* **Sliding Window Pruning (FIFO):** Retains only the most recent $N$ messages to prevent token budget overflow and lower latency.
* **Structural Input Validation:** Includes a validation gate to strip empty inputs and white spaces, preventing `400 Bad Request` API errors.
* **Secure API Key Handling:** Accepts the Gemini API Key via a sidebar input without hardcoding credentials in the codebase.
* **Streamlit UI:** Interactive chat interface featuring real-time response rendering.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frontend/UI:** Streamlit
* **AI Model:** Gemini 2.5 Flash (`gemini-2.5-flash`)
* **SDK:** `google-genai`

---

## 📋 Installation & Setup

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd ai-chatbot-memory
   💡 How to Test Memory
Open the local Streamlit URL in your browser (usually http://localhost:8501).

Enter your Google Gemini API Key in the sidebar.

Turn 1: Send a message providing personal context:

"My name is Annum Nisar."

Turn 2: Send a topic-unrelated prompt:

"Can you please write a short paragraph for me?"

Turn 3: Query context memory:

"Do you know my name?"

Expected Output: The AI will accurately recall your name from the session history array.

👤 Author
Annum Nisar

AI Automation & Data Science Practitioner
