import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import os
import tempfile

st.set_page_config(page_title = "Stock Analysis with LLM", layout = "wide")
st.title("Stock Analyzer")

questions = [
    "What does this company do?",
    "Is this business understandable?",
    "Is the company profitable over the long term?",
    "Is revenue and earnings growth sustainable?",
    "Does the company generate strong free cash flow?",
    "What are the ROE and ROIC values?",
    "Does the company have a strong balance sheet?",
    "Does the company have a competitive advantage (moat)?",
    "Is management competent and aligned?",
    "What are the key risks faced by the company?",
    "Is the valuation attractive?",
    "Is there a catalyst for improved performance?"
]

uploaded_file = st.file_uploader("Uplaod an annual report (PDF)", type = ["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete = False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    with st.spinner("Reading and chunking PDF..."):
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
        docs = splitter.split_documents(pages)

    with st.spinner("Embedding and indexing..."):
        embedding = OllamaEmbeddings(model = "llama3")
        vectordb = Chroma.from_documents(documents = docs, embedding = embedding)
        retriever = vectordb.as_retriever(search_kwargs = {"k": 5})
        llm = Ollama(model = "llama3")
        qa_chain = RetrievalQA.from_chain_type(llm = llm,
        retriever = retriever)

    st.subheader("Select questions to analyze")
    selected = st.multiselect("Choose questions", questions, default = questions[0])

    if st.button("Analyze"):
        with st.spinner("Thinking..."):
            for q in selected:
                answer = qa_chain.run(q)
                st.markdown(f"**Q: {q}**")
                st.markdown(f"> {answer}\n")
