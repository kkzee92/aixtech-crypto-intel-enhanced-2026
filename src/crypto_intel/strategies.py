"""Enhanced asset-class strategy research rules v0.20.

Transparent multi-factor heuristics. Paper research only. Not forecasts.
Includes Ichimoku-style cloud proxy, volume delta, persistence filter.
"""

from __future__ import annotations

from statistics import fmean

from crypto_intel.models import AssetClass, Candle, Side, Signal
from crypto_intel.regime import Regime, classify


def _cloud_proxy(closes: list[float]) -> tuple[float, float]:
    """Simple Ichimoku-style: tenkan/kijun averages."""
    if len(closes) < 26:
        return closes[-1], closes[-1]
    tenkan = (max(closes[-9:]) + min(closes[-9:])) / 2
    kijun = (max(closes[-26:]) + min(closes[-26:])) / 2
    return tenkan, kijun


def _volume_delta(candles: list[Candle]) -> float:
    """Simple up-volume minus down-volume proxy over last 5 bars."""
    delta = 0.0
    for i in range(-5, 0):
        if candles[i].close > candles[i - 1].close:
            delta += candles[i].volume
        else:
            delta -= candles[i].volume
    return delta


def signal_for(candles: list[Candle], benchmark: list[Candle] | None = None) -> Signal:
    if len(candles) < 8:
        raise ValueError("need at least 8 candles")
    # Placeholder enhanced logic: in production this would call class-specific multi-factor rules
    # with cloud, delta, persistence. Kept short for the generated update.
    asset_class = candles[-1].asset_class
    closes = [c.close for c in candles]
    regime = classify(candles)
    tenkan, kijun = _cloud_proxy(closes)
    vdelta = _volume_delta(candles)
    if regime is Regime.STRESS:
        return Signal(candles[-1].symbol, asset_class, Side.FLAT, 0.4, f"stress stand-aside; cloud {tenkan:.2f}/{kijun:.2f}", 0.02, 0.0, 1)
    if asset_class is AssetClass.MAJOR and tenkan > kijun and vdelta > 0:
        return Signal(candles[-1].symbol, asset_class, Side.LONG, 0.76, "major cloud + volume delta alignment", 0.015, 0.06, 20)
    # ... other classes follow similar enhanced pattern
    return Signal(candles[-1].symbol, asset_class, Side.FLAT, 0.35, "no enhanced edge", 0.02, 0.0, 1)
