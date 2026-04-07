# 📄 RAG-Based PDF Chatbot using LLMs

An end-to-end **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask context-aware questions. The system retrieves relevant information using semantic search and generates accurate responses using a Large Language Model (LLM).

---

## 🚀 Features

* 📂 Upload and process PDF documents
* 🔍 Semantic search using vector embeddings
* 🧠 Context-aware question answering using LLM
* ⚡ Fast retrieval using vector database
* 🌐 Interactive UI built with Streamlit

---

## 🧠 Overview

Traditional chatbots rely only on pre-trained knowledge, which can lead to inaccurate or outdated answers. This project uses a **RAG architecture** to ground responses in user-provided documents.

Instead of sending the entire document to the LLM, the system retrieves only the most relevant chunks using semantic search, improving both accuracy and efficiency.

---

## 🏗️ Architecture

PDF → Chunking → Embeddings → Vector DB → Retriever → LLM → Response

---

## ⚙️ Tech Stack

* Python
* Streamlit
* LangChain
* Chroma
* Hugging Face Embeddings
* LLM API / Ollama (optional)

---

## 📂 Project Structure

```
├── app.py
├── requirements.txt
├── README.md
├── temp.pdf
```

---

## 🛠️ Installation & Setup

1. Clone the repository:

```
git clone <your-repo-link>
cd <your-repo-name>
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
streamlit run app.py
```

---

## 🔑 API Configuration

* This project uses Hugging Face API for LLM inference
* You need to provide your API key in the app

👉 Alternatively, you can run locally using Ollama (no API key required)

---

## 🔍 How It Works

1. The PDF is loaded and split into smaller chunks
2. Each chunk is converted into embeddings (vector representation)
3. Embeddings are stored in Chroma
4. User query is converted into an embedding
5. Similar chunks are retrieved using Cosine Similarity
6. Retrieved context is passed to the LLM
7. LLM generates a context-aware response

---

## 🐞 Challenges & Fixes

* Fixed Streamlit command issue (`streamlit run app.py`)
* Handled API errors and response parsing
* Tuned chunk size and overlap for better retrieval
* Improved prompt structure for accurate answers

---

## 📈 Future Improvements

* Support multiple document formats (PDF, DOCX, TXT)
* Add chat memory
* Implement hybrid search (keyword + semantic)
* Deploy on cloud (AWS / Vercel)

---

## 🎯 Use Cases

* Document-based Q&A system
* Research assistant
* Knowledge base chatbot
* Enterprise document search

---

## 📚 Key Learnings

* Understanding of RAG architecture
* Semantic search and embeddings
* Vector databases and retrieval systems
* LLM integration and prompt engineering
* Debugging real-world AI applications



This project is open-source and available under the MIT License.
