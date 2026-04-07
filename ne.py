import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from huggingface_hub import InferenceClient
import requests

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("Ask Your PDF (HuggingFace API)")


hf_token = st.text_input("Enter Hugging Face API Key", type="password")


uploaded_file = st.file_uploader("Upload your PDF", type="pdf")


query = st.text_input("Ask a question from your document")


@st.cache_resource
def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectordb


import requests

def get_answer(vectordb, query, hf_token):
    retriever = vectordb.as_retriever(search_kwargs={"k": 2})
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question based only on the context below.

Context:
{context}

Question:
{query}
"""

    url = "https://router.huggingface.co/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3.2-1B-Instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 2000
    }

    response = requests.post(url, headers=headers, json=payload)

    #  error handling
    if response.status_code != 200:
        return f"API Error: {response.text}"

    result = response.json()

    return result["choices"][0]["message"]["content"]

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success(" PDF uploaded successfully!")

    vectordb = process_pdf("temp.pdf")

    if query and hf_token:
        with st.spinner("Thinking..."):
            response = get_answer(vectordb, query, hf_token)

        st.subheader(" Answer:")
        st.write(response)
else:
    st.info("Please upload a PDF and enter your Hugging Face API key.")
