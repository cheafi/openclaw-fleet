#!/usr/bin/env python3
"""Post beginner onboarding messages to Discord channels.

- Creates one short starter message per channel
- Skips channels that already have the marker message
"""

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List

MARKER = "[OpenClaw Starter Guide]"

CHANNEL_HINTS: Dict[str, str] = {
    "一般": "General help and onboarding. Ask anything here if you're unsure where to start.",
    "hk-weather": "Daily weather updates. Try: `Weather update for today and tomorrow`",
    "construction-news": "APAC construction opportunities. Try: `Show projects above HKD 10M`",
    "healthcheck": "System diagnostics. Try: `Run full health check`",
    "backup": "Backup status. Try: `When was last successful backup?`",
    "fail2ban-reporter": "Security events. Try: `Any suspicious events in last 24 hours?`",
    "learning-log": "Daily learning digest. Try: `Summarize today's top learnings`",
    "self-improving": "Weekly improvement planner. Try: `Top 3 improvements this week`",
    "self-evolving-skill": "Skill patching status. Try: `Any broken dependencies?`",
    "skill-builder": "Build new skills. Try: `Turn this workflow into a reusable skill`",
    "auto-workflow": "Chain tasks across agents. Try: `Search, summarize, then humanize this topic`",
    "auto-deploy": "Deployment helper. Try: `Deploy latest main safely`",
    "auto-update": "Dependency audit. Try: `What should be updated this week?`",
    "browser-automation": "Web automation tasks. Try: `Collect prices from these pages`",
    "ai-web-automation": "Complex multi-step web tasks. Try: `Research competitors and summarize`",
    "zalo-events": "Zalo event invites/follow-up. Try: `Send reminder to event attendees`",
    "remind-me": "Reminders and scheduling. Try: `Remind me tomorrow 3pm to follow up`",
    "summarize": "Summarize links/text. Try: `Summarize this URL in 5 bullets`",
    "file-summary": "Analyze documents. Try: `Extract risks from this PDF`",
    "file-organizer": "Disk cleanup guidance. Try: `Find biggest folders in Downloads`",
    "multi-search-engine": "Cross-engine research. Try: `Compare top results for this query`",
    "humanizer": "Rewrite tone. Try: `Make this message more natural`",
    "youtube-transcript": "Extract transcripts. Try: `Get transcript from this YouTube URL`",
    "openai-whisper": "Audio transcription. Try: `Transcribe this meeting recording`",
    "gig": "Freelance opportunities. Try: `Find remote AI contracts in APAC`",
    "find-skills": "In-demand skills. Try: `Top skills for AI ops roles now`",
    "skill-vetter": "Tool/package checks. Try: `Is this package safe and maintained?`",
    "free-ride": "Free tiers and credits. Try: `List current free cloud credits`",
    "github": "GitHub operations. Try: `Summarize open PR risks`",
    "api-gateway": "API design/debug. Try: `Help design auth flow`",
    "docker-essential": "Container diagnostics. Try: `Why is this container restarting?`",
    "agent-browser": "Deep web research. Try: `Research this company and summarize`",
}


def cfg() -> Dict[str, Any]:
    path = os.path.expanduser("~/.openclaw/openclaw.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def api(token: str, method: str, path: str, body: Any = None):
    req = urllib.request.Request(
        f"https://discord.com/api/v10{path}",
        data=json.dumps(body).encode("utf-8") if body is not None else None,
        method=method,
    )
    req.add_header("Authorization", f"Bot {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "openclaw-fleet-onboarding/1.0")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read().decode("utf-8")
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        txt = e.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"{method} {path} failed: {e.code} {txt}") from e


def main() -> int:
    c = cfg()
    d = c["channels"]["discord"]
    token = d["token"]
    gid = next(iter(d["guilds"].keys()))

    channels = api(token, "GET", f"/guilds/{gid}/channels")
    texts = [x for x in channels if x.get("type") == 0]

    posted = 0
    skipped = 0

    for ch in texts:
        name = ch.get("name", "")
        hint = CHANNEL_HINTS.get(name)
        if not hint:
            continue

        # check recent messages for marker
        cid = ch["id"]
        msgs = api(token, "GET", f"/channels/{cid}/messages?limit=20")
        found = False
        for m in msgs:
            content = (m.get("content") or "")
            if MARKER in content:
                found = True
                break

        if found:
            skipped += 1
            continue

        msg = (
            f"{MARKER}\n"
            f"👋 **How to use #{name}**\n"
            f"{hint}\n\n"
            f"If you are new, start in **#一般** and ask for a workflow."
        )
        api(token, "POST", f"/channels/{cid}/messages", {"content": msg})
        posted += 1

    print(f"Posted onboarding messages: {posted}")
    print(f"Skipped (already exists): {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
