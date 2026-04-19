#!/usr/bin/env bash
# Validate that all agent directories have required files
set -euo pipefail

AGENTS_DIR="$(cd "$(dirname "$0")/../agents" && pwd)"
errors=0

echo "Validating agent configs..."
for agent_dir in "$AGENTS_DIR"/*/; do
  agent="$(basename "$agent_dir")"
  [[ "$agent" == "__pycache__" ]] && continue

  if [[ ! -f "$agent_dir/SOUL.md" ]]; then
    echo "  ✗ agents/$agent/SOUL.md missing"
    errors=$((errors + 1))
  fi

  if [[ ! -f "$agent_dir/IDENTITY.md" ]]; then
    echo "  ✗ agents/$agent/IDENTITY.md missing"
    errors=$((errors + 1))
  fi

  if [[ -f "$agent_dir/SOUL.md" && -f "$agent_dir/IDENTITY.md" ]]; then
    echo "  ✓ agents/$agent"
  fi
done

echo ""
if [[ $errors -gt 0 ]]; then
  echo "FAILED: $errors missing files"
  exit 1
else
  echo "All agents valid."
fi
