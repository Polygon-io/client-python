from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CompanyAddress:
    "Contains address data for a ticker detail."
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return CompanyAddress(**d)


@dataclass
class Branding:
    "Contains branding data for a ticker detail."
    icon_url: Optional[str] = None
    logo_url: Optional[str] = None
    accent_color: Optional[str] = None
    light_color: Optional[str] = None
    dark_color: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Branding(**d)


@dataclass
class Publisher:
    "Contains publisher data for ticker news."
    favicon_url: Optional[str] = None
    homepage_url: Optional[str] = None
    logo_url: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Publisher(**d)


@dataclass
class Ticker:
    "Ticker contains data for a specified ticker symbol."
    active: Optional[bool] = None
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    currency_name: Optional[str] = None
    currency_symbol: Optional[str] = None
    base_currency_symbol: Optional[str] = None
    base_currency_name: Optional[str] = None
    delisted_utc: Optional[str] = None
    last_updated_utc: Optional[str] = None
    locale: Optional[str] = None
    market: Optional[str] = None
    name: Optional[str] = None
    primary_exchange: Optional[str] = None
    share_class_figi: Optional[str] = None
    ticker: Optional[str] = None
    type: Optional[str] = None
    source_feed: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Ticker(**d)


@dataclass
class TickerDetails:
    "TickerDetails contains data for a specified ticker symbol."
    active: Optional[bool] = None
    address: Optional[CompanyAddress] = None
    branding: Optional[Branding] = None
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    currency_name: Optional[str] = None
    currency_symbol: Optional[str] = None
    base_currency_name: Optional[str] = None
    base_currency_symbol: Optional[str] = None
    delisted_utc: Optional[str] = None
    description: Optional[str] = None
    ticker_root: Optional[str] = None
    ticker_suffix: Optional[str] = None
    homepage_url: Optional[str] = None
    list_date: Optional[str] = None
    locale: Optional[str] = None
    market: Optional[str] = None
    market_cap: Optional[float] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    primary_exchange: Optional[str] = None
    share_class_figi: Optional[str] = None
    share_class_shares_outstanding: Optional[int] = None
    sic_code: Optional[str] = None
    sic_description: Optional[str] = None
    ticker: Optional[str] = None
    total_employees: Optional[int] = None
    type: Optional[str] = None
    weighted_shares_outstanding: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return TickerDetails(
            active=d.get("active", None),
            address=(
                None if "address" not in d else CompanyAddress.from_dict(d["address"])
            ),
            branding=None if "branding" not in d else Branding.from_dict(d["branding"]),
            cik=d.get("cik", None),
            composite_figi=d.get("composite_figi", None),
            currency_name=d.get("currency_name", None),
            currency_symbol=d.get("currency_symbol", None),
            base_currency_name=d.get("base_currency_name", None),
            base_currency_symbol=d.get("base_currency_symbol", None),
            delisted_utc=d.get("delisted_utc", None),
            description=d.get("description", None),
            ticker_root=d.get("ticker_root", None),
            ticker_suffix=d.get("ticker_suffix", None),
            homepage_url=d.get("homepage_url", None),
            list_date=d.get("list_date", None),
            locale=d.get("locale", None),
            market=d.get("market", None),
            market_cap=d.get("market_cap", None),
            name=d.get("name", None),
            phone_number=d.get("phone_number", None),
            primary_exchange=d.get("primary_exchange", None),
            share_class_figi=d.get("share_class_figi", None),
            share_class_shares_outstanding=d.get(
                "share_class_shares_outstanding", None
            ),
            sic_code=d.get("sic_code", None),
            sic_description=d.get("sic_description", None),
            ticker=d.get("ticker", None),
            total_employees=d.get("total_employees", None),
            type=d.get("type", None),
            weighted_shares_outstanding=d.get("weighted_shares_outstanding", None),
        )


@dataclass
class TickerNews:
    "TickerDetails contains data for news articles relating to a stock ticker symbol."
    amp_url: Optional[str] = None
    article_url: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    image_url: Optional[str] = None
    keywords: Optional[List[str]] = None
    published_utc: Optional[str] = None
    publisher: Optional[Publisher] = None
    tickers: Optional[List[str]] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return TickerNews(
            amp_url=d.get("amp_url", None),
            article_url=d.get("article_url", None),
            author=d.get("author", None),
            description=d.get("description", None),
            id=d.get("id", None),
            image_url=d.get("image_url", None),
            keywords=d.get("keywords", None),
            published_utc=d.get("published_utc", None),
            publisher=(
                None if "publisher" not in d else Publisher.from_dict(d["publisher"])
            ),
            tickers=d.get("tickers", None),
            title=d.get("title", None),
        )


@dataclass
class TickerTypes:
    "TickerTypes contains data for ticker types."
    asset_class: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    locale: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return TickerTypes(**d)


@dataclass
class RelatedCompany:
    """
    Get a list of tickers related to the queried ticker based on News and Returns data.
    """

    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return RelatedCompany(
            ticker=d.get("ticker", None),
        )


@dataclass
class TickerChange:
    ticker: str

    @staticmethod
    def from_dict(d):
        return TickerChange(**d)


@dataclass
class TickerChangeEvent:
    type: str
    date: str
    ticker_change: TickerChange

    @staticmethod
    def from_dict(d):
        return TickerChangeEvent(**d)


@dataclass
class TickerChangeResults:
    name: str
    composite_figi: str
    cik: str
    events: Optional[List[TickerChangeEvent]] = None

    @staticmethod
    def from_dict(d):
        return TickerChangeResults(**d)
