# 🦞 OpenClaw AI Agent Fleet

> **31 AI agents working together on Discord** — self-improving, automated, and beginner-friendly.

A complete setup for running a fleet of specialized AI agents through [OpenClaw](https://openclaw.ai) on Discord. Each agent has its own channel, personality, and job — from daily weather updates to automated security scans.

![Agents](https://img.shields.io/badge/agents-31-blue)
![Crons](https://img.shields.io/badge/automated_crons-9-green)
![Discord](https://img.shields.io/badge/discord-6_categories-purple)

---

## 🤔 What Is This?

This is a **personal AI operations center** that runs on your Mac (or any machine). Think of it as having a team of AI assistants, each specialized in a different task, all talking to you through Discord.

**You don't need to code.** Just talk to them in Discord like you would with a colleague.

### Examples of What You Can Do

| Just Type This in Discord | What Happens |
|--------------------------|--------------|
| *"Summarize this article: [url]"* in #summarize | AI reads the page and gives you a summary |
| *"Find freelance AI jobs in Asia"* in #gig | AI searches job boards and lists opportunities |
| *"What's the weather?"* in #hk-weather | Already automated — posts every morning at 9 AM |
| *"Remind me to call John tomorrow 3pm"* in #remind-me | Sets a reminder and notifies you |
| *"Transcribe this YouTube video: [url]"* in #youtube-transcript | Extracts the full transcript |
| *"Make this text sound more human"* in #humanizer | Rewrites robotic text naturally |
| *"Check system health"* in #healthcheck | Runs a full diagnostic of your setup |

---

## 📁 Discord Server Layout

Your Discord server is organized into **6 clean categories**:

```
☕ Welcome
  └── #一般              — General chat

📡 Daily Briefings
  ├── #hk-weather        — Auto weather at 9 AM (Hong Kong)
  └── #construction-news — Auto APAC construction news at 9 AM

⚙️ Core Systems
  ├── #healthcheck       — System health monitoring (auto every 6h)
  ├── #backup            — Daily backups at 3 AM
  ├── #fail2ban-reporter — Security scans (auto every 6h)
  ├── #learning-log      — Fleet activity digest (auto 9:30 AM)
  ├── #self-improving    — Weekly fleet review (Mon 10 AM)
  ├── #self-evolving-skill — Auto skill patching (daily 4 AM)
  └── #skill-builder     — Convert workflows to skills

⚡ Automation
  ├── #auto-workflow     — Chain agents into pipelines
  ├── #auto-deploy       — CI/CD deployment
  ├── #auto-update       — Weekly dependency scan (Sun 8 PM)
  ├── #browser-automation — Web scraping & form filling
  ├── #ai-web-automation — Complex AI web tasks
  ├── #zalo-events       — Zalo OA event invites & follow-up
  └── #remind-me         — Scheduled reminders

📋 Productivity
  ├── #summarize         — Summarize articles, docs, URLs
  ├── #file-summary      — Analyze local documents
  ├── #file-organizer    — Filesystem cleanup (auto weekly)
  ├── #multi-search-engine — Search across multiple engines
  ├── #humanizer         — Rewrite text naturally
  ├── #youtube-transcript — Video transcription
  └── #openai-whisper    — Audio transcription

💼 Work & Research
  ├── #gig               — Find freelance opportunities
  ├── #find-skills       — Discover talent
  ├── #skill-vetter      — Assess candidates/tools
  ├── #free-ride          — Find free tiers & deals
  ├── #github            — GitHub operations
  ├── #api-gateway       — API design & debugging
  ├── #docker-essential  — Container management
  └── #agent-browser     — Web research
```

---

## 🚀 Quick Start (From Zero to Running)

### Prerequisites
- macOS (Apple Silicon or Intel)
- Node.js 20+ (`brew install node`)
- A Discord account
- ~30 minutes

### Step 1: Install OpenClaw
```bash
npm install -g openclaw
openclaw setup
```

### Step 2: Create a Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application → name it "Wai Bot" (or anything)
3. Go to **Bot** → copy the token
4. Go to **OAuth2 → URL Generator** → select `bot` scope + permissions: `Send Messages, Manage Channels, Read Message History`
5. Open the generated URL → add bot to your Discord server

### Step 3: Configure OpenClaw
```bash
# Set your model provider
openclaw config set models.mode replace
openclaw config set models.providers '[{"id":"my-provider","kind":"openai-custom","baseURL":"https://your-api.com/v1","apiKey":"your-key","models":["your-model"]}]'

# Connect Discord
openclaw config set channels.discord.token "YOUR_BOT_TOKEN"
openclaw config set channels.discord.enabled true
```

### Step 4: Clone This Fleet
```bash
git clone https://github.com/cheafi/openclaw-fleet.git
cd openclaw-fleet
./setup.sh  # Coming soon — auto-creates all agents & channels
```

### Step 5: Start the Gateway
```bash
openclaw gateway start
```

That's it! Your agents are now live on Discord. 🎉

---

## 🏗️ Architecture

### How It Works

```
You (Discord) → OpenClaw Gateway → AI Model → Agent Response → Discord Channel
                     ↓
              Agent SOUL.md (personality + instructions)
              Agent IDENTITY.md (who am I)
              Shared PROTOCOLS.md (how to communicate)
```

### Agent Tiers

| Tier | Purpose | Agents | Schedule |
|------|---------|--------|----------|
| **0 — Infrastructure** | Keep the system alive | healthcheck, backup, fail2ban-reporter | Auto (every 6h / daily) |
| **1 — Intelligence** | Learn and improve the fleet | learning-log, self-improving, self-evolving-skill, skill-builder | Auto (daily / weekly) |
| **2 — Automation** | Execute automated workflows | auto-workflow, auto-deploy, auto-update, browser-automation, ai-web-automation, zalo-events, remind-me | On-demand + cron |
| **3 — Productivity** | Help you daily | summarize, file-summary, file-organizer, multi-search-engine, humanizer, youtube-transcript, openai-whisper | On-demand + weekly cleanup |
| **4 — Specialists** | Domain expertise | construction-news, gig, find-skills, skill-vetter, free-ride, github, api-gateway, docker-essential, agent-browser | On-demand + daily news |

### Self-Improving Loop

The fleet improves itself automatically:

```
1. All agents log errors/successes → learning-log
2. learning-log generates daily digest
3. self-improving reviews fleet weekly, scores agents
4. self-evolving-skill patches broken dependencies
5. Repeat forever
```

---

## ⏰ Automated Schedules

These run automatically — no action needed:

| Time (HKT) | What | Channel |
|-------------|------|---------|
| Every 6h | System health check | #healthcheck |
| Every 6h | Security scan | #fail2ban-reporter |
| 3:00 AM | Full system backup | #backup |
| 4:00 AM | Auto-patch skills | #self-evolving-skill |
| 9:00 AM | HK weather report | #hk-weather |
| 9:00 AM | Construction news | #construction-news |
| 9:30 AM | Fleet activity digest | #learning-log |
| Saturday 10 AM | Disk cleanup scan | #file-organizer |
| Sunday 8 PM | Dependency scan | #auto-update |
| Monday 10 AM | Weekly fleet review | #self-improving |

---

## 💡 Use Cases

### For Job Seekers
- Use **#gig** to find freelance opportunities automatically
- Use **#find-skills** to discover in-demand skills
- Use **#humanizer** to polish your cover letters
- Use **#summarize** to quickly read job descriptions

### For Content Creators
- Use **#youtube-transcript** to get transcripts from videos
- Use **#summarize** to create article summaries
- Use **#humanizer** to rewrite AI-generated text
- Use **#openai-whisper** to transcribe audio/podcasts

### For Developers
- Use **#github** for PR reviews and repo management
- Use **#api-gateway** to design and debug APIs
- Use **#docker-essential** for container management
- Use **#auto-deploy** for CI/CD pipelines

### For Business / Sales
- Use **#construction-news** for industry prospecting
- Use **#zalo-events** for event invitation automation (Vietnam market)
- Use **#multi-search-engine** for market research
- Use **#agent-browser** for competitive analysis

### For Personal Productivity
- Use **#remind-me** for reminders and scheduling
- Use **#file-organizer** for automatic disk cleanup
- Use **#file-summary** to analyze documents
- Use **#free-ride** to find free tools and deals

---

## 📂 File Structure

```
~/.openclaw/
├── openclaw.json              # Main config (agents, channels, model)
├── workspace-{agent}/         # Per-agent workspace
│   ├── SOUL.md                # Agent personality & instructions
│   ├── IDENTITY.md            # Agent identity card
│   └── {work files}           # Agent-specific data
├── agents/{agent}/agent/
│   └── models.json            # Model routing per agent
├── workspace-learning-log/
│   ├── PROTOCOLS.md           # Shared communication protocols
│   ├── errors/                # Error logs from all agents
│   ├── corrections/           # User correction patterns
│   ├── successes/             # What worked well
│   ├── knowledge/             # Shared knowledge base
│   └── reports/               # Weekly analysis reports
└── workspace-self-improving/
    ├── ORCHESTRATOR.md         # Master architecture document
    └── fleet-runner.sh         # Workflow chain executor
```

---

## 🔗 Workflow Chains

Run multi-agent pipelines with one command:

```bash
# Weekly self-improvement cycle
~/.openclaw/workspace-self-improving/fleet-runner.sh self-improvement-loop

# Security audit
~/.openclaw/workspace-self-improving/fleet-runner.sh security-chain

# Content research: search → summarize → humanize
~/.openclaw/workspace-self-improving/fleet-runner.sh content-pipeline "AI in construction"

# Morning briefing: health + news + digest
~/.openclaw/workspace-self-improving/fleet-runner.sh morning-briefing
```

---

## 🛡️ Security & Privacy

- **All data stays local** — nothing leaves your machine except API calls to your chosen model
- **Token auth** on the gateway (loopback only, port 18789)
- **fail2ban-reporter** scans for security threats every 6 hours
- **backup agent** creates daily encrypted snapshots
- No telemetry, no tracking

---

## 📋 Agent Quick Reference

| Agent | What It Does | Talk To It In |
|-------|-------------|---------------|
| healthcheck | System monitoring | #healthcheck |
| backup | Daily backups | #backup |
| fail2ban-reporter | Security scans | #fail2ban-reporter |
| learning-log | Fleet memory | #learning-log |
| self-improving | Fleet reviews | #self-improving |
| self-evolving-skill | Auto-patching | #self-evolving-skill |
| skill-builder | Build new skills | #skill-builder |
| auto-workflow | Chain agents | #auto-workflow |
| auto-deploy | CI/CD | #auto-deploy |
| auto-update | Dependency checks | #auto-update |
| browser-automation | Web scraping | #browser-automation |
| ai-web-automation | AI web tasks | #ai-web-automation |
| zalo-events | Zalo invites | #zalo-events |
| remind-me | Reminders | #remind-me |
| summarize | Summarize anything | #summarize |
| file-summary | Analyze files | #file-summary |
| file-organizer | Disk cleanup | #file-organizer |
| multi-search-engine | Multi-search | #multi-search-engine |
| humanizer | Rewrite text | #humanizer |
| youtube-transcript | Video transcripts | #youtube-transcript |
| openai-whisper | Audio transcription | #openai-whisper |
| construction-news | Industry news | #construction-news |
| gig | Find freelance work | #gig |
| find-skills | Discover talent | #find-skills |
| skill-vetter | Assess tools/people | #skill-vetter |
| free-ride | Free tier finder | #free-ride |
| github | GitHub ops | #github |
| api-gateway | API design | #api-gateway |
| docker-essential | Containers | #docker-essential |
| agent-browser | Web research | #agent-browser |

---

## 🤝 Contributing

This is a personal fleet setup, but feel free to:
- Fork and adapt for your own use
- Open issues for questions
- Submit PRs for improvements

---

## 📜 License

MIT — do whatever you want with it.

---

*Built with [OpenClaw](https://openclaw.ai) 🦞 — one CLI to rule them all.*
