#!/usr/bin/env bash
# fleet-runner.sh - Inter-agent workflow executor
# Usage: fleet-runner.sh <workflow-name> [args]
set -euo pipefail

chain() {
  local agent="$1" msg="$2" channel="$3"
  echo "  -> Running $agent..."
  openclaw agent --agent "$agent" --message "$msg" --deliver --channel discord --reply-to "$channel" --timeout-seconds 300 2>&1 | tail -5
  echo "  Done: $agent"
}

case "${1:-help}" in
  self-improvement-loop)
    echo "Self-Improvement Loop"
    chain healthcheck "Quick health check for fleet review" "1494231467608375336"
    chain learning-log "Generate weekly digest of all errors, corrections, and successes" "1494231478790389801"
    chain self-improving "Read learning-log digest, score all 30 agents, propose top 5 improvements" "1494225966883405854"
    chain self-evolving-skill "Scan all agent SOUL.md files for outdated patterns and patch" "1494231476089389180"
    ;;
  security-chain)
    echo "Security Chain"
    chain healthcheck "Check all ports, processes, services" "1494231467608375336"
    chain fail2ban-reporter "Full security audit" "1494231469269188668"
    ;;
  content-pipeline)
    query="${2:-latest AI news}"
    echo "Content Pipeline: $query"
    chain agent-browser "Search and fetch: $query" "1494225970448564255"
    chain summarize "Summarize the latest findings about: $query" "1494225972717817927"
    chain humanizer "Rewrite this summary conversationally" "1494225968535961650"
    ;;
  deploy-pipeline)
    echo "Deploy Pipeline"
    chain github "Check latest commits and PR status" "1494225997594361880"
    chain auto-deploy "Run deployment pipeline" "1494231491918561431"
    chain healthcheck "Post-deploy health check" "1494231467608375336"
    ;;
  morning-briefing)
    echo "Morning Briefing"
    chain healthcheck "Quick system status" "1494231467608375336"
    chain construction-news "APAC construction opportunities" "1493890359057580093"
    chain learning-log "Yesterday fleet activity summary" "1494231478790389801"
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
    ;;
esac
