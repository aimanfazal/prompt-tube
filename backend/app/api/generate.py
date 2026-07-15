"""The /generate route.

This file's only job is to wire HTTP <-> services together and translate
service-level exceptions into clean HTTP error responses. All real logic
lives in app/services/.
"""

from fastapi import APIRouter, HTTPException

from app.schemas.generate import GenerateRequest, GenerateResponse
from app.services.llm import LLMGenerationError, build_prompt, generate_response
from app.services.youtube import (
    InvalidYouTubeURLError,
    TranscriptUnavailableError,
    extract_video_id,
    get_transcript,
)

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    # Step 1: validate the URL and pull out the video ID.
    try:
        video_id = extract_video_id(request.youtube_url)
    except InvalidYouTubeURLError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    # Step 2: fetch the transcript.
    try:
        transcript = get_transcript(video_id)
    except TranscriptUnavailableError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    # Step 3: build the final prompt (falls back to the default if empty).
    final_prompt = build_prompt(transcript, request.prompt)

    # Step 4: call the LLM.
    try:
        generated_text = generate_response(final_prompt)
    except LLMGenerationError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return GenerateResponse(response=generated_text)
