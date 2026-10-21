# Security Architecture (Enhanced v0.20)

Research control plane. Not a certified product. Not legal advice.

## Zero-trust principles

- Every signal re-validated against regime, volume, anomaly score, and source attestation.
- No role can enable live trading or load trade/withdrawal keys.
- Secrets refused at parse time; expanded redaction patterns.

## Data classification (extended)

| Field | Level | Handling |
|---|---|---|
| OHLCV, funding | Public market | Synthetic only in this repo |
| Source label + digest | Integrity | Attested; Merkle chain for lineage |
| Anomaly score | Integrity | Isolation proxy; high score forces flat |
| Wallet / seed / private key | Secret | Refused + redacted |
| Personal identifiers | Personal | PDPA tripwire |

## Controls

- Hash-chained audit log with sequence integrity.
- Feed anomaly: jump, staleness, directional inconsistency, extreme oscillator.
- Kill switch, drawdown halt, class caps, confidence floors.
- Paper-only mode guard.

## Incident response

1. Engage kill switch.
2. Freeze audit + attestation.
3. Rotate any pasted secret outside the repo.
4. Human review required to clear.
