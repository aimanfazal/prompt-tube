import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // A single restrained accent, used sparingly (the "Generate" button,
        // focus rings, and the terminal-style prompt markers).
        accent: {
          DEFAULT: "#5B5BD6",
          hover: "#4747c2",
        },
        canvas: "#0f1115",
        surface: "#161922",
        border: "#262b38",
      },
      fontFamily: {
        mono: ["var(--font-mono)", "ui-monospace", "monospace"],
        sans: ["var(--font-sans)", "ui-sans-serif", "system-ui"],
      },
    },
  },
  plugins: [],
};

export default config;
