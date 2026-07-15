"""Everything related to turning a YouTube URL into a transcript string.

This module intentionally does ONE thing: given a URL, return the transcript
text (or raise a clear, specific exception explaining what went wrong).
"""

import re

from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

# Matches the video ID out of the common YouTube URL shapes:
#   https://www.youtube.com/watch?v=VIDEOID
#   https://youtu.be/VIDEOID
#   https://www.youtube.com/embed/VIDEOID
# A video ID is always exactly 11 characters of [A-Za-z0-9_-].
_YOUTUBE_ID_PATTERN = re.compile(
    r"(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([A-Za-z0-9_-]{11})"
)


class InvalidYouTubeURLError(Exception):
    """Raised when we can't extract a video ID from the given URL."""


class TranscriptUnavailableError(Exception):
    """Raised when a video has no usable transcript/captions."""


def extract_video_id(youtube_url: str) -> str:
    """Pull the 11-character video ID out of a YouTube URL.

    Raises InvalidYouTubeURLError if the URL doesn't look like YouTube.
    """
    match = _YOUTUBE_ID_PATTERN.search(youtube_url.strip())
    if not match:
        raise InvalidYouTubeURLError(
            "That doesn't look like a valid YouTube URL. "
            "Expected something like https://www.youtube.com/watch?v=... "
            "or https://youtu.be/..."
        )
    return match.group(1)


def get_transcript(video_id: str) -> str:
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_segments = ytt_api.fetch(video_id)

    except (NoTranscriptFound, TranscriptsDisabled) as exc:
        raise TranscriptUnavailableError(
            "This video doesn't have captions available, so a transcript "
            "can't be extracted. Try a different video."
        ) from exc

    except VideoUnavailable as exc:
        raise TranscriptUnavailableError(
            "That video couldn't be found. It may be private, deleted, or "
            "the URL may be incorrect."
        ) from exc

    full_text = " ".join(
        segment.text
        for segment in transcript_segments
    )

    if not full_text.strip():
        raise TranscriptUnavailableError(
            "The transcript for this video came back empty."
        )

    return full_text
