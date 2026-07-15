"""Talks to Groq's free, OpenAI-compatible chat completions API.

NOTE (you): this file is fully wired up, but it needs your own Groq API key
to actually run. Groq's free tier doesn't require a credit card. Copy
backend/.env.example to backend/.env and fill in GROQ_API_KEY.

Why Groq instead of OpenAI: OpenAI's API is pay-as-you-go with no free tier.
Groq hosts open-weight models (Llama, Gemma, etc.) on its own hardware and
gives a generous free daily quota with no card required. Its API speaks the
same protocol as OpenAI's older Chat Completions API, so we still use the
`openai` Python package here -- we just point it at Groq's server instead
of OpenAI's, and use `chat.completions.create` instead of the newer
`responses.create` (Groq doesn't support the Responses API).
"""

import os

from openai import APIError, APIStatusError, OpenAI, OpenAIError

DEFAULT_PROMPT = "Generate a concise summary of this video."

GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# The template the final prompt is built from. Keeping it as a plain string
# (instead of something fancier like a templating library) is easiest for a
# small project with a single prompt shape.
_PROMPT_TEMPLATE = """User Request:
{prompt}

Video Transcript:
{transcript}

Please answer based only on the provided transcript."""


class LLMGenerationError(Exception):
    """Raised when the LLM API call fails or returns nothing usable."""


def build_prompt(transcript: str, prompt: str | None) -> str:
    """Combine the transcript and the (possibly missing) user prompt."""
    effective_prompt = prompt.strip() if prompt and prompt.strip() else DEFAULT_PROMPT
    return _PROMPT_TEMPLATE.format(prompt=effective_prompt, transcript=transcript)


def generate_response(final_prompt: str) -> str:
    """Send the constructed prompt to Groq's chat completions API and return the text.

    Raises LLMGenerationError on any failure (missing key, network issue,
    API error, or an empty response) so the API layer can turn it into a
    clean HTTP error.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        # TODO (you): set GROQ_API_KEY in backend/.env
        raise LLMGenerationError(
            "No Groq API key is configured on the server. "
            "Set GROQ_API_KEY in backend/.env."
        )

    model = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
    client = OpenAI(api_key=api_key, base_url=GROQ_BASE_URL)

    try:
        result = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": final_prompt}],
        )
    except (APIError, APIStatusError, OpenAIError) as exc:
        raise LLMGenerationError(
            "The AI service couldn't complete the request. Please try again."
        ) from exc

    output_text = result.choices[0].message.content if result.choices else None
    if not output_text or not output_text.strip():
        raise LLMGenerationError("The AI service returned an empty response.")

    return output_text
