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

## 3) Restrict tool blast radius

Prefer tighter defaults for exposed agents:

```bash
openclaw config set agents.defaults.sandbox.mode "all"
openclaw config set tools.fs.workspaceOnly true
```

Why: reduces filesystem and runtime impact if a prompt is malicious.

---

## 4) Tighten credentials directory permissions

```bash
chmod 700 ~/.openclaw/credentials
```

Why: avoids local credential files being readable by other users on the machine.

---

## 5) Re-check status

```bash
openclaw status
openclaw security audit
```

---

## 6) Operational cadence

- Run `openclaw security audit` weekly
- Rotate Discord token and API keys on suspected exposure
- Keep gateway loopback-only (`127.0.0.1`) unless you have proxy auth + TLS

---

## Notes

- This project intentionally favors local-first operation and transparent docs.
- For high-trust personal use, you may keep broader settings. For shared environments, apply all hardening steps above.