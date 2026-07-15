# PromptTube v0.1

Paste a YouTube URL, optionally add a prompt, and get an LLM-generated
response based on the video's transcript.

This is a small, intentionally minimal full-stack project:

- **Frontend:** Next.js (App Router) + TypeScript + Tailwind CSS
- **Backend:** FastAPI (Python 3.12+)
- **Transcript extraction:** `youtube-transcript-api`
- **LLM:** Groq (free, OpenAI-compatible API — no credit card needed)

## Project layout

```
prompttube/
  backend/
    app/
      api/        # HTTP route handlers (thin — just wiring)
      services/    # actual logic: youtube.py, llm.py
      schemas/     # Pydantic request/response models
      main.py      # FastAPI app + CORS setup
    requirements.txt
    .env.example
  frontend/
    app/
      layout.tsx
      page.tsx     # the single page
      globals.css
    components/
      PromptForm.tsx
      ResponseDisplay.tsx
    lib/
      api.ts       # typed fetch wrapper for the backend
    .env.local.example
```

## Backend setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# then open .env and set GROQ_API_KEY (get one free, no card, at
# https://console.groq.com/keys)

uvicorn app.main:app --reload
```

The API will be running at `http://localhost:8000`. Interactive docs are
available at `http://localhost:8000/docs`.

## Frontend setup

```bash
cd frontend
npm install

cp .env.local.example .env.local
# defaults already point at http://localhost:8000, only change if needed

npm run dev
```

The app will be running at `http://localhost:3000`.

## How it works (processing flow)

1. User pastes a YouTube URL and (optionally) a prompt, then clicks Generate.
2. Frontend POSTs `{ youtube_url, prompt }` to `POST /generate`.
3. Backend extracts the video ID and fetches its transcript via
   `youtube-transcript-api`.
4. If no prompt was given, a default ("Generate a concise summary of this
   video.") is used instead.
5. Backend builds a single combined prompt (user request + transcript) and
   sends it to Groq's free chat completions API.
6. The generated text is returned as `{ response }` and displayed on the page.

## What's intentionally left out of v0.1

No auth, no database, no saved history, no caching, no multi-video support,
no Docker/CI. See the original spec for the full list — these are explicit
non-goals for this version, not oversights.

## What you still need to do

- Create a free Groq API key at https://console.groq.com/keys (no credit
  card required) and add it as `GROQ_API_KEY` in `backend/.env` (see
  `backend/app/services/llm.py` for where it's used).
- Test the end-to-end flow with a real YouTube video that has captions.

## Note on free tiers

Groq's free tier is generous but rate-limited, and free-tier quotas and
model names can change over time — check https://console.groq.com/docs/models
if `GROQ_MODEL` in `.env` ever returns a "model not found" error.
