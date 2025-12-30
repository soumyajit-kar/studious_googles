# studious_googles
This is a simple pdf reader using gemini api which firstly read a PDF later on if you ask a question based on that it gives you a answer according to the question 


📄 studious_googles: Chat with your Documents
Ever had a 50-page PDF and only 2 minutes to find one specific detail? PDF ChatMind is a lightweight, AI-powered assistant that lets you "talk" to your PDF files. Instead of scrolling and searching, just ask a question in plain English and get an answer instantly.

✨ What it does
Instant Reading: Upload any PDF and the app processes it in seconds.

Smart Context: Uses FAISS to "remember" the content by breaking it into searchable chunks.

Natural Conversation: Powered by Google's Gemini API, it understands context and provides human-like answers based only on your document.

Clean Interface: A simple, intuitive UI built with Streamlit.

🛠️ The Tech Stack
I built this using some of the best tools in the AI ecosystem:

Streamlit: For the sleek web interface and hosting.

Gemini API: The "brain" that processes and answers your questions.

LangChain: The framework connecting our PDF data to the AI.

FAISS (CPU): Our lightning-fast vector database for storing and retrieving document chunks.

PyPDF2: To handle the heavy lifting of reading PDF text.

🚀 Getting Started
1. Clone the repository
Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Set up your environment
Create a .env file in the root directory and add your Google API Key:

Code snippet

GOOGLE_API_KEY=your_actual_api_key_here
3. Install dependencies
Bash

pip install -r requirements.txt
4. Run the app
Bash

streamlit run app.py
💡 How it works (The "Human" Version)
Upload: You drop a PDF into the sidebar.

Chunking: The app breaks the long text into small, manageable pieces (chunks) so the AI doesn't get overwhelmed.

Vectorizing: Those chunks are turned into "embeddings" (mathematical versions of text) and stored in FAISS.

Asking: When you ask a question, the app looks for the most relevant chunks in FAISS.

Answering: It sends your question + the relevant chunks to Gemini, which then writes back a clear answer for you.

🤝 Contributing
This is a side project I'm working on to make document handling easier. If you have ideas on how to make the chunking better or want to add support for multiple files, feel free to fork the repo and submit a PR!

📝 License
Distributed under the MIT License. See LICENSE for more information.
