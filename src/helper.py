import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableMap
from langchain_core.output_parsers import StrOutputParser
from src.prompt import prompt

load_dotenv()

# -----------------------------------------------
# Embeddings
# -----------------------------------------------
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# -----------------------------------------------
# FAISS Load Karo
# -----------------------------------------------
db = FAISS.load_local(
    "faiss_medical_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# -----------------------------------------------
# Groq LLM
# -----------------------------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.4,
    api_key=os.environ.get("GROQ_API_KEY")
)

# -----------------------------------------------
# Format + Retrieve Functions
# -----------------------------------------------
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def retrieve_and_format(query):
    docs = retriever.invoke(query)
    return format_docs(docs)

# -----------------------------------------------
# RAG Chain
# -----------------------------------------------
rag_chain = (
    RunnableMap({
        "context": RunnableLambda(retrieve_and_format),
        "input": RunnablePassthrough()
    })
    | prompt
    | llm
    | StrOutputParser()
)