# Agent Configs

This folder contains example `SOUL.md` and `IDENTITY.md` files for each agent in the fleet.

## How to use

Copy any agent folder into your OpenClaw workspace directory:

```bash
cp -r agents/summarize ~/.openclaw/workspace-summarize
cp -r agents/healthcheck ~/.openclaw/workspace-healthcheck
```

Then register the agent in `~/.openclaw/openclaw.json` under the `agents` array. See `config.example.json` at the repo root for the format.

## File format

Each agent folder contains two files:

### `SOUL.md`
Defines the agent's personality, purpose, capabilities, and LLM instructions. This is the primary file the AI model reads to understand how to behave.

### `IDENTITY.md`
A short identity card: agent name, role, assigned Discord channel, and tier. Kept under 30 lines.

## Available agents

| Agent | What it does | Auto-schedule |
|-------|-------------|---------------|
| file-organizer | Disk cleanup and file management | Saturday 10 AM HKT |
| gig | Find freelance and contract work | On-demand |
| healthcheck | System health monitoring | Every 6 hours |
| learning-log | Fleet activity digest | Daily 9:30 AM HKT |
| self-improving | Weekly fleet review and improvement proposals | Monday 10 AM HKT |
| summarize | Summarize articles, URLs, and documents | On-demand |
| zalo-events | Zalo event invitations and follow-up (personal account) | On-demand |

## Creating a new agent

1. Create a new folder: `agents/your-agent-name/`
2. Add `SOUL.md` — follow the structure in existing examples
3. Add `IDENTITY.md` — short identity card
4. Copy to `~/.openclaw/workspace-your-agent-name/`
5. Add an entry to `openclaw.json`
6. Restart the gateway: `openclaw gateway restart`

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full agent file format spec.
