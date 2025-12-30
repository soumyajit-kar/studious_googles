import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 1. Extract text from PDF
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# 2. Split text into manageable chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# 3. Create a Vector Store (FAISS) using Google Embeddings
def get_vector_store(text_chunks, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# 4. Set up the conversational chain
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "The answer is not available in the context"; don't provide a wrong answer.
    
    Context:\n {context}\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    return model, prompt_template

# 5. Handle user queries
def user_input(user_question, api_key):
    if not os.path.exists("faiss_index"):
        st.write("Please upload and process PDFs first.")
        return
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    # Load the local FAISS index
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    model, prompt_template = get_conversational_chain()
    context = "\n".join([doc.page_content for doc in docs])
    formatted_prompt = prompt_template.format(context=context, question=user_question)
    response = model.invoke(formatted_prompt)
    
    st.write("### 🤖 Response:")
    st.write(response.content)

# Streamlit UI
def main():
    st.set_page_config("PDF Reader with Gemini", page_icon="📄")
    st.header("Chat with your PDF using Gemini API")

    # --- Sidebar for Key and File Upload ---
    with st.sidebar:
        st.title("Settings")
        user_api_key = st.text_input("Enter your Google API Key", type="password")
        
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
        
        if st.button("Submit & Process"):
            if not user_api_key:
                st.error("Please provide an API Key first!")
            elif not pdf_docs:
                st.error("Please upload at least one PDF.")
            else:
                with st.spinner("Processing your documents..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks, user_api_key)
                    st.success("PDF processed successfully!")

    # --- Main Chat Area ---
    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        if not user_api_key:
            st.warning("Please enter your API Key in the sidebar to proceed.")
        else:
            user_input(user_question, user_api_key)

if __name__ == "__main__":
    main()