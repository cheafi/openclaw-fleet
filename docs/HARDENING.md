# Hardening Guide (Recommended)

Use this after initial setup to reduce risk from prompt injection and over-broad tool access.

---

## 1) Run a baseline audit

```bash
openclaw security audit
```

If you need deeper diagnostics:

```bash
openclaw security audit --deep
```

---

## 2) Lock Discord routing policy

If your audit warns that `channels.discord.groupPolicy` is open, switch to allowlist mode:

```bash
openclaw config set channels.discord.groupPolicy "allowlist"
```

Why: with `open`, any new/unknown channel can become an execution surface.

---

## 3) Allowlist Discord users for slash commands

Set both global and per-guild allowlists:

```bash
openclaw config set channels.discord.allowFrom '["YOUR_DISCORD_USER_ID"]'
openclaw config set channels.discord.guilds.YOUR_GUILD_ID.users '["YOUR_DISCORD_USER_ID"]'
```

Why: removes the `native.no_allowlists` warning and prevents unapproved command use.

---

## 4) Restrict tool blast radius

Prefer tighter defaults for exposed agents:

```bash
openclaw config set agents.defaults.sandbox.mode "all"
openclaw config set tools.fs.workspaceOnly true
```

Why: reduces filesystem and runtime impact if a prompt is malicious.

---

## 5) Tighten credentials directory permissions

```bash
chmod 700 ~/.openclaw/credentials
```

Why: avoids local credential files being readable by other users on the machine.

---

## 6) Re-check status

```bash
openclaw status
openclaw security audit
```

---

## 7) Optional one-command baseline script

Run the repository hardening helper:

```bash
./scripts/harden-openclaw.sh
```

With explicit Discord allowlist values:

```bash
DISCORD_GUILD_ID="YOUR_GUILD_ID" \
DISCORD_USER_ID="YOUR_DISCORD_USER_ID" \
./scripts/harden-openclaw.sh
```

---

## 8) Operational cadence

- Run `openclaw security audit` weekly
- Rotate Discord token and API keys on suspected exposure
- Keep gateway loopback-only (`127.0.0.1`) unless you have proxy auth + TLS

---

## Notes

- This project intentionally favors local-first operation and transparent docs.
- For high-trust personal use, you may keep broader settings. For shared environments, apply all hardening steps above.