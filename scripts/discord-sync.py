#!/usr/bin/env python3
"""
Ensure Discord categories/channels match the canonical OpenClaw Fleet layout
and beginner-friendly channel descriptions.

Default mode: dry-run (no changes)
Apply mode:   --apply (create/move channels + set topics)
"""

import argparse
import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, List

EXPECTED_LAYOUT: Dict[str, List[str]] = {
    "☕ Welcome": ["一般"],
    "📡 Daily Briefings": ["hk-weather", "construction-news"],
    "⚙️ Core Systems": [
        "healthcheck",
        "backup",
        "fail2ban-reporter",
        "learning-log",
        "self-improving",
        "self-evolving-skill",
        "skill-builder",
    ],
    "⚡ Automation": [
        "auto-workflow",
        "auto-deploy",
        "auto-update",
        "browser-automation",
        "ai-web-automation",
        "zalo-events",
        "remind-me",
    ],
    "📋 Productivity": [
        "summarize",
        "file-summary",
        "file-organizer",
        "multi-search-engine",
        "humanizer",
        "youtube-transcript",
        "openai-whisper",
    ],
    "💼 Work & Research": [
        "gig",
        "find-skills",
        "skill-vetter",
        "free-ride",
        "github",
        "api-gateway",
        "docker-essential",
        "agent-browser",
    ],
}

CHANNEL_TOPICS: Dict[str, str] = {
    "一般": (
        "General help and onboarding. "
        "Ask anything about how to use this AI fleet."
    ),
    "hk-weather": (
        "Daily Hong Kong weather briefing. "
        "Ask: 'Weather update for today and tomorrow'."
    ),
    "construction-news": (
        "Daily APAC construction opportunities. "
        "Ask: 'Show projects above HKD 10M'."
    ),
    "healthcheck": (
        "System diagnostics and uptime checks. "
        "Ask: 'Run full health check'."
    ),
    "backup": (
        "Backup status and recovery guidance. "
        "Ask: 'When was the last backup?'."
    ),
    "fail2ban-reporter": (
        "Security event summary and suspicious activity checks."
    ),
    "learning-log": (
        "Daily summary of what agents learned "
        "and where they failed/succeeded."
    ),
    "self-improving": "Weekly fleet review and improvement proposals.",
    "self-evolving-skill": "Dependency and skill patching status.",
    "skill-builder": (
        "Design and scaffold new OpenClaw skills "
        "from your workflow ideas."
    ),
    "auto-workflow": "Chain multiple agents into one repeatable workflow.",
    "auto-deploy": "Deployment automation for repos and app updates.",
    "auto-update": "Dependency audit and update recommendations.",
    "browser-automation": (
        "Automate browser tasks like scraping, "
        "form fill, and repetitive web steps."
    ),
    "ai-web-automation": (
        "Complex AI-assisted web workflows and multi-step tasks."
    ),
    "zalo-events": (
        "Zalo personal-account event invitations "
        "and follow-up messages."
    ),
    "remind-me": (
        "Set reminders and scheduling prompts. "
        "Example: 'Remind me tomorrow 3pm'."
    ),
    "summarize": "Summarize URLs, long text, and documents into key points.",
    "file-summary": (
        "Analyze local files (PDF, docs) "
        "and extract actionable insights."
    ),
    "file-organizer": "Disk cleanup and file organization suggestions.",
    "multi-search-engine": (
        "Search across multiple engines and combine findings."
    ),
    "humanizer": "Rewrite robotic text into more natural, human tone.",
    "youtube-transcript": "Extract transcript from YouTube links.",
    "openai-whisper": "Transcribe audio files into text.",
    "gig": "Find freelance/contract opportunities by your filters.",
    "find-skills": "Discover in-demand skills and profile requirements.",
    "skill-vetter": "Evaluate tools, candidates, or packages before use.",
    "free-ride": "Find free tiers, credits, and cost-saving options.",
    "github": "GitHub operations: PR review, issues, release workflow.",
    "api-gateway": "API design, debugging, and integration guidance.",
    "docker-essential": (
        "Container checks, diagnostics, "
        "and best-practice fixes."
    ),
    "agent-browser": "Deep web research and competitive analysis.",
}


def load_cfg() -> Dict[str, Any]:
    cfg_path = os.path.expanduser("~/.openclaw/openclaw.json")
    with open(cfg_path, "r", encoding="utf-8") as f:
        return json.load(f)


