# ORCHESTRATOR.md — Agent Fleet Architecture

## System Overview

```
                    ┌─────────────────────────────────┐
                    │      🧠 self-improving          │
                    │    (Fleet Brain / Meta-Agent)    │
                    │  Reviews, scores, upgrades all   │
                    └──────────┬──────────┬───────────┘
                               │          │
              ┌────────────────┘          └────────────────┐
              ▼                                            ▼
   ┌─────────────────┐                         ┌─────────────────┐
   │  📓 learning-log │◄────── all agents ─────│  🏥 healthcheck  │
   │  (Memory Layer)  │        report to        │ (Monitoring)     │
   └────────┬─────────┘                         └────────┬─────────┘
            │ feeds into                                  │ alerts
            ▼                                             ▼
   ┌─────────────────┐                         ┌─────────────────┐
   │ 🧬 self-evolving │                         │  🚨 fail2ban    │
   │   -skill         │                         │   -reporter     │
   │ (Auto-Patching)  │                         │ (Security)      │
   └──────────────────┘                         └─────────────────┘
```

## Architecture Tiers

### Tier 0 — Core Infrastructure (always running)
These agents keep the system itself alive. If they fail, everything degrades.

| Agent | Role | Schedule | Depends On |
|-------|------|----------|------------|
| healthcheck | System vitals monitoring | Every 6 hours | — (root) |
| backup | Data protection | Daily 3 AM HKT | healthcheck |
| fail2ban-reporter | Security monitoring | Every 6 hours | healthcheck |

### Tier 1 — Intelligence Layer (the brain)
These agents learn and improve the fleet. They process data from Tier 0 and all other agents.

| Agent | Role | Schedule | Depends On |
|-------|------|----------|------------|
| learning-log | Record all events, errors, corrections | Continuous + daily digest | All agents feed it |
| self-improving | Review & upgrade agents | Weekly (Mon 10 AM HKT) | learning-log |
| self-evolving-skill | Auto-patch broken skills | Daily 4 AM HKT | learning-log |
| skill-builder | Convert workflows to automations | On-demand | learning-log |

### Tier 2 — Automation Engine
These agents execute automated workflows. They can be chained together.

| Agent | Role | Schedule | Depends On |
|-------|------|----------|------------|
| auto-workflow | Pipeline orchestration | On-demand / event-driven | Tier 0 healthy |
| browser-automation | Web scraping, form filling | On-demand | — |
| ai-web-automation | Complex AI-driven web tasks | On-demand | browser-automation (fallback) |
| auto-deploy | CI/CD pipelines | On-demand / git push | github, healthcheck |
| auto-update | Dependency monitoring | Weekly (Sun 8 AM HKT) | healthcheck |
| remind-me | Scheduled reminders | Continuous | — |

### Tier 3 — Productivity Tools (user-facing)
Direct user interaction agents. These are the ones users talk to most.

| Agent | Role | Schedule | Depends On |
|-------|------|----------|------------|
| summarize | Content summarization | On-demand | agent-browser (for URLs) |
| file-summary | Document analysis | On-demand | — |
| multi-search-engine | Parallel search | On-demand | agent-browser |
| file-organizer | Filesystem cleanup | On-demand / weekly | — |
| humanizer | Text rewriting | On-demand | — |
| youtube-transcript | Video transcripts | On-demand | — |
| openai-whisper | Audio transcription | On-demand | — |

### Tier 4 — Domain Specialists
Agents focused on specific business domains.

| Agent | Role | Schedule | Depends On |
|-------|------|----------|------------|
| construction-news | APAC construction prospecting | Daily 9 AM HKT | agent-browser, multi-search-engine |
| gig | Freelance job finding | On-demand | multi-search-engine |
| find-skills | Talent discovery | On-demand | agent-browser, github |
| skill-vetter | Candidate/plugin assessment | On-demand | agent-browser |
| free-ride | Free tier/deal finding | On-demand | multi-search-engine |
| github | GitHub operations | On-demand | — |
| api-gateway | API design/debug | On-demand | — |
| docker-essential | Container management | On-demand | — |
| agent-browser | Web research | On-demand | — |

---

## Workflow Chains

### 🔄 Self-Improvement Loop (Weekly)

```
healthcheck ──→ learning-log ──→ self-improving ──→ self-evolving-skill
     │               │                │                     │
     │          reads errors     reviews fleet          patches skills
     │          + corrections    scores agents          updates deps
     │                           writes report
     │                                │
     └───────── posts to #self-improving on Discord ◄───┘
```

**Trigger:** Cron — Monday 10:00 AM HKT
**Steps:**
1. `healthcheck` → verify all systems healthy
2. `learning-log` → generate weekly digest of errors, corrections, wins
3. `self-improving` → read digest, score all agents, propose improvements
4. `self-evolving-skill` → check all skill dependencies, patch if needed
5. Report delivered to #self-improving channel

### 🛡️ Security Chain (Every 6 Hours)

```
healthcheck ──→ fail2ban-reporter ──→ backup (if threat detected)
     │                │                     │
  check ports    scan auth logs        snapshot data
  check services  check IPs            verify integrity
     │                │
     └──→ alert to #healthcheck / #fail2ban-reporter
```

**Trigger:** Cron — 00:00, 06:00, 12:00, 18:00 HKT
**Steps:**
1. `healthcheck` → system vitals + service status
2. `fail2ban-reporter` → security scan
3. If threat level HIGH → trigger `backup` immediately
4. Post combined report to Discord

### 📊 Content Pipeline (On-Demand)

```
User request ──→ agent-browser ──→ summarize ──→ humanizer
                      │                │              │
                 fetch content    distill key     rewrite to
                 from web        points           human voice
                                                      │
                                                      ▼
                                              Discord response
```

