import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

DATA_DIR = "Data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    print(f"📁 '{DATA_DIR}' naam ka folder nahi mila tha, isliye maine naya bana diya hai.")
    print("👉 ABHI IS STEP PAR RUKIEN: Pehle is 'Data' folder ke andar apni medical PDFs copy karein, phir is file ko dobara chalaein!")

else:
    if not os.listdir(DATA_DIR):
        print(f"⚠️ '{DATA_DIR}' folder toh mil gaya hai, lekin yeh bilkul KHALI (empty) hai!")
        print("👉 Is folder ke andar apni PDF files rakhein taaki code unhe read kar sake.")
    else:
        print("🔄 PDFs load ho rahi hain, thoda intezar karein...")

        def load_pdf_file(data_path):
            loader = DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
            return loader.load()

        extracted_data = load_pdf_file(DATA_DIR)
        print(f"✅ PDFs successfully load ho gayeen! Total documents/pages: {len(extracted_data)}")

        def text_split(data):
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
            return text_splitter.split_documents(data)

        text_chunks = text_split(extracted_data)
        print("✅ Length of Text Chunks:", len(text_chunks))

        print("📥 Hugging Face Embeddings model download/load ho raha hai...")
        def download_hugging_face_embeddings():
            return HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

        embeddings = download_hugging_face_embeddings()

        query_result = embeddings.embed_query("Hello world")
        print("✅ Embedding Dimension Length:", len(query_result))

        print("🧠 FAISS Vector Database ban raha hai aur chunks embed ho rahe hain...")
        db = FAISS.from_documents(text_chunks, embeddings)

        db.save_local("faiss_medical_db")
        print("\n🎉 MUBARAK HO! FAISS Database successfully ban gaya aur 'faiss_medical_db' ke naam se save ho gaya!")