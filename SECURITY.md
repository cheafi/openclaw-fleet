# Security Policy

## Scope

This repo contains example configuration files, agent personality files (`SOUL.md`, `IDENTITY.md`), and utility scripts for running an OpenClaw agent fleet. It does **not** contain any real credentials, tokens, or API keys — and must never contain them.

---

## Sensitive files — never commit these

| File | Why it is sensitive |
|------|---------------------|
| `~/.openclaw/openclaw.json` | Contains your Discord bot token and AI model API key |
| `~/.openclaw/skill-secrets.env` | Contains skill API keys (IMAP, Notion, etc.) |
| `~/.openclaw/zalo-session/credentials.json` | Contains your Zalo session cookie |
| Any `*.env` file with real values | Contains service credentials |

These are already listed in `.gitignore`. Do not override or bypass the ignore rules.

---

## Credential handling guidance

### Discord bot token
- Use least-privilege permissions: `Send Messages`, `Read Message History`, `Manage Channels`
- Do **not** grant Administrator, Manage Guild, or Manage Roles
- Rotate your token immediately if you suspect it was exposed (Discord Developer Portal → Bot → Reset Token)

### AI model API key
- Use a separate API key for this fleet, not your main personal key
- Set spending limits on your API provider dashboard
- Rotate the key if it is ever committed or leaked

### Gmail App Password (imap-smtp-email skill)
- Use an App Password, not your main Google account password
- App Passwords can be revoked individually at https://myaccount.google.com/apppasswords
- Enable 2FA on your Google account before creating App Passwords

### Zalo session credentials
- The `zca-js` bridge uses an unofficial API — Zalo may rate-limit or block your account if overused
- The session cookie is stored at `~/.openclaw/zalo-session/credentials.json` — treat it as a password
- Do not automate mass-messaging; use for genuine event follow-ups only

---

## Gateway security

- The OpenClaw gateway binds to `localhost:18789` only
- Do **not** expose this port via reverse proxy, ngrok, or firewall rules unless you have added authentication
- If you must expose the gateway externally, add IP allowlisting and TLS termination first

---

## Agent execution security

Agents can run shell commands via the `exec` tool. Before deploying an agent:
1. Read its `SOUL.md` — especially the Tools and Instructions sections
2. Confirm it only accesses paths and commands you intend
3. Avoid agents that write to system directories or run as root

---

## Reporting a vulnerability

This is a personal project, not a commercial product. If you find a security issue:

1. **Do not open a public issue** if it involves credentials, tokens, or exploitable logic
2. Open a [GitHub issue](https://github.com/cheafi/openclaw-fleet/issues) marked as `[SECURITY]` in the title for general security guidance improvements
3. For anything sensitive, email the repo owner directly via their GitHub profile

---

## Checklist before making the repo public or sharing it

- [ ] `~/.openclaw/openclaw.json` is not tracked by git (`git status` should not show it)
- [ ] No `.env` files with real values are tracked
- [ ] `git log --all --full-history -- "*.env"` shows no leaked env files in history
- [ ] `git grep -i "token\|apikey\|password\|secret"` returns only placeholder values
- [ ] Discord bot permissions are minimal (not Administrator)
