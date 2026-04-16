# Contributing

Thanks for your interest. This is primarily a personal fleet config repo, but contributions that make it easier for others to replicate or extend the setup are welcome.

---

## What kinds of contributions are useful

**Most wanted:**
- New agent examples (`SOUL.md` + `IDENTITY.md` pairs) for common use cases
- Bug fixes or clarifications in docs
- Improvements to `scripts/fleet-runner.sh` or `scripts/zalo-bridge.mjs`
- A working `setup.sh` installer (currently the #1 missing piece)
- Testing on Linux / non-macOS platforms

**Less needed right now:**
- Large architectural changes — this is a personal setup, not a framework
- New features that require paid APIs or proprietary services

---

## How to contribute

1. **Fork** the repo
2. **Create a branch**: `git checkout -b feat/your-change`
3. **Make your changes** — follow the conventions below
4. **Test locally** if possible (at minimum, verify JSON is valid and Markdown renders)
5. **Open a PR** with a short description of what you changed and why

For larger changes, open an issue first to discuss before building.

---

## Agent file conventions

Each agent lives in `agents/{agent-name}/` and contains two files:

### `SOUL.md`
Defines the agent's personality, capabilities, and instructions. Structure:
```
# {Agent Name}

## Identity
Who this agent is (1-2 sentences).

## Purpose
What this agent does (1-3 sentences).

## Capabilities
- List of what the agent can do

## Instructions
Detailed behavioral instructions for the LLM.

## Tools
Which tools the agent uses: exec, read, write, web-search, etc.

## Schedule (if applicable)
When this agent runs automatically.
```

### `IDENTITY.md`
A short identity card (name, role, channel, tier). Keep it under 30 lines.

---

## Docs conventions

- Use plain Markdown — no HTML
- Keep headings consistent (`##` for sections, `###` for subsections)
- Use tables for structured comparisons
- Use code blocks with language tags for all code samples
- Write in plain English — avoid marketing language

---

## What not to include in PRs

- Real API keys, tokens, bot tokens, passwords, or session cookies
- Personal data (names, email addresses, phone numbers)
- Copyrighted content
- Files in `~/.openclaw/` that are machine-specific config (only the `agents/` and `docs/` directories belong in this repo)

---

## Code style (scripts)

- Shell scripts: use `#!/usr/bin/env bash`, `set -euo pipefail`, quote all variables
- JavaScript/ESM: use `const`, prefer `async/await` over callbacks, add error handling
- No minification — readability over brevity in example scripts

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
