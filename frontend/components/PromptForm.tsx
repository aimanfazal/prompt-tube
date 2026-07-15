"use client";

interface PromptFormProps {
  youtubeUrl: string;
  prompt: string;
  isLoading: boolean;
  onYoutubeUrlChange: (value: string) => void;
  onPromptChange: (value: string) => void;
  onSubmit: () => void;
}

export function PromptForm({
  youtubeUrl,
  prompt,
  isLoading,
  onYoutubeUrlChange,
  onPromptChange,
  onSubmit,
}: PromptFormProps) {
  return (
    <form
      className="flex flex-col gap-6"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit();
      }}
    >
      <div className="flex flex-col gap-2">
        <label htmlFor="youtube-url" className="font-mono text-sm text-accent">
          <span className="text-white/40">$</span> youtube_url
        </label>
        <input
          id="youtube-url"
          type="url"
          required
          placeholder="https://www.youtube.com/watch?v=..."
          value={youtubeUrl}
          disabled={isLoading}
          onChange={(e) => onYoutubeUrlChange(e.target.value)}
          className="w-full rounded-md border border-border bg-surface px-4 py-3 font-mono text-sm text-white placeholder:text-white/30 disabled:opacity-50"
        />
      </div>

      <div className="flex flex-col gap-2">
        <label htmlFor="prompt" className="font-mono text-sm text-accent">
          <span className="text-white/40">$</span> prompt{" "}
          <span className="text-white/30">(optional)</span>
        </label>
        <textarea
          id="prompt"
          rows={4}
          placeholder="Generate a concise summary of this video."
          value={prompt}
          disabled={isLoading}
          onChange={(e) => onPromptChange(e.target.value)}
          className="w-full resize-y rounded-md border border-border bg-surface px-4 py-3 text-sm text-white placeholder:text-white/30 disabled:opacity-50"
        />
      </div>

      <button
        type="submit"
        disabled={isLoading}
        className="w-full rounded-md bg-accent px-4 py-3 font-medium text-white transition-colors hover:bg-accent-hover disabled:cursor-not-allowed disabled:opacity-50 sm:w-fit sm:px-8"
      >
        {isLoading ? "Generating…" : "Generate"}
      </button>
    </form>
  );
}
