from dataclasses import dataclass
from typing import Dict, List, Optional

from .aggs import Agg
from .quotes import LastQuote
from .trades import LastTrade


@dataclass
class MinuteSnapshot:
    "Most recent minute bar."
    accumulated_volume: Optional[float] = None
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None
    otc: Optional[bool] = None
    timestamp: Optional[int] = None
    transactions: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return MinuteSnapshot(
            d.get("av", None),
            d.get("o", None),
            d.get("h", None),
            d.get("l", None),
            d.get("c", None),
            d.get("v", None),
            d.get("vw", None),
            d.get("otc", None),
            d.get("t", None),
            d.get("n", None),
        )


@dataclass
class IndicesSession:
    "Contains data for the most recent daily bar in an options contract."
    change: Optional[float] = None
    change_percent: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return IndicesSession(**d)


@dataclass
class IndicesSnapshot:
    value: Optional[float] = None
    name: Optional[str] = None
    type: Optional[str] = None
    ticker: Optional[str] = None
    market_status: Optional[str] = None
    session: Optional[IndicesSession] = None
    error: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return IndicesSnapshot(
            value=d.get("value", None),
            name=d.get("name", None),
            type=d.get("type", None),
            ticker=d.get("ticker", None),
            market_status=d.get("market_status", None),
            session=(
                None if "session" not in d else IndicesSession.from_dict(d["session"])
            ),
            error=d.get("error", None),
            message=d.get("message", None),
        )


@dataclass
class TickerSnapshot:
    "Contains the most up-to-date market data for all traded ticker symbols."
    day: Optional[Agg] = None
    last_quote: Optional[LastQuote] = None
    last_trade: Optional[LastTrade] = None
    min: Optional[MinuteSnapshot] = None
    prev_day: Optional[Agg] = None
    ticker: Optional[str] = None
    todays_change: Optional[float] = None
    todays_change_percent: Optional[float] = None
    updated: Optional[int] = None
    fair_market_value: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return TickerSnapshot(
            day=None if "day" not in d else Agg.from_dict(d["day"]),
            last_quote=(
                None if "lastQuote" not in d else LastQuote.from_dict(d["lastQuote"])
            ),
            last_trade=(
                None if "lastTrade" not in d else LastTrade.from_dict(d["lastTrade"])
            ),
            min=None if "min" not in d else MinuteSnapshot.from_dict(d["min"]),
            prev_day=None if "prevDay" not in d else Agg.from_dict(d["prevDay"]),
            ticker=d.get("ticker", None),
            todays_change=d.get("todaysChange", None),
            todays_change_percent=d.get("todaysChangePerc", None),
            updated=d.get("updated", None),
            fair_market_value=d.get("fmv", None),
        )


@dataclass
class DayOptionContractSnapshot:
    "Contains data for the most recent daily bar in an options contract."
    change: Optional[float] = None
    change_percent: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    last_updated: Optional[int] = None
    low: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return DayOptionContractSnapshot(**d)


@dataclass
class OptionDetails:
    "Contains details for an options contract."
    contract_type: Optional[str] = None
    exercise_style: Optional[str] = None
    expiration_date: Optional[str] = None
    shares_per_contract: Optional[float] = None
    strike_price: Optional[float] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OptionDetails(**d)


@dataclass
class LastQuoteOptionContractSnapshot:
    "Contains data for the most recent quote in an options contract."
    ask: Optional[float] = None
    ask_size: Optional[float] = None
    bid: Optional[float] = None
    bid_size: Optional[float] = None
    last_updated: Optional[int] = None
    midpoint: Optional[float] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return LastQuoteOptionContractSnapshot(**d)


@dataclass
class LastTradeOptionContractSnapshot:
    "Contains data for the most recent trade for an options contract."
    price: Optional[float] = None
    sip_timestamp: Optional[int] = None
    size: Optional[int] = None
    conditions: Optional[List[int]] = None
    exchange: Optional[int] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return LastTradeOptionContractSnapshot(**d)


@dataclass
class Greeks:
    "Contains data for the greeks in an options contract."
    delta: Optional[float] = None
    gamma: Optional[float] = None
    theta: Optional[float] = None
    vega: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return Greeks(**d)


@dataclass
class UnderlyingAsset:
    "Contains data for the underlying stock in an options contract."
    change_to_break_even: Optional[float] = None
    last_updated: Optional[int] = None
    price: Optional[float] = None
    value: Optional[float] = None
    ticker: Optional[str] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return UnderlyingAsset(**d)


@dataclass
class OptionContractSnapshot:
    "Contains data for the snapshot of an option contract of a stock equity."
    break_even_price: Optional[float] = None
    day: Optional[DayOptionContractSnapshot] = None
    details: Optional[OptionDetails] = None
    greeks: Optional[Greeks] = None
    implied_volatility: Optional[float] = None
    last_quote: Optional[LastQuoteOptionContractSnapshot] = None
    last_trade: Optional[LastTradeOptionContractSnapshot] = None
    open_interest: Optional[float] = None
    underlying_asset: Optional[UnderlyingAsset] = None
    fair_market_value: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return OptionContractSnapshot(
            break_even_price=d.get("break_even_price", None),
            day=(
                None
                if "day" not in d
                else DayOptionContractSnapshot.from_dict(d["day"])
            ),
            details=(
                None if "details" not in d else OptionDetails.from_dict(d["details"])
            ),
            greeks=None if "greeks" not in d else Greeks.from_dict(d["greeks"]),
            implied_volatility=d.get("implied_volatility", None),
            last_quote=(
                None
                if "last_quote" not in d
                else LastQuoteOptionContractSnapshot.from_dict(d["last_quote"])
            ),
            last_trade=(
                None
                if "last_trade" not in d
                else LastTradeOptionContractSnapshot.from_dict(d["last_trade"])
            ),
            open_interest=d.get("open_interest", None),
            underlying_asset=(
                None
                if "underlying_asset" not in d
                else UnderlyingAsset.from_dict(d["underlying_asset"])
            ),
            fair_market_value=d.get("fmv", None),
        )