**Trigger:** User message in any channel
**Example:** "Find and summarize the top 3 articles about AI in construction"

### 🚀 Deploy Pipeline (On-Demand)

```
github ──→ auto-deploy ──→ healthcheck ──→ learning-log
   │            │               │               │
  PR merge   build+test    post-deploy      log result
  trigger    deploy         health check    success/fail
                │
          [on failure] ──→ rollback ──→ fail2ban-reporter
```

### 📁 File Processing Pipeline (On-Demand)

```
file-organizer ──→ file-summary ──→ summarize
       │                │               │
  sort/dedupe     extract data     create digest
  clean folders   analyze content  format report
```

### 💼 Prospecting Pipeline (Daily)

```
multi-search-engine ──→ agent-browser ──→ construction-news
         │                    │                  │
   search multiple      deep dive into      format as
   news sources         each finding        prospect list
                                                 │
                                                 ▼
                                    #construction-news on Discord
```

---

## Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ~/.openclaw/                               │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  learning-log/ (Central Knowledge Store)              │   │
│  │  ├── errors/          ← all agent errors              │   │
│  │  ├── corrections/     ← user corrections              │   │
│  │  ├── successes/       ← what worked well              │   │
│  │  ├── knowledge/       ← accumulated insights          │   │
│  │  └── reports/         ← weekly/monthly analysis       │   │
│  └──────────────────────────────────────────────────────┘   │
│       ▲ write                              ▼ read           │
│  ┌─────────┐  ┌─────────┐  ┌──────────────────────────┐   │
│  │ All 30  │  │ self-   │  │  self-evolving-skill     │   │
│  │ agents  │  │improving│  │  (reads logs, patches)    │   │
│  │ report  │  │ (reads, │  └──────────────────────────┘   │
│  │ errors  │  │ scores) │                                   │
│  └─────────┘  └─────────┘                                   │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  workspace-{agent}/ (Per-Agent Workspace)             │   │
│  │  ├── SOUL.md         ← agent instructions             │   │
│  │  ├── IDENTITY.md     ← agent persona                  │   │
│  │  └── {work files}    ← agent-specific data            │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Escalation Matrix

| Severity | Detection | First Responder | Escalation | Notification |
|----------|-----------|-----------------|------------|-------------|
| 🟢 Info | healthcheck | learning-log | — | #healthcheck (daily) |
| 🟡 Warning | healthcheck / any agent | self-improving | auto-update | #healthcheck (immediate) |
| 🔴 Critical | fail2ban-reporter / healthcheck | backup (snapshot) | self-improving | #fail2ban-reporter + #healthcheck |
| 💀 System Down | healthcheck fails | launchd auto-restart | — | macOS notification |

---

## Cron Schedule Summary

| Time (HKT) | Agent | Task | Channel |
|-------------|-------|------|---------|
| 03:00 Daily | backup | Full system backup | #backup |
| 04:00 Daily | self-evolving-skill | Dependency check + auto-patch | #self-evolving-skill |
| 06:00 Every 6h | healthcheck | System health scan | #healthcheck |
| 09:00 Daily | construction-news | APAC construction prospecting | #construction-news |
| 09:00 Daily | weather (launchd) | HK Fanling weather | #hk-weather |
| 09:30 Daily | learning-log | Daily digest of fleet activity | #learning-log |
| 10:00 Mon | self-improving | Weekly fleet review + scoring | #self-improving |
| 01:00 Every 6h | fail2ban-reporter | Security scan + audit | #fail2ban-reporter |
| 20:00 Sun | auto-update | Weekly dependency scan | #auto-update |

---

## Agent Communication Patterns

### Direct Invocation
Any agent can be called directly via:
```
openclaw agent --agent {id} --message "{task}" --deliver --channel discord --reply-to {channel-id}
```

### Chain Execution (via auto-workflow)
Define pipelines that call agents in sequence:
```
auto-workflow: [healthcheck] → [learning-log --message "generate digest"] → [self-improving --message "review fleet"]
```

### Event-Driven (via cron + conditions)
```
if healthcheck.status == "critical":
    trigger backup --message "emergency snapshot"
    trigger fail2ban-reporter --message "security audit"
```

### Shared Knowledge (via learning-log workspace)
All agents write to `~/.openclaw/workspace-learning-log/{type}/`
The self-improving agent reads from it during weekly reviews.


## Fleet Runner CLI

Located at `~/.openclaw/workspace-self-improving/fleet-runner.sh`

Run any workflow chain manually:
```bash
fleet-runner.sh self-improvement-loop
fleet-runner.sh security-chain
fleet-runner.sh content-pipeline "AI in construction 2025"
fleet-runner.sh deploy-pipeline
fleet-runner.sh morning-briefing
```

## Cron Job Registry

| ID (short) | Name | Agent | Schedule | Channel |
|------------|------|-------|----------|---------|
| 1179d571 | apac-construction-news | construction-news | 0 9 * * * | #construction-news |
| 92bfe172 | system-healthcheck | healthcheck | 0 0,6,12,18 * * * | #healthcheck |
| 69185e7e | security-scan | fail2ban-reporter | 0 1,7,13,19 * * * | #fail2ban-reporter |
| 1e099c7b | daily-backup | backup | 0 3 * * * | #backup |
| c0e845a0 | skill-evolution | self-evolving-skill | 0 4 * * * | #self-evolving-skill |
| 8070123b | daily-digest | learning-log | 30 9 * * * | #learning-log |
| 6da2e701 | weekly-dependency-scan | auto-update | 0 20 * * 0 | #auto-update |
| f26b355e | weekly-fleet-review | self-improving | 0 10 * * 1 | #self-improving |

All times in Asia/Hong_Kong timezone.
