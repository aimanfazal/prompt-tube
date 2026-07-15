interface ResponseDisplayProps {
  isLoading: boolean;
  error: string | null;
  response: string | null;
}

export function ResponseDisplay({
  isLoading,
  error,
  response,
}: ResponseDisplayProps) {
  return (
    <div className="flex flex-col gap-2">
      <span className="font-mono text-sm text-accent">
        <span className="text-white/40">$</span> response
      </span>

      <div className="min-h-[10rem] whitespace-pre-wrap rounded-md border border-border bg-surface px-4 py-3 text-sm text-white/90">
        {isLoading && (
          <span className="text-white/50">Extracting transcript and generating a response…</span>
        )}

        {!isLoading && error && <span className="text-red-400">{error}</span>}

        {!isLoading && !error && response && response}

        {!isLoading && !error && !response && (
          <span className="text-white/30">
            Paste a YouTube URL above and click Generate to see a response here.
          </span>
        )}
      </div>
    </div>
  );
}
