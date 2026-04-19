# Agent Configs

This folder contains `SOUL.md` and `IDENTITY.md` files for 7 agents in the fleet.

## Quick start

```bash
# Copy any agent to your OpenClaw workspace
cp -r agents/summarize ~/.openclaw/workspace-summarize

# Register it in your config (see config.example.json for full format)
# Then restart
openclaw gateway restart
```

## File format

### `SOUL.md`
The primary file — defines personality, capabilities, output format, rules, and tool permissions. The LLM reads this as its system prompt.

### `IDENTITY.md`
Short identity card: name, emoji, one-liner. Kept under 30 lines.

## Shipped agents

> All 7 agents ship with real, tested configs. They were written for one person's setup — review and adapt to your needs.

| Agent | Purpose | Schedule | Tools | Status |
|-------|---------|----------|-------|--------|
| summarize | Summarize URLs, articles, documents | On-demand | web-search, read | ✅ Stable |
| healthcheck | System health monitoring | Every 6 hours | exec, read | ✅ Stable |
| file-organizer | Disk cleanup and file management | Sat 10 AM HKT | exec, read, write | ✅ Stable |
| gig | Find freelance and contract work | On-demand | web-search | ✅ Stable |
| learning-log | Fleet activity digest | Daily 9:30 AM | read, write | ✅ Stable |
| self-improving | Fleet review and improvement proposals | Mon 10 AM | read, write | ✅ Stable |
| zalo-events | Zalo event invitations (personal account) | On-demand | exec | ⚠️ Experimental |

> **About the "31 agents" number:** The Discord layout has 31 channels. Most use the default OpenClaw agent — only these 7 have custom personality configs. The other 24 channels are just named endpoints.

## Agent permissions

⚠️ Agents with `exec` can run shell commands. Review each `SOUL.md` before deploying.

| Agent | exec | read | write | network |
|-------|------|------|-------|---------|
| summarize | ❌ | ✅ | ❌ | ✅ |
| healthcheck | ✅ | ✅ | ❌ | ✅ |
| file-organizer | ✅ | ✅ | ✅ | ❌ |
| gig | ❌ | ❌ | ❌ | ✅ |
| learning-log | ❌ | ✅ | ✅ | ❌ |
| self-improving | ❌ | ✅ | ✅ | ❌ |
| zalo-events | ✅ | ❌ | ❌ | ✅ |

## Creating a new agent

1. Create a folder: `agents/your-agent/`
2. Add `SOUL.md` — follow the structure in existing examples
3. Add `IDENTITY.md` — name, emoji, one-liner
4. Copy to `~/.openclaw/workspace-your-agent/`
5. Add an entry to `openclaw.json` (see `config.example.json`)
6. Restart: `openclaw gateway restart`

## Inter-agent communication

All agents reference a shared protocol for logging errors, corrections, and successes to the `learning-log` workspace. See [docs/PROTOCOLS.md](../docs/PROTOCOLS.md).

> **Note:** The inter-agent protocol is a convention enforced by prompts, not by code. Agents follow it because their `SOUL.md` says to — there is no runtime enforcement.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full agent file format spec.
