#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/harden-openclaw.sh
#   DISCORD_GUILD_ID=... DISCORD_USER_ID=... ./scripts/harden-openclaw.sh
#
# Optional env vars:
#   DISCORD_GUILD_ID   Discord guild/server ID for per-guild slash-command allowlist
#   DISCORD_USER_ID    Discord user ID to allow for slash commands

echo "Applying OpenClaw hardening baseline..."

openclaw config set channels.discord.groupPolicy "allowlist"
openclaw config set agents.defaults.sandbox.mode "all"
openclaw config set tools.fs.workspaceOnly true

if [[ -n "${DISCORD_USER_ID:-}" ]]; then
  openclaw config set channels.discord.allowFrom "[\"${DISCORD_USER_ID}\"]"

  if [[ -n "${DISCORD_GUILD_ID:-}" ]]; then
    openclaw config set "channels.discord.guilds.${DISCORD_GUILD_ID}.users" "[\"${DISCORD_USER_ID}\"]"
  fi
fi

if [[ -d "$HOME/.openclaw/credentials" ]]; then
  chmod 700 "$HOME/.openclaw/credentials"
fi

echo "Restarting gateway..."
openclaw gateway restart

echo "Running security audit..."
openclaw security audit

echo "Done."
