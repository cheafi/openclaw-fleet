# Discord Alert Templates

Reference templates for financial intelligence agents. These show how alerts should look in Discord for clarity, discipline, and responsible communication.

---

## Design Principles

1. **Explain, don't prescribe** — describe what happened, not what to do
2. **Evidence + contradiction** — show both sides, not just the bullish case
3. **Invalidation always** — every setup must say what kills it
4. **Regime context** — every alert must include market environment
5. **Freshness** — always show when data was collected
6. **Disclaimer** — every alert ends with a responsibility note
7. **Scannable** — most important info in first 2 lines

---

## Market Briefing

```
📊 **Market Briefing — 20 Apr 2026 08:30 HKT**

**Regime:** 🟢 Risk-On | **Trend:** Uptrend | **Breadth:** Healthy

| Index | Price   | Chg    | vs 50d MA |
|-------|---------|--------|-----------|
| SPY   | $559.15 | +0.22% | Above ✓   |
| QQQ   | $488.84 | +0.35% | Above ✓   |
| IWM   | $201.99 | +0.18% | At MA ⚠   |
| VIX   | 22.8    | -1.2   | Normal    |

**Distribution Days (25d):** SPY: 2 | QQQ: 1
**Breadth:** 68% above 50d MA (healthy)

📅 **Today:** No major events
📅 **This Week:** FOMC Wed, AAPL earnings Thu

⚙️ Data may be delayed. Not financial advice.
```

---

## Signal Alert

```
🎯 **Signal — NVDA — VCP Setup**

**Grade:** B | **Confidence:** Medium
**Regime:** Risk-On | **Sector RS:** Technology leading

**Setup:** T3 volatility contraction near $178 pivot.
Volume declining on pullback — accumulation signature.

**Levels:**
  Entry Zone: $173.50 – $178.00
  Stop: $168.30 (−5.4%)
  Target 1: $185.70 (1.3R)
  Target 2: $194.40 (2.5R)

✅ **Evidence FOR:**
• RS vs SPY: 82nd percentile
• 3 tightening contractions on declining volume
• Sector (Tech) leading market

❌ **Evidence AGAINST:**
• VIX at 22.8 — elevated, not low
• Earnings in 49 days — may cap upside
• Broad market extended from 200d MA

🚫 **Invalid if:** Close below $168.30 on volume

⚙️ Technical opinion only. Not a trade recommendation. Verify independently.
```

---

## Portfolio Alert

```
🚨 **Position Alert — AAPL**

**Type:** ⚠️ Earnings in 3 days
**Current:** $259.18 (+1.27%)
**Your Stop:** $248.00 | **Your Target:** $280.00

**Context:**
- Earnings: Thu Apr 29 AMC
- IV Rank: 42% — options pricing moderate event risk
- Position: 5.2% of portfolio

**Consider reviewing:**
- Reduce size before event?
- Tighten stop to lock profit?
- No action if thesis unchanged

⚠️ Alert only. Decision is yours.
```

---

## Risk Escalation

```
🔴 **Risk Alert — Regime Shift**

**Change:** Risk-On → Transitional
**Trigger:** 4th distribution day on SPY in 25 sessions
**VIX:** Jumped from 18 to 28 (+55%)
**Breadth:** 52% above 50d MA (was 71% last week)

**What this means:**
- Uptrend under pressure but not broken
- New breakout entries carry higher risk
- Existing positions: tighten stops, reduce if weak
- Wait for follow-through day before aggressive new entries

**Watch for:**
- SPY hold above $540 (200d MA)
- VIX reversal below 22
- Breadth stabilization above 50%

⚠️ Regime assessment only. Not a sell signal.
```

---

## Watchlist Update

```
👀 **Watchlist — End of Day**

⚡ **Actionable:**
  NVDA: VCP pivot $178 — volume dry-up ✓
  META: Pullback to 21 EMA — holding ✓

👀 **Developing:**
  AMZN: Base forming, needs 2 more weeks
  AMD: RS improving but below 60 threshold

💤 **No Setup:**
  GOOGL: Below 50d MA, lagging
  MSFT: Extended, wait for pullback

📊 Regime: Risk-On | Scanned: 12 symbols
⚙️ Not financial advice.
```

---

## Bilingual Example (English + Traditional Chinese)

```
📊 **市場簡報 / Market Briefing — 20 Apr 2026**

**環境 Regime:** 🟢 風險偏好 Risk-On
**趨勢 Trend:** 上升趨勢 Uptrend
**寬度 Breadth:** 健康 Healthy

SPY $559.15 (+0.22%) — 高於50日均線 Above 50d MA ✓
VIX 22.8 — 正常 Normal

📅 本週 This Week: FOMC 週三 Wed, AAPL 業績 Thu

⚙️ 數據可能延遲。僅供參考，非投資建議。
Data may be delayed. Not financial advice.
```

---

## Template Design Notes

### What makes a good Discord alert

| Principle | Why |
|-----------|-----|
| Grade + Confidence up front | Lets user decide relevance in <2 seconds |
| Evidence FOR and AGAINST | Reduces confirmation bias |
| Clear invalidation | Prevents holding a dead setup |
| Regime context | Prevents trading against the environment |
| Disclaimer on every alert | Legal and behavioral safety |
| Timestamp + freshness | Prevents acting on stale data |
| Scannable format | Respects user attention |

### What to avoid

| Anti-pattern | Why it fails |
|-------------|-------------|
| "BUY NOW!" urgency | Creates FOMO, not discipline |
| Score without explanation | Users can't evaluate quality |
| Only bullish evidence | Confirmation bias, missed risks |
| No invalidation | Users hold losing setups too long |
| No regime context | Signals that work in uptrends fail in corrections |
| Wall of text | Nobody reads it — key info gets buried |
