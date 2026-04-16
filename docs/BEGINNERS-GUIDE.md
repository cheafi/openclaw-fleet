# Beginner's Guide

## I'm Not Technical — Can I Still Use This?

**Yes!** Once the fleet is set up, you interact with everything through Discord. No coding needed.

Think of each Discord channel as a different assistant sitting at a desk. You walk up to the right desk and ask your question.

---

## How to Talk to an Agent

### Step 1: Open Discord
Open your Discord server where the bot is installed.

### Step 2: Find the Right Channel
Look at the categories on the left sidebar:

- **Need to summarize something?** → Go to `#summarize`
- **Need a reminder?** → Go to `#remind-me`
- **Want to find freelance work?** → Go to `#gig`
- **Want to clean up your files?** → Go to `#file-organizer`

### Step 3: Just Type
Type your request in plain English (or any language). The agent will respond.

**Example:**
```
You: Summarize this article https://example.com/ai-news
Bot: Here's a summary of the article...
     Key Points:
     1. ...
     2. ...
     3. ...
```

---

## What Each Category Does

### ☕ Welcome
General chat. Say hi, ask questions, test things.

### 📡 Daily Briefings
**These are automatic** — you don't need to do anything. Every morning at 9 AM HKT:
- `#hk-weather` posts the Fanling, Hong Kong weather
- `#construction-news` posts APAC construction industry opportunities

### ⚙️ Core Systems
**These run in the background** keeping everything healthy:
- `#healthcheck` — checks if everything is working (every 6 hours)
- `#backup` — backs up your config files (daily at 3 AM)
- `#fail2ban-reporter` — security monitoring (every 6 hours)
- `#learning-log` — records what all agents learn (daily digest at 9:30 AM)
- `#self-improving` — reviews the whole fleet and suggests upgrades (weekly Monday 10 AM)

**You can also ask them directly:**
```
In #healthcheck: "Is everything okay?"
In #backup: "When was the last backup?"
```

### ⚡ Automation
Agents that do things automatically:
- `#auto-workflow` — chain multiple agents together
- `#auto-deploy` — deploy code
- `#auto-update` — check for software updates (weekly Sunday 8 PM)
- `#browser-automation` — scrape websites, fill forms
- `#zalo-events` — send Zalo invitations for events
- `#remind-me` — "Remind me to buy groceries tomorrow at 5pm"

### 📋 Productivity
Your daily helpers:
- `#summarize` — "Summarize this: [paste text or URL]"
- `#file-summary` — "Analyze this PDF for me"
- `#file-organizer` — "Clean up my Downloads folder" (also auto weekly)
- `#multi-search-engine` — "Search for best AI tools 2026"
- `#humanizer` — "Make this sound natural: [paste robotic text]"
- `#youtube-transcript` — "Get transcript: [YouTube URL]"
- `#openai-whisper` — "Transcribe this audio file"

### 💼 Work & Research
For business and professional use:
- `#gig` — "Find remote AI engineering jobs in Asia"
- `#find-skills` — "Who are the top Rust developers on GitHub?"
- `#skill-vetter` — "Is this npm package safe to use?"
- `#free-ride` — "What free cloud credits are available?"
- `#github` — "Show my open PRs"
- `#api-gateway` — "Help me design a REST API for user auth"
- `#docker-essential` — "List running containers"
- `#agent-browser` — "Research competitors in Hong Kong construction tech"

---

## Common Questions

### Q: Do I need to keep my computer on?
**Yes**, the gateway runs on your Mac. If you close it, agents stop responding. The gateway auto-starts on boot via macOS LaunchAgent.

### Q: Is my data private?
**Yes.** Everything runs locally. The only external call is to your AI model provider. No data is sent to OpenClaw or anyone else.

### Q: Can I add my own agents?
**Yes!** Create a workspace folder with a SOUL.md file describing what the agent should do, register it in the config, and create a Discord channel for it.

### Q: What if an agent gives a wrong answer?
Just correct it in the chat. The learning-log agent records corrections so the fleet improves over time.

### Q: How much does it cost?
- **OpenClaw**: Free and open source
- **AI Model**: Depends on your provider (the setup uses a custom endpoint)
- **Discord**: Free
- **Total**: Just your AI API costs

---

## Tips & Tricks

1. **Be specific** — Instead of "find jobs", say "Find remote Python developer jobs paying >$50/hr in Asia Pacific"
2. **Use the right channel** — Each agent is specialized. Don't ask #healthcheck to summarize articles.
3. **Check #learning-log** — See what your agents have been up to each day.
4. **Let it learn** — The more you use and correct agents, the better they get.
5. **Chain agents** — Ask one agent to pass work to another: "Search for articles about AI, then summarize the top 3"
