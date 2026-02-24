# AI Study Assistant 📚🤖

**AI Study Assistant** is a Streamlit web app designed to help students and professionals study PDF documents efficiently. Upload any PDF and ask questions about its content. The app uses **AI embeddings** to understand the content and return the most relevant sentences or passages.  

---

## Features

- Upload **PDF files** directly in the app.  
- Ask questions about your PDF content and get answers instantly.  
- Uses **SentenceTransformers** and **FAISS** for semantic search.  
- Simple and user-friendly interface powered by **Streamlit**.  
- Works entirely in the browser — no complex setup required.  

---

## How It Works

1. **Upload PDF** – Extracts text from all pages using `pdfplumber`.  
2. **Text Processing** – Splits text into sentences and filters out short sentences.  
3. **Embeddings** – Converts sentences into embeddings using `SentenceTransformers`.  
4. **Semantic Search** – Uses `FAISS` to find the most relevant sentences for your query.  
5. **Answer Display** – Shows the top relevant answers directly in the app.  

---

## Requirements

- Python 3.10+  
- streamlit  
- pdfplumber  
- sentence-transformers  
- faiss-cpu  
- numpy  
- torch  
- transformers  

*(All dependencies are included in `requirements.txt`.)*

---

## How to Run Locally

```bash
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
pip install -r requirements.txt
streamlit run app.py
