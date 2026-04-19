#!/usr/bin/env bash
# fleet-runner.sh - Inter-agent workflow executor
# Usage: fleet-runner.sh <workflow-name> [args]
#
# Channel IDs are read from environment variables.
# Set them in your .env or export before running:
#   export CHANNEL_HEALTHCHECK="1494231467608375336"
#   export CHANNEL_LEARNING_LOG="1494231478790389801"
#   etc.
set -euo pipefail

# Resolve channel IDs from env vars, with empty defaults
CH_HEALTHCHECK="${CHANNEL_HEALTHCHECK:-}"
CH_LEARNING_LOG="${CHANNEL_LEARNING_LOG:-}"
CH_SELF_IMPROVING="${CHANNEL_SELF_IMPROVING:-}"
CH_SELF_EVOLVING="${CHANNEL_SELF_EVOLVING:-}"
CH_FAIL2BAN="${CHANNEL_FAIL2BAN:-}"
CH_AGENT_BROWSER="${CHANNEL_AGENT_BROWSER:-}"
CH_SUMMARIZE="${CHANNEL_SUMMARIZE:-}"
CH_HUMANIZER="${CHANNEL_HUMANIZER:-}"
CH_GITHUB="${CHANNEL_GITHUB:-}"
CH_AUTO_DEPLOY="${CHANNEL_AUTO_DEPLOY:-}"
CH_CONSTRUCTION_NEWS="${CHANNEL_CONSTRUCTION_NEWS:-}"

chain() {
  local agent="$1" msg="$2" channel="$3"

  if [[ -z "$channel" ]]; then
    echo "  ⚠ Skipping $agent — channel ID not set (export CHANNEL_* env vars)"
    return 0
  fi

  echo "  -> Running $agent..."
  openclaw agent --agent "$agent" --message "$msg" \
    --deliver --channel discord --reply-to "$channel" \
    --timeout-seconds 300 2>&1 | tail -5
  echo "  Done: $agent"
}

case "${1:-help}" in
  self-improvement-loop)
    echo "Self-Improvement Loop"
    chain healthcheck "Quick health check for fleet review" "$CH_HEALTHCHECK"
    chain learning-log "Generate weekly digest of all errors, corrections, and successes" "$CH_LEARNING_LOG"
    chain self-improving "Read learning-log digest, score all agents, propose top 5 improvements" "$CH_SELF_IMPROVING"
    chain self-evolving-skill "Scan all agent SOUL.md files for outdated patterns and patch" "$CH_SELF_EVOLVING"
    ;;
  security-chain)
    echo "Security Chain"
    chain healthcheck "Check all ports, processes, services" "$CH_HEALTHCHECK"
    chain fail2ban-reporter "Full security audit" "$CH_FAIL2BAN"
    ;;
  content-pipeline)
    query="${2:-latest AI news}"
    echo "Content Pipeline: $query"
    chain agent-browser "Search and fetch: $query" "$CH_AGENT_BROWSER"
    chain summarize "Summarize the latest findings about: $query" "$CH_SUMMARIZE"
    chain humanizer "Rewrite this summary conversationally" "$CH_HUMANIZER"
    ;;
  deploy-pipeline)
    echo "Deploy Pipeline"
    chain github "Check latest commits and PR status" "$CH_GITHUB"
    chain auto-deploy "Run deployment pipeline" "$CH_AUTO_DEPLOY"
    chain healthcheck "Post-deploy health check" "$CH_HEALTHCHECK"
    ;;
  morning-briefing)
    echo "Morning Briefing"
    chain healthcheck "Quick system status" "$CH_HEALTHCHECK"
    chain construction-news "APAC construction opportunities" "$CH_CONSTRUCTION_NEWS"
    chain learning-log "Yesterday fleet activity summary" "$CH_LEARNING_LOG"
    ;;
  *)
    echo "Fleet Workflow Runner"
    echo "Usage: $0 <workflow>"
    echo ""
    echo "Workflows:"
    echo "  self-improvement-loop  Weekly fleet review + auto-patching"
    echo "  security-chain         Security scan + audit"
    echo "  content-pipeline <q>   Search -> summarize -> humanize"
    echo "  deploy-pipeline        GitHub -> deploy -> healthcheck"
    echo "  morning-briefing       Health + news + digest"
    echo ""
    echo "Set CHANNEL_* env vars before running. See .env.example."
    ;;
esac