def api_req(token: str, method: str, path: str, payload: Any = None):
    base = "https://discord.com/api/v10"
    req = urllib.request.Request(
        base + path,
        data=(
            json.dumps(payload).encode("utf-8")
            if payload is not None
            else None
        ),
        method=method,
    )
    req.add_header("Authorization", f"Bot {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "openclaw-fleet-discord-sync/1.0")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else None
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"{method} {path} -> {e.code}: {body}") from e


def as_list(value: Any) -> List[Dict[str, Any]]:
    """Normalize unknown API responses to a list of dict items."""
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Create/move channels and set descriptions",
    )
    args = parser.parse_args()

    cfg = load_cfg()
    discord = cfg.get("channels", {}).get("discord", {})
    token = discord.get("token")
    guilds = discord.get("guilds", {})

    if not token:
        raise SystemExit(
            "Discord token not found in ~/.openclaw/openclaw.json"
        )
    if not guilds:
        raise SystemExit(
            "No Discord guild configured in ~/.openclaw/openclaw.json"
        )

    guild_id = next(iter(guilds.keys()))
    channels = as_list(api_req(token, "GET", f"/guilds/{guild_id}/channels"))

    categories = {c["name"]: c for c in channels if c.get("type") == 4}
    texts = {c["name"]: c for c in channels if c.get("type") == 0}

    missing_categories = [c for c in EXPECTED_LAYOUT if c not in categories]
    missing_channels = []
    misplaced_channels = []
    topic_updates = []

    for cat, names in EXPECTED_LAYOUT.items():
        for name in names:
            ch = texts.get(name)
            if ch is None:
                missing_channels.append((cat, name))
            elif (
                cat in categories
                and ch.get("parent_id") != categories[cat]["id"]
            ):
                misplaced_channels.append((cat, name))
            if ch is not None and name in CHANNEL_TOPICS:
                current_topic = (ch.get("topic") or "").strip()
                desired_topic = CHANNEL_TOPICS[name].strip()
                if current_topic != desired_topic:
                    topic_updates.append(name)

    print("Discord layout audit")
    print("- Missing categories:", len(missing_categories))
    for c in missing_categories:
        print("  +", c)

    print("- Missing channels:", len(missing_channels))
    for cat, ch in missing_channels:
        print(f"  + #{ch} (under {cat})")

    print("- Misplaced channels:", len(misplaced_channels))
    for cat, ch in misplaced_channels:
        print(f"  ~ #{ch} (should be under {cat})")

    print("- Topic updates needed:", len(topic_updates))
    for ch in topic_updates:
        print(f"  * #{ch}")

    if not args.apply:
        print("\nDry-run complete. Re-run with --apply to fix.")
        return 0

    # Apply fixes
    for pos, c in enumerate(EXPECTED_LAYOUT.keys()):
        if c not in categories:
            created = api_req(
                token,
                "POST",
                f"/guilds/{guild_id}/channels",
                {"name": c, "type": 4, "position": pos},
            )
            if isinstance(created, dict):
                categories[c] = created

    channels = as_list(api_req(token, "GET", f"/guilds/{guild_id}/channels"))
    categories = {c["name"]: c for c in channels if c.get("type") == 4}
    texts = {c["name"]: c for c in channels if c.get("type") == 0}

    for cat, names in EXPECTED_LAYOUT.items():
        cat_id = categories[cat]["id"]
        for idx, name in enumerate(names):
            existing = texts.get(name)
            if existing is None:
                api_req(
                    token,
                    "POST",
                    f"/guilds/{guild_id}/channels",
                    {
                        "name": name,
                        "type": 0,
                        "parent_id": cat_id,
                        "position": idx,
                        "topic": CHANNEL_TOPICS.get(name, ""),
                    },
                )
            elif existing.get("parent_id") != cat_id:
                api_req(
                    token,
                    "PATCH",
                    f"/channels/{existing['id']}",
                    {"parent_id": cat_id},
                )

    # Refresh and apply channel topics/descriptions.
    channels = as_list(api_req(token, "GET", f"/guilds/{guild_id}/channels"))
    texts = {c["name"]: c for c in channels if c.get("type") == 0}
    updated_topics = 0
    for name, desired_topic in CHANNEL_TOPICS.items():
        ch = texts.get(name)
        if ch is None:
            continue
        current_topic = (ch.get("topic") or "").strip()
        if current_topic != desired_topic.strip():
            api_req(
                token,
                "PATCH",
                f"/channels/{ch['id']}",
                {"topic": desired_topic},
            )
            updated_topics += 1

    print(
        "\nApply complete. Discord layout synced. "
        f"Topics updated: {updated_topics}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
