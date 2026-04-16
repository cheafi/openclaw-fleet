# SHARED PROTOCOLS — Inter-Agent Communication Standards

All 30 agents in the fleet follow these protocols for communication, error reporting, and knowledge sharing.

## 1. Error Reporting Protocol

When any agent encounters an error, it MUST write a log entry to the learning-log workspace:

**File:** `~/.openclaw/workspace-learning-log/errors/{YYYY-MM-DD}-{your-agent-id}-{short-hash}.json`

```json
{
  "timestamp": "ISO-8601",
  "agent": "your-agent-id",
  "type": "error",
  "severity": "info|warning|critical",
  "context": "what task you were performing",
  "error_message": "the actual error",
  "root_cause": "your analysis of why",
  "attempted_fix": "what you tried",
  "resolved": true/false,
  "lesson": "what to do differently",
  "tags": ["category1", "category2"]
}
```

## 2. Correction Logging Protocol

When a user corrects your output:

**File:** `~/.openclaw/workspace-learning-log/corrections/{YYYY-MM-DD}-{your-agent-id}-{short-hash}.json`

```json
{
  "timestamp": "ISO-8601",
  "agent": "your-agent-id",
  "type": "correction",
  "original_output": "what you said",
  "correction": "what the user wanted instead",
  "root_cause": "why you got it wrong",
  "pattern": "general pattern to avoid",
  "tags": ["tone", "accuracy", "format", "hallucination"]
}
```

## 3. Success Logging Protocol

When something works well or a user expresses satisfaction:

**File:** `~/.openclaw/workspace-learning-log/successes/{YYYY-MM-DD}-{your-agent-id}-{short-hash}.json`

```json
{
  "timestamp": "ISO-8601",
  "agent": "your-agent-id",
  "type": "success",
  "task": "what you did",
  "why_successful": "what made it work",
  "reusable_pattern": "extractable technique for other agents",
  "tags": ["efficiency", "accuracy", "user-satisfaction"]
}
```

## 4. Agent Handoff Protocol

When you need another agent to continue your work:

```
Request format in your response:
@handoff:{target-agent-id} — {task description}

Example:
@handoff:summarize — Please summarize the 5 articles I just fetched about AI in construction.
```

The orchestration layer (auto-workflow or fleet-runner) will route this.

## 5. Escalation Protocol

| Your Severity | Action |
|---------------|--------|
| 🟢 Info | Log to learning-log, continue |
| 🟡 Warning | Log + mention in next digest |
| 🔴 Critical | Log + trigger healthcheck + alert #healthcheck channel |
| 💀 System Down | Log + trigger backup + alert all monitoring channels |

To escalate, write to: `~/.openclaw/workspace-learning-log/errors/` with `"severity": "critical"`

## 6. Knowledge Sharing Protocol

When you discover something useful for other agents:

**File:** `~/.openclaw/workspace-learning-log/knowledge/{topic}-{short-hash}.json`

```json
{
  "timestamp": "ISO-8601",
  "contributed_by": "your-agent-id",
  "topic": "descriptive topic name",
  "insight": "the knowledge to share",
  "applicable_to": ["agent-id-1", "agent-id-2"],
  "tags": ["api", "prompt", "workflow", "tool"]
}
```

## 7. Status Reporting Protocol

Every agent should include a status footer in scheduled/cron outputs:

```
---
⏱ Duration: Xs | 🧠 Model: gemini-3-flash-preview | 📊 Tokens: N
📁 Logs: {count} new entries written to learning-log
🔗 Next: {next-scheduled-run or "on-demand"}
```

## 8. Channel Routing Map

| Agent | Primary Channel | Escalation Channel |
|-------|----------------|-------------------|
| healthcheck | #healthcheck | — (root) |
| backup | #backup | #healthcheck |
| fail2ban-reporter | #fail2ban-reporter | #healthcheck |
| learning-log | #learning-log | #self-improving |
| self-improving | #self-improving | #healthcheck |
| self-evolving-skill | #self-evolving-skill | #self-improving |
| skill-builder | #skill-builder | #self-improving |
| auto-workflow | #auto-workflow | #healthcheck |
| browser-automation | #browser-automation | #auto-workflow |
| ai-web-automation | #ai-web-automation | #auto-workflow |
| auto-deploy | #auto-deploy | #healthcheck |
| auto-update | #auto-update | #healthcheck |
| remind-me | #remind-me | — |
| summarize | #summarize | — |
| file-summary | #file-summary | — |
| multi-search-engine | #multi-search-engine | — |
| file-organizer | #file-organizer | — |
| humanizer | #humanizer | — |
| youtube-transcript | #youtube-transcript | — |
| openai-whisper | #openai-whisper | — |
| construction-news | #construction-news | #agent-browser |
| gig | #gig | #multi-search-engine |
| find-skills | #find-skills | #agent-browser |
| skill-vetter | #skill-vetter | #agent-browser |
| free-ride | #free-ride | #multi-search-engine |
| github | #github | — |
| api-gateway | #api-gateway | — |
| docker-essential | #docker-essential | #healthcheck |
| agent-browser | #agent-browser | — |

## 9. Fleet Registry

Total: 30 agents across 7 categories.

**Core Infrastructure:** healthcheck, backup, fail2ban-reporter
**Intelligence:** learning-log, self-improving, self-evolving-skill, skill-builder
**Automation:** auto-workflow, browser-automation, ai-web-automation, auto-deploy, auto-update, remind-me
**Productivity:** summarize, file-summary, multi-search-engine, file-organizer, humanizer, youtube-transcript, openai-whisper
**Domain Specialists:** construction-news, gig, find-skills, skill-vetter, free-ride
**Developer Tools:** github, api-gateway, docker-essential
**Research:** agent-browser
