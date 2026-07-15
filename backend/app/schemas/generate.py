"""Request and response models for the /generate endpoint.

Keeping these in their own file (separate from the route handler) makes it
easy to see the "shape" of the API at a glance, and lets FastAPI generate
accurate OpenAPI docs automatically.
"""

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """What the frontend sends us."""

    youtube_url: str = Field(
        ...,
        description="Full YouTube URL, e.g. https://www.youtube.com/watch?v=XXXXXXXXXXX",
        min_length=1,
    )
    prompt: str | None = Field(
        default=None,
        description="Optional custom prompt. Falls back to a default summary prompt if omitted.",
    )


class GenerateResponse(BaseModel):
    """What we send back to the frontend."""

    response: str
