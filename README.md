# 🚀 AI Resume Analyzer

An AI-powered resume analyzer built with **Streamlit**, **LangChain**, and **Google Gemini**. Upload a PDF resume and ask questions about it — the app uses RAG (Retrieval-Augmented Generation) to extract insights, highlight strengths, identify missing skills, and offer actionable suggestions.

---

## ✨ Features

- 📄 Upload any PDF resume
- 🧠 Semantic search over resume content using FAISS and HuggingFace embeddings
- 🤖 Powered by Google Gemini (`gemini-2.0-flash`) for intelligent analysis
- 💬 Ask natural language questions about the resume
- 📊 Get structured feedback: **Strengths**, **Missing Skills**, and **Suggestions**

---

## 🛠️ Tech Stack

| Layer        | Technology                                      |
|--------------|-------------------------------------------------|
| UI           | [Streamlit](https://streamlit.io/)              |
| PDF Parsing  | LangChain `PyPDFLoader`                         |
| Chunking     | LangChain `RecursiveCharacterTextSplitter`      |
| Embeddings   | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store | [FAISS](https://github.com/facebookresearch/faiss) |
| LLM          | [Google Gemini 2.0 Flash](https://ai.google.dev/) |

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Raghavraghav1/ResumeAnalayzerAI.git
cd ResumeAnalayzerAI
```

### 2. Install dependencies

```bash
pip install streamlit langchain-community langchain-text-splitters langchain-huggingface \
            faiss-cpu pypdf google-genai sentence-transformers
```

### 3. Set your Gemini API key

Open `rag.py` and replace the placeholder with your actual key:

```python
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")
```

> **Tip:** Use an environment variable to avoid committing secrets:
> ```python
> import os
> client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
> ```
> Then run the app with `GEMINI_API_KEY=your_key streamlit run app.py`.

Get a free API key at [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).

---

## ▶️ Usage

```bash
streamlit run app.py
```

1. Open the URL shown in your terminal (usually `http://localhost:8501`).
2. Upload a PDF resume using the file uploader.
3. Type a question in the text box, for example:
   - *"What are the candidate's key strengths?"*
   - *"What skills are missing for a data scientist role?"*
   - *"How can this resume be improved?"*
4. Click **Analyze** to get AI-generated feedback.

---

## 📁 Project Structure

```
ResumeAnalayzerAI/
├── app.py            # Streamlit frontend
├── rag.py            # RAG pipeline (PDF loading, embeddings, Gemini LLM)
├── requirements.txt  # Project dependencies
└── README.md
```

---

## 🔒 Security Note

Never commit API keys to version control. Use environment variables or a secrets manager (e.g., Streamlit's `st.secrets`) to manage credentials safely.

---

## 📄 License

This project is open-source. Feel free to use, modify, and distribute it.
