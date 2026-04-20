# Changelog

All notable changes to this repo are documented here.

Format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

---

## [2026-04-21]

### Added
- `agents/market-intel/` — market regime monitoring agent (daily briefings, distribution day tracking, macro event awareness)
- `agents/signal-scanner/` — technical setup detection and grading (VCP, breakout, pullback, RSI, momentum, mean reversion, relative strength)
- `agents/portfolio-monitor/` — position monitoring with risk alerts (stop proximity, earnings warnings, correlation risk)
- `DISCLAIMER.md` — financial information disclaimer
- `docs/DISCORD-ALERT-TEMPLATES.md` — reference templates for Discord financial alerts (market briefing, signal, portfolio, risk escalation, watchlist)
- Markdownlint step in CI pipeline

### Changed
- `README.md` — added financial intelligence section, updated agent count to 10, added alert template and disclaimer links
- `agents/README.md` — added 3 financial agents to table and permissions matrix
- `config.example.json` — added market-intel, signal-scanner, portfolio-monitor agent entries with weekday cron schedules
- `ROADMAP.md` — added financial intelligence improvement roadmap items
- `.github/workflows/ci.yml` — added markdownlint validation step

---



### Planned
- `setup.sh` one-command installer
- Linux / Docker support docs
- Interactive skill credential setup script

---

## [2026-04-16] (continued)

### Added
- `docs/HARDENING.md` — post-setup hardening steps for Discord routing policy, sandboxing, filesystem scope, credential permissions
- `docs/DISCORD-OPERATIONS.md` — Discord runbook with health checks and operational tasks
- `docs/DISCORD-BOT-GUIDE.md` — beginner-friendly purpose and example prompt for every Discord channel
- `scripts/discord-sync.py` — canonical Discord layout audit/apply utility
- `scripts/harden-openclaw.sh` — one-command hardening baseline helper
- `scripts/discord-post-onboarding.py` — posts starter "how to use" messages into every Discord bot channel

### Changed
- `README.md` — simplified structure, removed duplication, added Discord sync commands and hardening doc link
- `docs/ARCHITECTURE.md` — updated Zalo bridge wording from OA to personal account bridge
- `docs/HARDENING.md` — added Discord slash-command allowlist guidance and script usage
- `scripts/discord-sync.py` — now also enforces beginner-friendly channel topics/descriptions

---

## [2026-04-16]

### Added
- `SECURITY.md` — credential handling guidance, least-privilege Discord setup, checklist
- `CONTRIBUTING.md` — agent file conventions, code style, what to include in PRs
- `ROADMAP.md` — near-term, medium-term, and stretch goals
- `CHANGELOG.md` — this file
- `config.example.json` — safe config template with placeholder values
- `docs/TROUBLESHOOTING.md` — common errors and fixes for gateway, agents, skills, Zalo

### Changed
- `README.md` — rewrote hero section, added Current Status table, "Who this is for" section, removed false `setup.sh` reference, improved quickstart with honest caveats, added security and contributing links
- `agents/README.md` — updated with copy instructions and file format reference
- `.gitignore` — added more credential and session file patterns

---

## [2026-04-14]

### Added
- Zalo personal account bridge (`scripts/zalo-bridge.mjs`) using `zca-js`
- `agents/zalo-events/` — SOUL.md and IDENTITY.md for Zalo event follow-up agent
- 11 ClawHub skills installed: powerpoint-pptx, imap-smtp-email, multi-search-engine, self-improving, ontology, skill-finder-cn, notion, notion-api-skill, notion-skill, file-manager

### Fixed
- Zalo bridge `loginQR()` crash — fixed by passing `qrPath` param and using `ctx.cookie.serializeSync()` instead of nonexistent `getCredentials()`
- Discord config validation error — removed invalid `allowChannels` key from guilds config

---

## [2026-04-12]

### Added
- GitHub public repo: https://github.com/cheafi/openclaw-fleet
- `docs/ARCHITECTURE.md`, `docs/BEGINNERS-GUIDE.md`, `docs/USE-CASES.md`
- `docs/ORCHESTRATOR.md`, `docs/PROTOCOLS.md`
- `scripts/fleet-runner.sh` — workflow chain executor
- Discord server reorganized into 6 clean categories
- 31-channel Discord layout with 7 custom agent configs and 9 automated cron schedules
- Mac weekly disk cleanup via `file-organizer` cron (Saturday 10 AM HKT)
