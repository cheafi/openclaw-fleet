# Security Policy

## Scope

This repo contains agent personality files (`SOUL.md`, `IDENTITY.md`), utility scripts, and docs for running an OpenClaw agent fleet. It does **not** contain any real credentials — and must never contain them.

---

## ⚠️ Critical: Agent execution risk

**Agents with the `exec` tool can run arbitrary shell commands on your machine.** This is the single biggest security consideration.

### What this means

When you deploy a `SOUL.md` that includes the `exec` tool, you are giving an LLM the ability to run shell commands as your user. A prompt injection attack — where a malicious input tricks the agent into running unintended commands — is a real risk.

### Agent permissions matrix

| Agent | exec | read | write | web | Risk level |
|-------|------|------|-------|-----|------------|
| summarize | ❌ | ✅ | ❌ | ✅ | Low |
| healthcheck | ✅ | ✅ | ❌ | ✅ | Medium |
| file-organizer | ✅ | ✅ | ✅ | ❌ | **High** |
| gig | ❌ | ❌ | ❌ | ✅ | Low |
| learning-log | ❌ | ✅ | ✅ | ❌ | Low |
| self-improving | ❌ | ✅ | ✅ | ❌ | Medium |
| zalo-events | ✅ | ❌ | ❌ | ✅ | Medium |

### Mitigations

1. **Run `./scripts/harden-openclaw.sh`** — enables sandbox mode and workspace-only filesystem
2. **Review every `SOUL.md`** before deploying — treat it as code, not just a prompt
3. **Enable `tools.fs.workspaceOnly: true`** — prevents agents from accessing files outside their workspace
4. **Use `channels.discord.groupPolicy: "allowlist"`** — restricts who can talk to agents
5. **Set API spending limits** — prevents runaway costs from prompt injection loops

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

## Reporting a vulnerability

This is a personal project, not a commercial product. If you find a security issue:

1. **Do not open a public issue** if it involves credentials, tokens, or exploitable logic
2. Open a [GitHub issue](https://github.com/cheafi/openclaw-fleet/issues) marked as `[SECURITY]` in the title for general security guidance improvements
3. For anything sensitive, email the repo owner directly via their GitHub profile

---

## Checklist before sharing

- [ ] `~/.openclaw/openclaw.json` is not tracked by git
- [ ] No `.env` files with real values are tracked
- [ ] `git log --all --full-history -- "*.env"` shows no leaked env files in history
- [ ] `git grep -iE "sk-[a-zA-Z0-9]{20,}|MTQ[a-zA-Z0-9]{50,}"` returns nothing
- [ ] Discord bot permissions are minimal (not Administrator)
- [ ] `./scripts/harden-openclaw.sh` has been run
