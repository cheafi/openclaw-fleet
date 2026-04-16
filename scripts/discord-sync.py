#!/usr/bin/env python3
"""
Ensure Discord categories/channels match the canonical OpenClaw Fleet layout.

Default mode: dry-run (no changes)
Apply mode:   --apply (create/move channels)
"""

import argparse
import json
import os
import urllib.error
import urllib.request
from typing import Dict, List, Any

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


def load_cfg() -> Dict[str, Any]:
    cfg_path = os.path.expanduser("~/.openclaw/openclaw.json")
    with open(cfg_path, "r", encoding="utf-8") as f:
        return json.load(f)


def api_req(token: str, method: str, path: str, payload: Any = None):
    base = "https://discord.com/api/v10"
    req = urllib.request.Request(
        base + path,
        data=(json.dumps(payload).encode("utf-8") if payload is not None else None),
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Create/move channels")
    args = parser.parse_args()

    cfg = load_cfg()
    discord = cfg.get("channels", {}).get("discord", {})
    token = discord.get("token")
    guilds = discord.get("guilds", {})

    if not token:
        raise SystemExit("Discord token not found in ~/.openclaw/openclaw.json")
    if not guilds:
        raise SystemExit("No Discord guild configured in ~/.openclaw/openclaw.json")

    guild_id = next(iter(guilds.keys()))
    channels = api_req(token, "GET", f"/guilds/{guild_id}/channels")

    categories = {c["name"]: c for c in channels if c.get("type") == 4}
    texts = {c["name"]: c for c in channels if c.get("type") == 0}

    missing_categories = [c for c in EXPECTED_LAYOUT if c not in categories]
    missing_channels = []
    misplaced_channels = []

    for cat, names in EXPECTED_LAYOUT.items():
        for name in names:
            ch = texts.get(name)
            if ch is None:
                missing_channels.append((cat, name))
            elif cat in categories and ch.get("parent_id") != categories[cat]["id"]:
                misplaced_channels.append((cat, name))

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
            categories[c] = created

    channels = api_req(token, "GET", f"/guilds/{guild_id}/channels")
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
                    },
                )
            elif existing.get("parent_id") != cat_id:
                api_req(token, "PATCH", f"/channels/{existing['id']}", {"parent_id": cat_id})

    print("\nApply complete. Discord layout synced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
