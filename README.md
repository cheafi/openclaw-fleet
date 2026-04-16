# OpenClaw Fleet

A practical, self-managing AI agent fleet for Discord, built on [OpenClaw](https://openclaw.ai).

![Agents](https://img.shields.io/badge/agents-31-blue)
![Crons](https://img.shields.io/badge/automated%20crons-9-green)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Value proposition

This repository gives you a real, running blueprint for operating specialized AI agents through Discord channels, with scheduled automation, shared learning, and operational docs.

---

## Current status

| Area | Status |
|------|--------|
| 31-agent fleet | ✅ Running |
| Discord 6-category layout | ✅ Live |
| 9 automated schedules | ✅ Live |
| Zalo personal-account bridge | ✅ Live (first-time QR login required) |
| One-command installer (`setup.sh`) | 🚧 Not built yet |
| Linux/cloud deployment docs | 🚧 Partial |

---

## Who this is for

**Good fit**
- Developers and power users who want a local AI operations center
- Teams prototyping agent workflows on Discord

**Not a good fit**
- Users expecting a managed SaaS product
- Production workloads requiring strict SLA/compliance guarantees

---

## Architecture (high level)

```text
Discord message
    ↓
OpenClaw Gateway (localhost:18789)
    ↓
Agent routing by channel
    ↓
Load SOUL.md + IDENTITY.md + shared protocols
    ↓
Model call (OpenAI-compatible API)
    ↓
Tool use (exec/read/write/web/MCP)
    ↓
Response posted back to Discord
```

---

## Discord layout (canonical)

```text
☕ Welcome
  └── #一般

📡 Daily Briefings
  ├── #hk-weather
  └── #construction-news

⚙️ Core Systems
  ├── #healthcheck
  ├── #backup
  ├── #fail2ban-reporter
  ├── #learning-log
  ├── #self-improving
  ├── #self-evolving-skill
  └── #skill-builder

⚡ Automation
  ├── #auto-workflow
  ├── #auto-deploy
  ├── #auto-update
  ├── #browser-automation
  ├── #ai-web-automation
  ├── #zalo-events
  └── #remind-me

📋 Productivity
  ├── #summarize
  ├── #file-summary
  ├── #file-organizer
  ├── #multi-search-engine
  ├── #humanizer
  ├── #youtube-transcript
  └── #openai-whisper

💼 Work & Research
  ├── #gig
  ├── #find-skills
  ├── #skill-vetter
  ├── #free-ride
  ├── #github
  ├── #api-gateway
  ├── #docker-essential
  └── #agent-browser
```

To verify and sync your server to this layout:

```bash
# audit only (no changes)
python3 scripts/discord-sync.py

# apply missing categories/channels and move misplaced channels
python3 scripts/discord-sync.py --apply
```

---

## Quickstart

### 1) Install OpenClaw

```bash
npm install -g openclaw
openclaw --version
```

### 2) Create Discord bot

1. Open [Discord Developer Portal](https://discord.com/developers/applications)
2. Create app → add bot
3. Copy bot token
4. OAuth2 URL Generator → `bot` scope + permissions:
   - Send Messages
   - Read Message History
   - Manage Channels
5. Invite bot to your server

### 3) Initialize OpenClaw locally

```bash
openclaw setup
```

This creates `~/.openclaw/openclaw.json`.

### 4) Configure model provider

```bash
openclaw config set models.mode replace
openclaw config set models.providers '[{"id":"my-provider","kind":"openai-custom","baseURL":"https://your-api.com/v1","apiKey":"YOUR_API_KEY","models":["your-model"]}]'
```

### 5) Configure Discord

```bash
openclaw config set channels.discord.token "YOUR_BOT_TOKEN"
openclaw config set channels.discord.enabled true
openclaw config set channels.discord.guilds.YOUR_GUILD_ID '{}'
```

### 6) Clone this repo and copy agent configs

```bash
git clone https://github.com/cheafi/openclaw-fleet.git
cd openclaw-fleet
cp -r agents/summarize ~/.openclaw/workspace-summarize
cp -r agents/healthcheck ~/.openclaw/workspace-healthcheck
# repeat for other agents you need
```

> `setup.sh` is not available yet. Manual copy is currently required.

### 7) Start gateway

```bash
openclaw gateway start
openclaw status
```

---

## Production-readiness notes

- Keep gateway loopback-only (`127.0.0.1`) unless you have proxy auth + TLS
- Treat `SOUL.md` as executable policy (especially for `exec` tool)
- Use least-privilege Discord bot permissions
- Rotate API keys and Discord token if exposed
- Enable periodic backups and run security audit regularly
- Apply the baseline hardening script: `./scripts/harden-openclaw.sh`

---

## Repo structure

```text
openclaw-fleet/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── ROADMAP.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── config.example.json
├── agents/
├── docs/
└── scripts/
```

---

## Key docs

- [Beginner guide](docs/BEGINNERS-GUIDE.md)
- [Architecture deep dive](docs/ARCHITECTURE.md)
- [Discord operations runbook](docs/DISCORD-OPERATIONS.md)
- [Hardening guide](docs/HARDENING.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Use cases](docs/USE-CASES.md)
- [Security policy](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

---

## Security

Never commit secrets. Specifically:
- `~/.openclaw/openclaw.json`
- `~/.openclaw/skill-secrets.env`
- `~/.openclaw/zalo-session/credentials.json`

See [SECURITY.md](SECURITY.md) for full guidance.

---

## License

MIT — see [LICENSE](LICENSE).
