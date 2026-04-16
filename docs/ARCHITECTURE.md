# Architecture Deep Dive

## System Overview

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR DISCORD SERVER                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │#summarize│ │#healthchk│ │#gig      │ │#backup   │  │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘  │
└───────┼─────────────┼────────────┼────────────┼─────────┘
        │             │            │            │
        ▼             ▼            ▼            ▼
┌─────────────────────────────────────────────────────────┐
│                  OPENCLAW GATEWAY                         │
│              (localhost:18789, token auth)                │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Agent Router                                      │   │
│  │  message → match agent → load SOUL.md → call LLM │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────┐  │
│  │ Cron Engine│  │ MCP Bridge │  │ Tool Executor    │  │
│  │ (9 jobs)   │  │ (Zalo OA)  │  │ (exec,read,web)  │  │
│  └────────────┘  └────────────┘  └──────────────────┘  │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                   AI MODEL PROVIDER                       │
│              (OpenAI-compatible API endpoint)             │
│                  gemini-3-flash-preview                   │
└─────────────────────────────────────────────────────────┘
```

## Agent Lifecycle

### 1. Message Arrives
User types in a Discord channel → Gateway identifies which agent owns that channel.

### 2. Context Loading
Gateway reads the agent's workspace:
- `SOUL.md` — personality, instructions, capabilities
- `IDENTITY.md` — who the agent is
- `PROTOCOLS.md` — shared fleet communication rules
- Previous conversation history

### 3. LLM Call
All context + user message → sent to AI model → response generated.

### 4. Tool Execution
If the agent needs to run commands, read files, or search the web, it uses tools:
- `exec` — run shell commands
- `read` — read files from disk
- `write` — create/edit files
- `web-search` — search the internet

### 5. Response Delivery
Agent's response → posted back to the Discord channel.

### 6. Learning
If the agent encounters errors or the user corrects it, logs are written to the shared learning-log workspace.

## Data Flow

```
All 31 Agents
     │
     ├── write errors ──────→ learning-log/errors/
     ├── write corrections ──→ learning-log/corrections/
     ├── write successes ───→ learning-log/successes/
     └── share knowledge ───→ learning-log/knowledge/
                                      │
                    ┌─────────────────┘
                    ▼
            self-improving (weekly)
                    │
                    ├── reads all logs
                    ├── scores each agent
                    ├── proposes improvements
                    └── triggers self-evolving-skill
                              │
                              └── patches broken skills
```

## Cron Architecture

```
┌─────────────────────────────────────────────────┐
│              OPENCLAW CRON ENGINE                │
│                                                  │
│  Evaluates schedule → creates isolated session   │
│  → runs agent with message → delivers to Discord │
│                                                  │
│  ┌─────────────────┐  ┌─────────────────┐      │
│  │ Every 6 hours   │  │ Daily           │      │
│  │ • healthcheck   │  │ • backup (3AM)  │      │
│  │ • fail2ban      │  │ • skill-evo(4AM)│      │
│  └─────────────────┘  │ • news (9AM)    │      │
│                        │ • digest(9:30)  │      │
│  ┌─────────────────┐  └─────────────────┘      │
│  │ Weekly          │                             │
│  │ • cleanup (Sat) │                             │
│  │ • deps (Sun)    │                             │
│  │ • review (Mon)  │                             │
│  └─────────────────┘                             │
└─────────────────────────────────────────────────┘
```
