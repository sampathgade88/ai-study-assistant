import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

st.title("📚 AI Study Assistant")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    st.success("PDF Loaded Successfully!")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    embeddings = model.encode(sentences)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    query = st.text_input("Ask a question from the PDF:")

    if query:
        query_embedding = model.encode([query])
        D, I = index.search(np.array(query_embedding), k=3)

        st.subheader("📖 Answer:")
        for i in I[0]:
            if i < len(sentences):
                st.write(sentences[i])