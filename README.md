# OpenClaw Fleet

A curated collection of AI agent configurations for [OpenClaw](https://openclaw.ai), orchestrated through Discord.

![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## What this is

This repo contains agent personality files (`SOUL.md` + `IDENTITY.md`), Discord layout scripts, automation workflows, and operational docs for running a fleet of specialized AI agents on a single machine via OpenClaw.

**This is not a framework or SaaS product.** It is a working personal setup, published so others can study, fork, and adapt it.

---

## Current status

> ⚠️ This is a real setup that runs daily on one Mac. Some parts are well-tested; others are prototypes.

| Component | Status | Notes |
|-----------|--------|-------|
| 7 shipped agent configs | ✅ Working | `agents/` directory — copy and use |
| Discord 6-category layout | ✅ Working | Scripted sync via `discord-sync.py` |
| Automated cron schedules | ✅ Working | 9 scheduled jobs |
| Zalo personal bridge | ⚠️ Experimental | Unofficial API, session can expire |
| One-command installer | 🚧 Not built | Manual setup required |
| Linux / Docker support | 🚧 Untested | macOS only for now |

---

## Who this is for

**Good fit:**
- Developers who want a local AI operations center through Discord
- OpenClaw users looking for real agent config examples
- Teams prototyping agent workflows before building custom tooling

**Not a good fit:**
- Users expecting a managed product with support
- Production workloads requiring SLA or compliance guarantees
- People who have never used a terminal

---

## Prerequisites

- **macOS** (tested on Apple Silicon)
- **Node.js 20+** (`node --version`)
- **OpenClaw** installed (`npm install -g openclaw`)
- **A Discord bot** with token ([setup guide](docs/DISCORD-BOT-GUIDE.md))
- **An AI model API key** (OpenAI-compatible endpoint)

---

## Quickstart

### 1. Install OpenClaw

```bash
npm install -g openclaw
openclaw setup
```

### 2. Create a Discord bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create app → add bot → copy token
3. OAuth2 → enable `bot` + `applications.commands` scopes
4. Bot permissions: Send Messages, Read Message History, Manage Channels
5. Invite bot to your server

### 3. Configure OpenClaw

```bash
# Set your AI model provider
openclaw config set agents.defaults.model.primary "your-provider/your-model"

# Set Discord credentials
export DISCORD_BOT_TOKEN="your-bot-token"
openclaw config set channels.discord.enabled true
```

See [config.example.json](config.example.json) for a complete template.

### 4. Copy agent configs

```bash
git clone https://github.com/cheafi/openclaw-fleet.git
cd openclaw-fleet

# Copy agents you want to use
cp -r agents/summarize ~/.openclaw/workspace-summarize
cp -r agents/healthcheck ~/.openclaw/workspace-healthcheck
```

### 5. Start the gateway

```bash
openclaw gateway start
openclaw status
```

### 6. Sync Discord layout (optional)

```bash
python3 scripts/discord-sync.py          # audit only (dry run)
python3 scripts/discord-sync.py --apply  # create/move channels
```

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

---

## Shipped agent configs

These agents have custom `SOUL.md` and `IDENTITY.md` in `agents/`:

| Agent | Purpose | Schedule |
|-------|---------|----------|
| `summarize` | Summarize URLs, articles, and documents | On-demand |
| `healthcheck` | System health monitoring | Every 6 hours |
| `file-organizer` | Disk cleanup and file management | Weekly (Sat 10 AM) |
| `gig` | Find freelance and contract work | On-demand |
| `learning-log` | Fleet activity digest | Daily 9:30 AM |
| `self-improving` | Weekly fleet review and improvement proposals | Monday 10 AM |
| `zalo-events` | Zalo event invitations (experimental) | On-demand |

> The Discord layout references ~31 channels. Most work with the default OpenClaw agent. The 7 above have custom personality configs.

---

## Repo structure

```
openclaw-fleet/
├── README.md              ← You are here
├── CONTRIBUTING.md         ← How to contribute
├── SECURITY.md             ← Credential handling
├── ROADMAP.md              ← What's planned
├── CHANGELOG.md            ← What changed
├── LICENSE                 ← MIT
├── config.example.json     ← Safe config template
├── agents/                 ← Agent SOUL.md + IDENTITY.md
├── docs/                   ← Architecture, guides, runbooks
└── scripts/                ← Discord sync, hardening, workflows
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

---

## Security

**Never commit real credentials.** See [SECURITY.md](SECURITY.md) for full guidance.

Quick hardening:

```bash
./scripts/harden-openclaw.sh
```

---

## License

MIT — see [LICENSE](LICENSE).
