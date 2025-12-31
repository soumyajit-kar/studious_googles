📖 Studious Googles
Studious Googles is a lightweight, AI-powered document assistant designed to help you interact with your PDFs. Instead of scrolling through hundreds of pages to find a specific detail, you can simply upload your file and start a conversation with it.

Whether it's a dense research paper, a legal contract, or a textbook, Studious Googles uses the power of Google's Gemini API and Vector Search to give you precise, context-aware answers in seconds.

🚀 Features
Instant Document Parsing: Upload any PDF and let the app digest the information for you.

Contextual Intelligence: It doesn't just look for keywords; it understands the meaning of your questions using semantic search.

Privacy-First Retrieval: Only the relevant parts of your document are sent to the AI to generate an answer.

Clean UI: A simple, user-friendly interface built with Streamlit.

🛠️ The Tech Stack
This project leverages a modern RAG (Retrieval-Augmented Generation) architecture:

Streamlit: For the interactive web interface.

LangChain: The framework orchestrating the flow between the document and the AI.

Google Gemini API: The large language model (LLM) providing the "brain" for natural language generation.

FAISS: A high-performance vector database used to store and retrieve document embeddings.

PyPDF: For robust PDF text extraction.

⚙️ How It Works
Load: You upload your PDF.

Split: The app breaks the text into small, manageable "chunks."

Embed: These chunks are converted into mathematical vectors.

Store: The vectors are saved in a local FAISS index.

Query: When you ask a question, the app finds the most relevant chunks and sends them to Gemini to synthesize a human-like response.

🚦 Getting Started
Prerequisites
Python 3.8+

A Google AI (Gemini) API Key

Installation
Clone the repo:

Bash

git clone https://github.com/yourusername/studious-googles.git
cd studious-googles
Install dependencies:

Bash

pip install -r requirements.txt
Set up your environment: Create a .env file in the root directory and add your API key:

Code snippet

GOOGLE_API_KEY=your_actual_api_key_here
Run the app:

Bash

streamlit run app.py
💡 Use Cases
Students: Summarize chapters or ask specific questions about lecture notes.

Professionals: Quickly extract terms from long business reports or manuals.

Researchers: Find specific citations or data points across multiple papers.
