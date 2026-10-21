# AIxTech Crypto Intel Enhanced 2026

**Paper-only** automated cryptocurrency trading **information system** with cyber and data security architecture.

Research harness only. Does **not** place live orders, does not store exchange secrets, and is **not financial advice**.

Reference: builds on [kkzee92/aixtech-crypto-intel](https://github.com/kkzee92/aixtech-crypto-intel) and the public reference under [zeekiankok92/aixtech-crypto-intel](https://github.com/zeekiankok92/aixtech-crypto-intel).

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![version](https://img.shields.io/badge/version-0.20.0-blue)
![mode](https://img.shields.io/badge/execution-paper%20only-orange)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## Enhancements in v0.20

- **Strategies**: Per-asset-class multi-factor rules with Ichimoku-style cloud proxies, volume delta confirmation, Hurst-like persistence for regime, adaptive ATR stops, multi-timeframe alignment.
- **Risk**: Volatility-scaled sizing, correlation regime overlay, dynamic confidence floors, portfolio-level drawdown gates.
- **Security**: Zero-trust re-validation, expanded secret redaction (incl. seeds, PEM, base58), Merkle-style data lineage, anomaly scoring with isolation forest proxy, data residency notes.
- Still strictly **paper-only**. Live execution is refused by design.

## Asset-class research rules (summary)

| Class | Key enhancements |
|---|---|
| Major | EMA + MACD + RSI + cloud + volume delta + persistence |
| Large-cap alt | Volume-confirmed breakout + strength + delta |
| Stablecoin | Adaptive depeg bands with sustained checks |
| DeFi | Calm-regime trend + vol filter + multi-factor |
| Meme | Burst + extension filter + volume accel |
| L2 | Relative strength + correlation + ATR contained |
| RWA | Slow trend + gap halt + persistence |
| Perpetual | Funding carry + drift containment + stability |

See `docs/asset-class-strategies.md` and `docs/security-architecture.md` for full details.

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python scripts/make_fixtures.py
PYTHONPATH=src python -m crypto_intel scan fixtures/candles_synthetic.json
```

## Honesty

- Synthetic fixtures only for research.
- No live connectors.
- Scores describe historical synthetic data, not future returns.
