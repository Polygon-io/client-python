from dataclasses import dataclass
from typing import List, Optional

from .aggs import Agg


@dataclass
class IndicatorValue:
    "Contains one datum for indicators with a single value."
    timestamp: Optional[int] = None
    value: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return IndicatorValue(
            timestamp=d.get("timestamp", None),
            value=d.get("value", None),
        )


@dataclass
class MACDIndicatorValue:
    "Contains one datum for all MACD values."
    timestamp: Optional[int] = None
    value: Optional[float] = None
    signal: Optional[float] = None
    histogram: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return MACDIndicatorValue(
            timestamp=d.get("timestamp", None),
            value=d.get("value", None),
            signal=d.get("signal", None),
            histogram=d.get("histogram", None),
        )


@dataclass
class IndicatorUnderlying:
    "Contains the URL to call to get the aggs used for building the indicator."
    url: Optional[str] = None
    aggregates: Optional[List[Agg]] = None

    @staticmethod
    def from_dict(d):
        return IndicatorUnderlying(
            url=d.get("url", None),
            aggregates=[Agg.from_dict(a) for a in d.get("aggregates", [])],
        )


@dataclass
class SingleIndicatorResults:
    "Contains indicator values and Underlying."
    values: Optional[List[IndicatorValue]] = None
    underlying: Optional[IndicatorUnderlying] = None

    @staticmethod
    def from_dict(d):
        return SingleIndicatorResults(
            values=[IndicatorValue.from_dict(v) for v in (d.get("values", []))],
            underlying=IndicatorUnderlying.from_dict(d.get("underlying", None)),
        )


SMAIndicatorResults = SingleIndicatorResults
EMAIndicatorResults = SingleIndicatorResults
RSIIndicatorResults = SingleIndicatorResults


@dataclass
class MACDIndicatorResults:
    "Contains indicator values and Underlying."
    values: Optional[List[MACDIndicatorValue]] = None
    underlying: Optional[IndicatorUnderlying] = None

    @staticmethod
    def from_dict(d):
        return MACDIndicatorResults(
            values=[MACDIndicatorValue.from_dict(v) for v in (d.get("values", []))],
            underlying=IndicatorUnderlying.from_dict(d.get("underlying", None)),
        )