@dataclass
class OrderBookQuote:
    "Contains data for a book bid or ask."
    price: Optional[float] = None
    exchange_shares: Optional[Dict[str, float]] = None

    @staticmethod
    def from_dict(d):
        return OrderBookQuote(
            d.get("p", None),
            d.get("x", None),
        )


@dataclass
class SnapshotTickerFullBook:
    "Contains the current level 2 book of a single ticker. This is the combined book from all of the exchanges."
    ticker: Optional[str] = None
    bids: Optional[List[OrderBookQuote]] = None
    asks: Optional[List[OrderBookQuote]] = None
    bid_count: Optional[float] = None
    ask_count: Optional[float] = None
    spread: Optional[float] = None
    updated: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return SnapshotTickerFullBook(
            ticker=d.get("ticker", None),
            bids=(
                None
                if "bids" not in d
                else [OrderBookQuote.from_dict(o) for o in d["bids"]]
            ),
            asks=(
                None
                if "asks" not in d
                else [OrderBookQuote.from_dict(o) for o in d["asks"]]
            ),
            bid_count=d.get("bidCount", None),
            ask_count=d.get("askCount", None),
            spread=d.get("spread", None),
            updated=d.get("updated", None),
        )


@dataclass
class UniversalSnapshotSession:
    """Contains data about the most recent trading session for an asset."""

    price: Optional[float] = None
    change: Optional[float] = None
    change_percent: Optional[float] = None
    early_trading_change: Optional[float] = None
    early_trading_change_percent: Optional[float] = None
    late_trading_change: Optional[float] = None
    late_trading_change_percent: Optional[float] = None
    open: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    previous_close: Optional[float] = None
    volume: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return UniversalSnapshotSession(**d)


@dataclass
class UniversalSnapshotLastQuote:
    """Contains the most recent quote for an asset."""

    ask: Optional[float] = None
    ask_size: Optional[float] = None
    bid: Optional[float] = None
    bid_size: Optional[float] = None
    midpoint: Optional[float] = None
    exchange: Optional[int] = None
    timeframe: Optional[str] = None
    last_updated: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return UniversalSnapshotLastQuote(**d)


@dataclass
class UniversalSnapshotLastTrade:
    """Contains the most recent trade for an asset."""

    id: Optional[int] = None
    price: Optional[float] = None
    size: Optional[int] = None
    exchange: Optional[int] = None
    conditions: Optional[List[int]] = None
    timeframe: Optional[str] = None
    last_updated: Optional[int] = None
    participant_timestamp: Optional[int] = None
    sip_timestamp: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return UniversalSnapshotLastTrade(**d)


@dataclass
class UniversalSnapshotUnderlyingAsset:
    """Contains data for the underlying stock in an options contract."""

    ticker: Optional[str] = None
    price: Optional[float] = None
    value: Optional[float] = None
    change_to_break_even: Optional[float] = None
    timeframe: Optional[str] = None
    last_updated: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return UniversalSnapshotUnderlyingAsset(**d)


@dataclass
class UniversalSnapshotDetails:
    """Contains details for an options contract."""

    contract_type: Optional[str] = None
    exercise_style: Optional[str] = None
    expiration_date: Optional[str] = None
    shares_per_contract: Optional[float] = None
    strike_price: Optional[float] = None
    underlying_ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return UniversalSnapshotDetails(**d)


@dataclass
class UniversalSnapshot:
    """Contains snapshot data for an asset."""

    ticker: Optional[str] = None
    type: Optional[str] = None
    session: Optional[UniversalSnapshotSession] = None
    last_quote: Optional[UniversalSnapshotLastQuote] = None
    last_trade: Optional[UniversalSnapshotLastTrade] = None
    greeks: Optional[Greeks] = None
    underlying_asset: Optional[UniversalSnapshotUnderlyingAsset] = None
    details: Optional[UniversalSnapshotDetails] = None
    break_even_price: Optional[float] = None
    implied_volatility: Optional[float] = None
    open_interest: Optional[float] = None
    market_status: Optional[str] = None
    name: Optional[str] = None
    fair_market_value: Optional[float] = None
    error: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return UniversalSnapshot(
            ticker=d.get("ticker", None),
            type=d.get("type", None),
            session=(
                None
                if "session" not in d
                else UniversalSnapshotSession.from_dict(d["session"])
            ),
            last_quote=(
                None
                if "last_quote" not in d
                else UniversalSnapshotLastQuote.from_dict(d["last_quote"])
            ),
            last_trade=(
                None
                if "last_trade" not in d
                else UniversalSnapshotLastTrade.from_dict(d["last_trade"])
            ),
            greeks=None if "greeks" not in d else Greeks.from_dict(d["greeks"]),
            underlying_asset=(
                None
                if "underlying_asset" not in d
                else UniversalSnapshotUnderlyingAsset.from_dict(d["underlying_asset"])
            ),
            details=(
                None
                if "details" not in d
                else UniversalSnapshotDetails.from_dict(d["details"])
            ),
            break_even_price=d.get("break_even_price", None),
            implied_volatility=d.get("implied_volatility", None),
            open_interest=d.get("open_interest", None),
            market_status=d.get("market_status", None),
            name=d.get("name", None),
            fair_market_value=d.get("fmv", None),
            error=d.get("error", None),
            message=d.get("message", None),
        )
