"""FastAPI application entrypoint.

Run with:  uvicorn app.main:app --reload
(from inside the backend/ directory, with your virtualenv activated)
"""

import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load backend/.env before anything else reads os.environ.
load_dotenv()

from app.api.generate import router as generate_router  # noqa: E402

app = FastAPI(
    title="PromptTube API",
    description="Turns a YouTube video's transcript into a promptable text source.",
    version="0.1.0",
)

frontend_origin = os.environ.get("FRONTEND_ORIGIN", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin],
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(generate_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Simple endpoint to confirm the server is running."""
    return {"status": "ok"}
