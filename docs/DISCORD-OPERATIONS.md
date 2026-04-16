# Discord Operations

Operational runbook for the OpenClaw Fleet Discord server.

---

## Canonical structure

Use the layout documented in [README.md](../README.md) under **Discord layout (canonical)**.

To enforce it programmatically:

```bash
python3 scripts/discord-sync.py          # audit only
python3 scripts/discord-sync.py --apply  # create/move channels
```

---

## Health checks

```bash
openclaw status
openclaw channels status --probe
openclaw directory groups list --channel discord
```

Expected:
- Discord channel state should be `OK`
- Gateway should be reachable on `ws://127.0.0.1:18789`

---

## Least-privilege Discord bot setup

Bot permissions should be limited to:
- Send Messages
- Read Message History
- Manage Channels

Avoid Administrator and broad server-management scopes.

---

## Common operational tasks

### Move a channel to the right category
Preferred: run sync script.

```bash
python3 scripts/discord-sync.py --apply
```

### Post beginner usage messages in every channel

```bash
python3 scripts/discord-post-onboarding.py
```

This posts one starter message per channel with a simple "what this bot does"
description and an example prompt.

### Verify channel mapping for an agent
1. Confirm channel ID in `~/.openclaw/openclaw.json`
2. Right-click Discord channel → Copy Channel ID
3. IDs must match exactly

### If bot stops responding
1. Check gateway process:
   ```bash
   openclaw gateway status
   ```
2. Restart gateway:
   ```bash
   openclaw gateway restart
   ```
3. Check status again:
   ```bash
   openclaw status
   ```

---

## Change policy

- Do not delete channels in bulk without backup
- Prefer additive updates (create/move)
- Keep channel names stable once mapped in `openclaw.json`
- If a rename is needed, update both Discord and `openclaw.json` in the same change
