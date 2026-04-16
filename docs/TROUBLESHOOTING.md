# Troubleshooting

Common errors and how to fix them.

---

## Gateway won't start

**Symptom:** `openclaw gateway start` hangs or returns an error immediately.

**Check 1 — Config is valid:**
```bash
openclaw config check
```
If it reports an error, check `~/.openclaw/openclaw.json` for:
- Invalid JSON syntax (trailing commas, missing brackets)
- Unknown property names in the `channels.discord.guilds` block — only `{}` or valid guild config keys are allowed

**Check 2 — Port is already in use:**
```bash
lsof -i :18789
```
If something is already on port 18789, kill it or stop a previous gateway instance:
```bash
openclaw gateway stop
```

**Check 3 — Node.js version:**
```bash
node --version  # must be 20+
```

---

## Agents don't respond in Discord

**Symptom:** You type in a Discord channel but the bot doesn't reply.

**Check 1 — Gateway is running:**
```bash
openclaw gateway status
```

**Check 2 — Bot is in your server:**
Go to your Discord server. If the bot user is not listed as a member, re-run the OAuth2 install URL from the Discord Developer Portal.

**Check 3 — Bot has permission to read and send in the channel:**
In Discord, right-click the channel → Edit Channel → Permissions → confirm the bot role has `Send Messages` and `Read Message History`.

**Check 4 — Channel ID is correct in config:**
Right-click the Discord channel → Copy Channel ID (requires Developer Mode). Compare to the `channelId` in `~/.openclaw/openclaw.json` for that agent.

---

## `openclaw skills list` shows "Config invalid"

**Symptom:** Running any `openclaw skills` command returns `Config invalid` or a validation error.

**Most common cause:** An invalid property in `channels.discord.guilds`. The guilds block must look like:
```json
"guilds": {
  "YOUR_GUILD_ID": {}
}
```
Not:
```json
"guilds": {
  "YOUR_GUILD_ID": {
    "allowChannels": [...]
  }
}
```

Remove any unknown properties from the guilds block, then retry.

---

## Skill shows "missing requirements" in `openclaw skills check`

**Symptom:** `openclaw skills check` lists a skill as failing with missing env vars.

**Fix:** Set the required environment variables. Most skills read from a `.env` file in `~/.config/{skill-name}/.env`.

Example for `imap-smtp-email`:
```bash
mkdir -p ~/.config/imap-smtp-email
cat > ~/.config/imap-smtp-email/.env << 'EOF'
IMAP_HOST=imap.gmail.com
IMAP_PORT=993
IMAP_USER=your@gmail.com
IMAP_PASS=your-16-char-app-password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@gmail.com
SMTP_PASS=your-16-char-app-password
SMTP_FROM=your@gmail.com
EOF
```

For Gmail: you need an **App Password**, not your regular password. Enable 2FA first, then generate one at https://myaccount.google.com/apppasswords.

---

## Zalo bridge: `getCredentials is not a function`

**Symptom:** Running `node scripts/zalo-bridge.mjs login` crashes with `api.getContext().getCredentials is not a function`.

**Fix:** This was a bug in an earlier version of the bridge. The current version of `scripts/zalo-bridge.mjs` uses `ctx.cookie.serializeSync()` instead. If you have an old copy, pull the latest from this repo.

---

## Zalo bridge: QR code not found

**Symptom:** Login command runs but no QR image appears.

**Fix:** The QR is written to `~/.openclaw/zalo-session/qr.png`. Open it manually:
```bash
mkdir -p ~/.openclaw/zalo-session
node scripts/zalo-bridge.mjs login
open ~/.openclaw/zalo-session/qr.png
```

Scan the QR with your Zalo mobile app within 60 seconds.

---

## Zalo bridge: session expired

**Symptom:** Zalo commands work initially but fail after a few days with an auth error.

**Fix:** Delete the saved credentials and log in again:
```bash
rm ~/.openclaw/zalo-session/credentials.json
node scripts/zalo-bridge.mjs login
```

---

## Cron jobs not running

**Symptom:** Expected automated messages (weather, digest, etc.) don't appear in Discord.

**Check 1 — Gateway is running continuously:**
Crons only fire if the gateway process is alive. If you restarted your Mac, the gateway needs to be restarted too.

For auto-start on login:
```bash
openclaw gateway install-service   # installs a macOS LaunchAgent
```

**Check 2 — Cron is registered:**
```bash
openclaw crons list
```
Each scheduled agent should appear here with its next run time.

**Check 3 — Check cron logs:**
```bash
openclaw crons logs
```

---

## Model API errors (429, 503, auth failures)

**Symptom:** Agents return errors about the AI model API.

**Check 1 — API key is correct:**
```bash
openclaw config get models.providers
```
Confirm the `apiKey` and `baseURL` match your provider's documentation.

**Check 2 — Rate limits:**
A 429 error means you've hit your API rate limit. Either wait, or upgrade your API plan.

**Check 3 — Model name is correct:**
The `models` array in your provider config must contain exact model IDs accepted by your API endpoint.

---

## Disk space issues

**Symptom:** Gateway or agents behave erratically; disk is nearly full.

**Check:**
```bash
df -h ~
du -sh ~/.openclaw/workspace-*/
```

The `learning-log` workspace can grow large over time. You can ask the `file-organizer` agent to clean up old logs, or manually delete files older than 30 days:
```bash
find ~/.openclaw -name "*.log" -mtime +30 -delete
```
