from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from google import genai

# 🔑 Replace with your Gemini API key
client = genai.Client(api_key="API_key")


def create_qa_chain(pdf_path):

    # 📄 Load PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # ✂️ Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    # 🧠 Embeddings (LOCAL - FREE)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 📦 Store in FAISS
    db = FAISS.from_documents(chunks, embeddings)

    # 🤖 Ask function
    def ask_question(query):
        docs = db.similarity_search(query)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        You are an AI Resume Analyzer.

        Analyze the resume and return:

        - Strengths
        - Missing Skills
        - Suggestions

        Resume:
        {context}

        Question:
        {query}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    return ask_question
