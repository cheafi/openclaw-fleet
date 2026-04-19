.PHONY: validate lint sync sync-apply harden

validate:
	@bash scripts/validate.sh

lint:
	@echo "Checking shell scripts..."
	@shellcheck scripts/*.sh 2>/dev/null || echo "shellcheck not installed — brew install shellcheck"
	@echo "Checking markdown..."
	@npx markdownlint-cli2 '**/*.md' 2>/dev/null || echo "markdownlint not installed — npm install -g markdownlint-cli2"

sync:
	@python3 scripts/discord-sync.py

sync-apply:
	@python3 scripts/discord-sync.py --apply

harden:
	@bash scripts/harden-openclaw.sh
