"use client";

import { useState } from "react";
import { PromptForm } from "@/components/PromptForm";
import { ResponseDisplay } from "@/components/ResponseDisplay";
import { ApiError, generate } from "@/lib/api";

export default function Home() {
  const [youtubeUrl, setYoutubeUrl] = useState("");
  const [prompt, setPrompt] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [response, setResponse] = useState<string | null>(null);

  async function handleSubmit() {
    setIsLoading(true);
    setError(null);
    setResponse(null);

    try {
      const result = await generate({ youtubeUrl, prompt });
      setResponse(result.response);
    } catch (err) {
      const message =
        err instanceof ApiError
          ? err.message
          : "Something unexpected went wrong. Please try again.";
      setError(message);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="mx-auto flex min-h-screen max-w-2xl flex-col gap-10 px-6 py-16">
      <header className="flex flex-col gap-2">
        <h1 className="text-2xl font-semibold tracking-tight text-white">
          Prompt<span className="text-accent">Tube</span>
        </h1>
        <p className="text-sm text-white/50">
          Paste a YouTube URL. Ask it anything. It answers from the transcript.
        </p>
      </header>

      <PromptForm
        youtubeUrl={youtubeUrl}
        prompt={prompt}
        isLoading={isLoading}
        onYoutubeUrlChange={setYoutubeUrl}
        onPromptChange={setPrompt}
        onSubmit={handleSubmit}
      />

      <ResponseDisplay isLoading={isLoading} error={error} response={response} />
    </main>
  );
}
