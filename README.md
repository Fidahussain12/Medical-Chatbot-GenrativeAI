# 🏥 Medical Chatbot — End-to-End Generative AI Project

A RAG (Retrieval-Augmented Generation) based Medical Chatbot built with LangChain, FAISS, Groq LLM, and Flask.

---

## 🚀 Features

- 📄 Medical PDF se knowledge extract karta hai
- 🧠 FAISS Vector Database mein store karta hai
- 🤖 Groq LLM (Llama 3.1) se intelligent answers deta hai
- 💬 Clean Chat UI with Flask
- 🔒 API keys `.env` file mein safe hain

---

## 🛠️ Tech Stack

| Technology | Use |
|---|---|
| Python 3.10 | Core Language |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| HuggingFace Embeddings | Text Embeddings |
| Groq (Llama 3.1) | LLM |
| Flask | Web Framework |
| HTML/CSS | Frontend |

---

## 📁 Project Structure

```
Medical/
├── Data/                        # Medical PDFs yahan rakhein
│   └── Medical_book.pdf
├── faiss_medical_db/            # Auto-generate hoga
│   ├── index.faiss
│   └── index.pkl
├── src/
│   ├── __init__.py
│   ├── helper.py                # RAG Chain + Embeddings + LLM
│   ├── prompt.py                # Prompt Template
│   └── store_index.py          # FAISS Database Builder
├── static/
│   └── style.css                # Frontend Styling
├── templates/
│   └── chat.html                # Chat Interface
├── research/
│   └── trials.ipynb             # Experiments Notebook
├── .env                         # API Keys (secret)
├── .gitignore
├── app.py                       # Main Flask Application
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Step 1 — Repository Clone Karo
```bash
git clone https://github.com/Fidahussain12/Medical-Chatbot-GenrativeAI
cd medical-chatbot
```

### Step 2 — Conda Environment Banao
```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### Step 3 — Dependencies Install Karo
```bash
pip install -r requirements.txt
```

### Step 4 — `.env` File Banao
```bash
touch .env
```
`.env` file mein yeh likho:
```
GROQ_API_KEY=your_groq_api_key_here
```
> 🔑 Groq API Key free mein milti hai: [console.groq.com](https://console.groq.com)

---

## 🗄️ FAISS Database Banana (Sirf Ek Baar)

### Step 1 — Medical PDFs `Data/` folder mein rakho
```
Medical/
└── Data/
    └── your_medical_book.pdf
```

### Step 2 — Database Build Karo
```bash
python src/store_index.py
```

Expected Output:
```
🔄 PDFs load ho rahi hain...
✅ Total pages loaded: 638
✅ Total chunks: 4227
✅ Embedding Dimension: 384
🎉 FAISS Database successfully save ho gaya!
```

---

## ▶️ App Chalao

```bash
python app.py
```

Browser mein kholo:
```
http://localhost:8080
```

---

## 💬 App Use Karna

1. Browser mein `http://localhost:8080` kholo
2. Medical question type karo
3. **Send** button dabao ya **Enter** press karo
4. Chatbot PDF se jawab dhundh ke dega

**Example Questions:**
- What is diabetes?
- What are the symptoms of malaria?
- How is hypertension treated?
- What causes asthma?

---

## 📦 Requirements

`requirements.txt`:
```
flask
langchain
langchain-community
langchain-huggingface
langchain-groq
langchain-core
langchain-text-splitters
faiss-cpu
sentence-transformers
pypdf
python-dotenv
```

Install karo:
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

| Variable | Description | Kahan Se Milegi |
|---|---|---|
| `GROQ_API_KEY` | Groq LLM API Key | [console.groq.com](https://console.groq.com) |

---

## ⚠️ Important Notes

- `faiss_medical_db/` folder **sirf ek baar** banana hota hai
- Naya PDF add karne ke baad `store_index.py` **dobara chalao**
- `.env` file kabhi GitHub pe **push mat karo**
- CUDA warning ignore karo — CPU pe chal jayega

---

## 🤝 Contributing

1. Fork karo
2. Feature branch banao (`git checkout -b feature/AmazingFeature`)
3. Commit karo (`git commit -m 'Add AmazingFeature'`)
4. Push karo (`git push origin feature/AmazingFeature`)
5. Pull Request kholo

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author
Fida Hussain
Made with ❤️ using LangChain + Groq + FAISS