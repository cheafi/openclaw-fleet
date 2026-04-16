# Discord Bot Guide (Beginner)

This guide explains what each Discord channel is for, in plain language.

---

## ☕ Welcome

| Channel | What it does | Example prompt |
|---|---|---|
| #一般 | General help and onboarding | "I’m new. Which channel should I use for summaries?" |

---

## 📡 Daily Briefings

| Channel | What it does | Example prompt |
|---|---|---|
| #hk-weather | Daily weather briefing for Hong Kong | "Give me weather for today + tomorrow." |
| #construction-news | Daily APAC construction opportunities | "Only show projects above HKD 10M." |

---

## ⚙️ Core Systems

| Channel | What it does | Example prompt |
|---|---|---|
| #healthcheck | Checks system status and failures | "Run full health check now." |
| #backup | Backup status and recovery notes | "When was last successful backup?" |
| #fail2ban-reporter | Security event and anomaly summary | "Any suspicious events in last 24h?" |
| #learning-log | Daily digest of what agents learned | "Summarize today’s top learnings." |
| #self-improving | Weekly fleet review and improvement plan | "What should we improve first this week?" |
| #self-evolving-skill | Skill/dependency patch status | "Any broken skill dependencies?" |
| #skill-builder | Build new skills from workflows | "Turn this workflow into a reusable skill." |

---

## ⚡ Automation

| Channel | What it does | Example prompt |
|---|---|---|
| #auto-workflow | Chain multiple agents into one pipeline | "Search, summarize, then humanize this topic." |
| #auto-deploy | Automate deploy steps | "Deploy the latest main branch safely." |
| #auto-update | Dependency checks and update guidance | "What should be updated this week?" |
| #browser-automation | Browser scraping and repetitive web steps | "Collect product prices from these pages." |
| #ai-web-automation | Complex multi-step AI web tasks | "Research competitors and compile findings." |
| #zalo-events | Zalo personal-account invite/follow-up | "Send reminder to event attendees." |
| #remind-me | Reminder and scheduling helper | "Remind me tomorrow at 3 PM to follow up." |

---

## 📋 Productivity

| Channel | What it does | Example prompt |
|---|---|---|
| #summarize | Summarize URLs, docs, and text | "Summarize this article in 5 bullets." |
| #file-summary | Analyze local documents | "Extract key risks from this PDF." |
| #file-organizer | Disk cleanup and organization | "Find biggest folders in Downloads." |
| #multi-search-engine | Search multiple engines and merge results | "Compare top 10 results for this query." |
| #humanizer | Rewrite text to sound natural | "Make this email friendlier." |
| #youtube-transcript | Extract transcript from YouTube links | "Get transcript from this video URL." |
| #openai-whisper | Transcribe audio files | "Transcribe this meeting recording." |

---

## 💼 Work & Research

| Channel | What it does | Example prompt |
|---|---|---|
| #gig | Find freelance/contract opportunities | "Find remote AI contracts in APAC." |
| #find-skills | Discover in-demand skills | "What skills are hot for AI ops now?" |
| #skill-vetter | Evaluate tools/candidates/packages | "Is this package safe and maintained?" |
| #free-ride | Find free tiers and credits | "List current free cloud credits." |
| #github | GitHub operations and PR help | "Summarize open PR risks." |
| #api-gateway | API design and debugging | "Help design auth flow for this API." |
| #docker-essential | Container diagnostics and fixes | "Why is this container restarting?" |
| #agent-browser | Deep web research | "Research this company and summarize." |

---

## Keep this guide and Discord in sync

Apply canonical channel descriptions directly to Discord:

```bash
python3 scripts/discord-sync.py --apply
```

This updates channel structure and beginner-friendly channel descriptions (topics).
