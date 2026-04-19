# Use Cases

Real-world scenarios showing how to use the agent fleet.

---

## 🏗️ Construction Sales Prospecting

**Scenario:** You're in construction sales and need daily leads.

**Setup:** Already automated! Every morning at 9 AM:
- `#construction-news` posts APAC construction opportunities
- Includes project names, values, locations, and tender deadlines

**Enhance it:**
```
In #construction-news: "Focus on Hong Kong government projects above HKD 10M"
In #agent-browser: "Research the developer behind the Kai Tak project"
In #summarize: "Summarize this tender document: [URL]"
```

---

## 💼 Job Hunting

**Scenario:** You're looking for a new role.

```
In #gig: "Find AI/ML engineer positions in Singapore, remote-friendly, $80k+"

In #humanizer: "Rewrite my cover letter to sound more natural:
Dear Hiring Manager, I am writing to express my interest..."

In #summarize: "Summarize this job description and list the key requirements: [URL]"

In #skill-vetter: "What skills are most in-demand for AI engineering in 2026?"
```

---

## 🎥 Content Creation

**Scenario:** You create YouTube videos or write articles.

```
In #youtube-transcript: "Get the transcript of this video: https://youtube.com/watch?v=..."

In #summarize: "Turn this 45-minute transcript into a 5-point summary"

In #humanizer: "Rewrite these bullet points as a blog post introduction"

In #multi-search-engine: "Find the latest statistics on AI adoption in Asia"
```

---

## 🔒 System Administration

**Scenario:** You want to keep your Mac secure and clean.

**Already automated:**
- Security scans every 6 hours → `#fail2ban-reporter`
- Health checks every 6 hours → `#healthcheck`
- Daily backups at 3 AM → `#backup`
- Weekly disk cleanup → `#file-organizer`
- Weekly dependency updates → `#auto-update`

**Manual checks:**
```
In #healthcheck: "Full system report"
In #file-organizer: "What's using the most disk space?"
In #docker-essential: "Show me all running containers and their resource usage"
```

---

## 🇻🇳 Event Marketing (Vietnam)

**Scenario:** You're hosting a business event and need to invite contacts via Zalo.

```
In #zalo-events: "Create event: AI Workshop, April 30, 2PM, Ho Chi Minh City"

In #zalo-events: "Add contact list:
- Nguyen Van A: 0912345678
- Tran Thi B: 0923456789"

In #zalo-events: "Send invitations"

(3 days before event)
In #zalo-events: "Send reminders"

(After event)
In #zalo-events: "Send thank you and survey link"
```

---

## 📚 Research & Learning

**Scenario:** You're researching a new technology.

```
In #multi-search-engine: "Search for 'MCP protocol AI agents' across Google, Bing, and DuckDuckGo"

In #agent-browser: "Go to https://docs.openclaw.ai and summarize the API documentation"

In #summarize: "Compare these 3 articles and list the common themes:
1. [url1]
2. [url2]
3. [url3]"

In #github: "Find the most starred repos for 'AI agent framework' created in 2026"
```

---

## 🆓 Saving Money

**Scenario:** You want to find free tools and credits.

```
In #free-ride: "What free AI API credits are available right now?"

In #free-ride: "Find free cloud hosting tiers for a Node.js app"

In #free-ride: "List all free developer tools I should be using"
```

---

## 🔄 The Self-Improving Loop

> ⚠️ **Experimental.** This loop runs automatically but has no feedback metric yet — it produces suggestions, not validated improvements.

Every week on Monday at 10 AM:
1. `self-improving` reviews the fleet's agent configs
2. Reads the learning log for errors and corrections
3. Scores each agent and proposes improvements
4. `self-evolving-skill` patches any broken dependencies

Check the results in `#self-improving` every Monday morning. Treat the output as suggestions to review, not automatic upgrades.

---

## 🔗 Workflow Chains (fleet-runner)

**Scenario:** You want to run multi-agent pipelines with one command.

```bash
# Research a topic → summarize → rewrite in natural tone
./scripts/fleet-runner.sh content-pipeline "latest AI agent frameworks"

# Morning briefing: health + news + digest
./scripts/fleet-runner.sh morning-briefing

# Security audit: healthcheck + fail2ban scan
./scripts/fleet-runner.sh security-chain

# Weekly self-review: health → learning-log → score → patch
./scripts/fleet-runner.sh self-improvement-loop
```

Set `CHANNEL_*` env vars first — see `.env.example`.

---

## 📋 Daily Operations Checklist

A suggested daily routine using the fleet:

| Time | Action | Channel |
|------|--------|---------|
| 9:00 AM | Check morning briefing (auto) | `#construction-news`, `#hk-weather` |
| 9:30 AM | Review learning digest (auto) | `#learning-log` |
| As needed | Summarize articles / URLs | `#summarize` |
| As needed | Research topics | `#multi-search-engine`, `#agent-browser` |
| As needed | Find gigs | `#gig` |
| 6-hourly | Review health reports (auto) | `#healthcheck` |
| Saturday | Review cleanup proposal (auto) | `#file-organizer` |
| Monday | Review improvement proposals (auto) | `#self-improving` |
