# OpenClaw Fleet

Ready-to-use AI agent configs for [OpenClaw](https://openclaw.ai), orchestrated through Discord.

**10 agent templates** (incl. 3 financial intelligence agents) · **Discord layout script** · **Cron automation** · **Operational docs**

> Clone the repo. Copy an agent. Start the gateway. Your AI assistant replies in Discord.

![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Agents](https://img.shields.io/badge/shipped_agents-10-blue)

---

## Contents

- [What this is](#what-this-is)
- [Status](#status)
- [Who this is for](#who-this-is-for)
- [Quickstart](#quickstart)
- [How it works](#how-it-works)
- [Shipped agents](#shipped-agents)
- [Discord layout](#discord-layout)
- [Customizing agents](#customizing-agents)
- [Documentation](#documentation)
- [Security](#security)
- [Contributing](#contributing)

---

## What this is

This repo contains **10 tested agent personality configs** (`SOUL.md` + `IDENTITY.md`), a Discord server layout script, automation workflows, and operational docs for running AI agents on a single machine via OpenClaw.

**This is not a framework or SaaS product.** It is a working personal setup, published so others can study, fork, and adapt it.

### Financial intelligence agents

Three specialized agents provide **market regime awareness, technical signal scanning, and portfolio monitoring** — all via Discord. They explain and educate; they never say "buy" or "sell." See [DISCLAIMER.md](DISCLAIMER.md).

| Agent | What it does |
|-------|-------------|
| `market-intel` | Daily regime assessment, breadth, distribution days, macro events |
| `signal-scanner` | VCP, breakout, pullback, RSI, momentum setups with Grade + Confidence |
| `portfolio-monitor` | Position alerts — stop proximity, earnings warnings, correlation risk |

> See [docs/DISCORD-ALERT-TEMPLATES.md](docs/DISCORD-ALERT-TEMPLATES.md) for example Discord alert formats.

---

## Status

> This runs daily on one Mac. Some parts are well-tested; others are prototypes.

| Component | Status | Notes |
|-----------|--------|-------|
| 10 shipped agent configs | ✅ Stable | `agents/` — copy and use (incl. 3 financial) |
| Discord 6-category layout | ✅ Stable | Scripted sync via `discord-sync.py` |
| 9 automated cron schedules | ✅ Stable | Healthcheck, cleanup, digest, review |
| Workflow chains (fleet-runner) | ✅ Stable | 5 multi-agent pipelines |
| Self-improvement loop | ⚠️ Experimental | Runs but unvalidated — no feedback metric yet |
| Zalo personal bridge | ⚠️ Experimental | Unofficial API, session can expire |
| One-command installer | 🚧 Not built | Manual setup required |
| Linux / Docker support | 🚧 Untested | macOS only for now |

---

## Who this is for

✅ Developers who want working agent prompt templates for OpenClaw
✅ Anyone setting up a Discord-based AI operations center
✅ Teams evaluating multi-agent patterns before building custom tooling

❌ Non-technical users (terminal + config editing required)
❌ Production workloads needing uptime guarantees
❌ Users who want a managed product with support

---

## Quickstart

**Prerequisites:** macOS, Node.js 20+, a Discord bot token, an OpenAI-compatible API key.

### 1. Install OpenClaw

```bash
npm install -g openclaw && openclaw setup
```

### 2. Create a Discord bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create app → add bot → copy token
3. OAuth2 → enable `bot` + `applications.commands` scopes
4. Bot permissions: Send Messages, Read Message History, Manage Channels
5. Invite bot to your server

### 3. Configure

```bash
# Set model provider (replace with your endpoint)
openclaw config set agents.defaults.model.primary "openai/gpt-4o"

# Set Discord credentials
openclaw config set channels.discord.token "YOUR_BOT_TOKEN"
openclaw config set channels.discord.enabled true
openclaw config set channels.discord.guilds.YOUR_GUILD_ID '{}'
```

See [config.example.json](config.example.json) for a complete template with all 7 agents.

### 4. Clone and copy agents

```bash
git clone https://github.com/cheafi/openclaw-fleet.git
cd openclaw-fleet

# Copy the agents you want
cp -r agents/summarize ~/.openclaw/workspace-summarize
cp -r agents/healthcheck ~/.openclaw/workspace-healthcheck
# repeat for other agents
```

### 5. Start the gateway

```bash
openclaw gateway start
openclaw status
```

Send a message in your Discord `#summarize` channel. The agent responds.

> `setup.sh` is not available yet. See [ROADMAP.md](ROADMAP.md) for plans.

### 6. Sync Discord layout (optional)

```bash
python3 scripts/discord-sync.py          # audit only (dry run)
python3 scripts/discord-sync.py --apply  # create/move channels
```

### 7. Harden (recommended)

```bash
./scripts/harden-openclaw.sh
```

---

## How it works

```
Discord message in #summarize
    ↓
OpenClaw Gateway (localhost:18789)
    ↓
Agent routing — matches channel to agent
    ↓
Loads SOUL.md (personality + instructions) + IDENTITY.md
    ↓
Sends context + message to AI model (OpenAI-compatible API)
    ↓
Agent uses tools if needed (exec, read, write, web-search)
    ↓
Response posted back to Discord
```

Each agent is defined by two files:
- **`SOUL.md`** — personality, capabilities, output format, rules, tool permissions
- **`IDENTITY.md`** — short identity card (name, emoji, one-liner)

The gateway reads these files as the system prompt. You customize agent behavior by editing the markdown.

---

## Shipped agents

These 7 agents have tested `SOUL.md` + `IDENTITY.md` configs in `agents/`:

| Agent | Purpose | Schedule | Tools |
|-------|---------|----------|-------|
| `summarize` | Summarize URLs, articles, documents | On-demand | web-search, read |
| `healthcheck` | System health monitoring | Every 6 hours | exec, read |
| `file-organizer` | Disk cleanup and file management | Weekly (Sat 10 AM) | exec, read, write |
| `gig` | Find freelance and contract work | On-demand | web-search |
| `learning-log` | Fleet activity digest | Daily 9:30 AM | read, write |
| `self-improving` | Fleet review and improvement proposals | Monday 10 AM | read, write |
| `zalo-events` | Zalo event invitations (experimental) | On-demand | exec |
| `market-intel` | Market regime, breadth, macro events | Daily 7:00 AM | web-search, read |
| `signal-scanner` | Technical setup detection and grading | Daily 7:30 AM | web-search, read |
| `portfolio-monitor` | Position alerts and risk monitoring | Every 4 hours | read |

> **Note:** The Discord layout defines ~31 channels. Most use the default OpenClaw agent with no custom config. Only these 7 have custom personality files.

### Agent blast radius

⚠️ **Agents with `exec` tool can run shell commands.** Treat `SOUL.md` as executable policy. Review the Tools and Rules sections of each agent before deploying. See [SECURITY.md](SECURITY.md).

| Agent | Can run commands | Can write files | Can access network |
|-------|-----------------|----------------|--------------------|
| summarize | ❌ | ❌ | ✅ (web-search) |
| healthcheck | ✅ | ❌ | ✅ |
| file-organizer | ✅ | ✅ | ❌ |
| gig | ❌ | ❌ | ✅ (web-search) |
| learning-log | ❌ | ✅ | ❌ |
| self-improving | ❌ | ✅ | ❌ |
| zalo-events | ✅ | ❌ | ✅ (via bridge) |

---

## Discord layout

```
☕ Welcome
  └── #一般

📡 Daily Briefings
  ├── #hk-weather
  └── #construction-news

⚙️ Core Systems
  ├── #healthcheck        ├── #backup
  ├── #fail2ban-reporter  ├── #learning-log
  ├── #self-improving     ├── #self-evolving-skill
  └── #skill-builder

⚡ Automation
  ├── #auto-workflow      ├── #auto-deploy
  ├── #auto-update        ├── #browser-automation
  ├── #ai-web-automation  ├── #zalo-events
  └── #remind-me

📋 Productivity
  ├── #summarize          ├── #file-summary
  ├── #file-organizer     ├── #multi-search-engine
  ├── #humanizer          ├── #youtube-transcript
  └── #openai-whisper

💼 Work & Research
  ├── #gig         ├── #find-skills   ├── #skill-vetter
  ├── #free-ride   ├── #github        ├── #api-gateway
  ├── #docker-essential  └── #agent-browser
```

> Some channels (e.g. `#hk-weather`, `#construction-news`) are personal to the author's use case. Fork and replace them with your own.

---

## Customizing agents

### Edit an existing agent

```bash
# Edit the SOUL.md in your workspace
nano ~/.openclaw/workspace-summarize/SOUL.md

# Restart to pick up changes
openclaw gateway restart
```

### Create a new agent

1. Create a folder: `agents/your-agent/`
2. Add `SOUL.md` — follow the structure in existing examples
3. Add `IDENTITY.md` — name, emoji, one-liner
4. Copy to `~/.openclaw/workspace-your-agent/`
5. Add an entry to `openclaw.json` (see `config.example.json`)
6. Restart: `openclaw gateway restart`

### Run a workflow chain

```bash
./scripts/fleet-runner.sh content-pipeline "latest AI news"
./scripts/fleet-runner.sh morning-briefing
./scripts/fleet-runner.sh security-chain
```

---

## Repo structure

```
openclaw-fleet/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── ROADMAP.md
├── CHANGELOG.md
├── LICENSE                  MIT
├── .env.example             Environment variable template
├── config.example.json      Safe openclaw.json template (all 7 agents)
├── requirements.txt         Python dependencies
├── package.json             Node.js dependencies
├── Makefile                 Common commands (validate, lint)
├── DISCLAIMER.md            Financial information disclaimer
├── agents/                  10 agent configs (SOUL.md + IDENTITY.md)
├── docs/                    Architecture, guides, runbooks
└── scripts/                 Discord sync, hardening, workflows
```

---

## Documentation

| Doc | Description |
|-----|-------------|
| [Beginner's Guide](docs/BEGINNERS-GUIDE.md) | Non-technical intro to using agents via Discord |
| [Architecture](docs/ARCHITECTURE.md) | System design, data flow, agent lifecycle |
| [Orchestrator](docs/ORCHESTRATOR.md) | Agent tiers, workflow chains, cron schedules |
| [Discord Bot Guide](docs/DISCORD-BOT-GUIDE.md) | What each channel does + example prompts |
| [Discord Operations](docs/DISCORD-OPERATIONS.md) | Operational runbook |
| [Protocols](docs/PROTOCOLS.md) | Inter-agent communication standards |
| [Hardening](docs/HARDENING.md) | Post-setup security steps |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common errors and fixes |
| [Use Cases](docs/USE-CASES.md) | Real-world usage scenarios |
| [Discord Alert Templates](docs/DISCORD-ALERT-TEMPLATES.md) | Financial alert formatting examples |
| [Disclaimer](DISCLAIMER.md) | Financial information disclaimer |

---

## Security

⚠️ **Agents with the `exec` tool can run arbitrary shell commands.** A prompt injection in user input could lead to unintended command execution. Mitigations:

1. Run `./scripts/harden-openclaw.sh` after setup
2. Review each agent's `SOUL.md` Tools section before deploying
3. Enable `tools.fs.workspaceOnly: true` (the hardening script does this)
4. Use least-privilege Discord bot permissions (not Administrator)
5. Never commit real credentials — see [SECURITY.md](SECURITY.md)

---

## Production-readiness checklist

```
[ ] All agents load without error (openclaw status)
[ ] Gateway responds on localhost:18789
[ ] Discord bot is online and responds in at least one channel
[ ] harden-openclaw.sh has been run
[ ] .env is not tracked by git
[ ] API key spending limits are set
[ ] Discord bot has minimum permissions
[ ] Disk space > 10% free
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Most wanted:

- New agent examples (`SOUL.md` + `IDENTITY.md` pairs)
- Bug fixes or clarifications in docs
- A working `setup.sh` installer
- Testing on Linux

---

## License

MIT — see [LICENSE](LICENSE).
