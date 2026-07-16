<div align="center">

# 🎥 PromptTube

### 💬 Chat with any YouTube video using its transcript

Paste a YouTube URL, ask a question, and receive AI-generated responses grounded entirely in the video's transcript.

<p align="center">
  <a href="https://github.com/aimanfazal/prompttube/stargazers">
    <img src="https://img.shields.io/github/stars/aimanfazal/prompttube?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/aimanfazal/prompttube/network/members">
    <img src="https://img.shields.io/github/forks/aimanfazal/prompttube?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/aimanfazal/prompttube/issues">
    <img src="https://img.shields.io/github/issues/aimanfazal/prompttube?style=for-the-badge" alt="Issues">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=nextdotjs">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/TailwindCSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white">
</p>

</div>

---

## 📖 Overview

PromptTube is a lightweight full-stack AI application that allows users to interact with YouTube videos through natural language.

The application extracts captions directly from YouTube videos and uses an LLM to generate answers strictly grounded in the transcript content.

Simply:

1. Paste a YouTube URL
2. Ask a question (optional)
3. Get an AI-generated answer based on the video's transcript

---

## ✨ Features

✅ YouTube transcript extraction  
✅ Natural language querying  
✅ Transcript-grounded responses  
✅ Markdown formatted output  
✅ Fast API responses via Groq  
✅ Modern dark UI built with Tailwind  
✅ Fully typed backend schemas with Pydantic  

---

## 🏗️ Architecture

```text
User Input
    ↓
Next.js Frontend
    ↓
FastAPI Backend
    ↓
YouTube Transcript API
    ↓
Prompt Construction
    ↓
Groq LLM API
    ↓
Generated Response
```

---

## 📂 Project Structure

```text
prompttube/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── schemas/
│   │   ├── services/
│   │   │   ├── youtube.py
│   │   │   └── llm.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── .env.local.example
│
└── README.md
```

---

## ⚙️ Backend Setup

### 1️⃣ Create a Virtual Environment

```bash
cd backend

py -3.12 -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

```bash
copy .env.example .env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

You can get a free API key from:

https://console.groq.com/keys

### 4️⃣ Start the Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## 🎨 Frontend Setup

### 1️⃣ Install Dependencies

```bash
cd frontend
npm install
```

### 2️⃣ Configure Environment Variables

```bash
copy .env.local.example .env.local
```

### 3️⃣ Start Development Server

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

## 🔄 Processing Flow

1. User submits a YouTube URL and optional prompt.
2. Frontend sends a request to `POST /generate`.
3. Backend extracts the video ID.
4. Transcript is fetched using `youtube-transcript-api`.
5. Prompt and transcript are merged into a single context.
6. Request is sent to Groq's OpenAI-compatible API.
7. Generated response is returned to the frontend.

---

## 🛠️ Technologies Used

<p align="center">

<img src="https://img.shields.io/badge/Next.js-black?style=for-the-badge&logo=nextdotjs">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
<img src="https://img.shields.io/badge/TailwindCSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white">
<img src="https://img.shields.io/badge/Groq-F97316?style=for-the-badge">

</p>

---

## 🚧 Limitations

Current version intentionally excludes:

- Authentication
- Persistent chat history
- Multi-video conversations
- Database storage
- Caching
- Docker deployment
- CI/CD pipelines

These are explicit non-goals for `v0.1`.

---

## 🚀 Future Improvements

- 📚 Saved conversations
- 🎥 Multi-video context support
- 📝 Study notes mode
- 📄 Report generation mode
- ❓ Quiz generation mode
- 🧠 Semantic transcript search
- ☁️ Cloud deployment

---

## 🤖 Development Process

PromptTube was built using an AI-assisted development workflow ("vibe coding") combined with manual integration, debugging, and architecture decisions.

The project involved solving issues such as:

- Breaking API changes in `youtube-transcript-api`
- Dependency conflicts between `openai` and `httpx`
- Prompt construction and transcript grounding
- Frontend-backend integration

---

## 📜 License

This project is licensed under the MIT License.

---

<div align="center">

## 👨‍💻 Author

### Aiman Fazal

<a href="https://github.com/aimanfazal">
  <img src="https://img.shields.io/badge/GitHub-aimanfazal-black?style=for-the-badge&logo=github">
</a>

### ⭐ If you found this project interesting, consider starring the repository!

</div>