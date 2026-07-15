// Small typed wrapper around the one backend endpoint this app has.
// Keeping fetch + error-handling logic here (instead of inline in the page
// component) keeps page.tsx focused on UI state.

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export interface GenerateRequest {
  youtubeUrl: string;
  prompt: string;
}

export interface GenerateResult {
  response: string;
}

export class ApiError extends Error {}

export async function generate({
  youtubeUrl,
  prompt,
}: GenerateRequest): Promise<GenerateResult> {
  let res: Response;

  try {
    res = await fetch(`${API_BASE_URL}/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        youtube_url: youtubeUrl,
        prompt: prompt.trim() === "" ? undefined : prompt,
      }),
    });
  } catch {
    throw new ApiError(
      "Couldn't reach the server. Check your connection and that the backend is running."
    );
  }

  if (!res.ok) {
    // FastAPI's HTTPException responses look like: { "detail": "message" }
    let message = "Something went wrong while generating a response.";
    try {
      const body = await res.json();
      if (typeof body?.detail === "string") {
        message = body.detail;
      }
    } catch {
      // Response wasn't JSON; fall back to the generic message above.
    }
    throw new ApiError(message);
  }

  const data = (await res.json()) as GenerateResult;
  return data;
}
