

import os
from openai import OpenAI
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

# --- Setup OpenAI API ---
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# --- Load documents ---
docs = []
for filename in os.listdir("documents"):
    path = os.path.join("documents", filename)
    if filename.endswith(".pdf"):
        docs.extend(PyPDFLoader(path).load())
    elif filename.endswith(".txt"):
        docs.extend(TextLoader(path).load())

# --- Split into chunks ---
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = splitter.split_documents(docs)

# --- Create vectorstore ---
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(splits, embeddings, persist_directory="db")

# --- Build chatbot with memory ---
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0),
    retriever=vectorstore.as_retriever(),
)

chat_history = []

print("Your AI is ready! Type 'exit' to quit.")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    result = qa_chain({"question": query, "chat_history": chat_history})
    print("AI:", result["answer"])
    chat_history.append((query, result["answer"]))
