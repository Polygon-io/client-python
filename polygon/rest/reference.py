from .base import BaseClient
from typing import Optional, Any, Dict, List, Union, Iterator
from .models import (
    MarketHoliday,
    MarketStatus,
    Ticker,
    TickerDetails,
    TickerNews,
    TickerTypes,
    Sort,
    Order,
    AssetClass,
    Locale,
    Split,
)
from urllib3 import HTTPResponse

# https://polygon.io/docs/stocks
class MarketsClient(BaseClient):
    def list_market_holidays(
        self, params: Optional[Dict[str, Any]] = None, raw: bool = False
    ) -> Union[List[MarketHoliday], HTTPResponse]:
        """
        Get upcoming market holidays and their open/close times.

        :param params: Any additional query params
        :param raw: Return HTTPResponse object instead of results object
        :return: List of quotes
        """
        url = "/v1/marketstatus/upcoming"

        return self._get(
            path=url, params=params, deserializer=MarketHoliday.from_dict, raw=raw
        )

    def get_market_status(
        self, params: Optional[Dict[str, Any]] = None, raw: bool = False
    ) -> Union[MarketStatus, HTTPResponse]:
        """
        Get the current trading status of the exchanges and overall financial markets.

        :param params: Any additional query params
        :param raw: Return HTTPResponse object instead of results object
        :return: List of quotes
        """
        url = "/v1/marketstatus/now"

        return self._get(
            path=url, params=params, deserializer=MarketStatus.from_dict, raw=raw
        )


class TickersClient(BaseClient):
    def list_tickers(
        self,
        ticker: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        type: Optional[str] = None,
        market: Optional[str] = None,
        exchange: Optional[str] = None,
        cusip: Optional[int] = None,
        cik: Optional[int] = None,
        date: Optional[str] = None,
        active: Optional[bool] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[Iterator[Ticker], HTTPResponse]:
        """
        Query all ticker symbols which are supported by Polygon.io. This API currently includes Stocks/Equities, Crypto, and Forex.
        :param ticker: Specify a ticker symbol. Defaults to empty string which queries all tickers.
        :param ticker_lt: Ticker less than
        :param ticker_lte: Ticker less than or equal to
        :param ticker_gt: Ticker greater than
        :param ticker_gte: Ticker greater than or equal to
        :param type: Specify the type of the tickers. Find the types that we support via our Ticker Types API. Defaults to empty string which queries all types.
        :param market: Filter by market type. By default all markets are included.
        :param exchange: Specify the primary exchange of the asset in the ISO code format. Find more information about the ISO codes at the ISO org website. Defaults to empty string which queries all exchanges.
        :param cusip: Specify the CUSIP code of the asset you want to search for. Find more information about CUSIP codes at their website. Defaults to empty string which queries all CUSIPs.
        :param cik: Specify the CIK of the asset you want to search for. Find more information about CIK codes at their website. Defaults to empty string which queries all CIKs.
        :param date: Specify a point in time to retrieve tickers available on that date. Defaults to the most recent available date.
        :param search: Search for terms within the ticker and/or company name.
        :param active: Specify if the tickers returned should be actively traded on the queried date. Default is true.
        :param limit: Limit the size of the response, default is 100 and max is 1000.
        :param sort: The field to sort the results on. Default is ticker. If the search query parameter is present, sort is ignored and results are ordered by relevance.
        :param order: The order to sort the results on. Default is asc (ascending).
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: List of tickers
        """
        url = "/v3/reference/tickers"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_tickers, locals()),
            raw=raw,
            deserializer=Ticker.from_dict,
        )

    def get_ticker_details(
        self,
        ticker: Optional[str] = None,
        date: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[TickerDetails, HTTPResponse]:
        """
        Get a single ticker supported by Polygon.io. This response will have detailed information about the ticker and the company behind it.
        :param ticker: The ticker symbol of the asset.
        :param date: Specify a point in time to get information about the ticker available on that date. When retrieving information from SEC filings, we compare this date with the period of report date on the SEC filing.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: Ticker Details V3
        """
        url = f"/v3/reference/tickers/{ticker}"

        return self._get(
            path=url, params=params, deserializer=TickerDetails.from_dict, raw=raw
        )

    def get_ticker_news(
        self,
        ticker: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        published_utc: Optional[str] = None,
        published_utc_lt: Optional[str] = None,
        published_utc_lte: Optional[str] = None,
        published_utc_gt: Optional[str] = None,
        published_utc_gte: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[TickerDetails, HTTPResponse]:
        """
        Get the most recent news articles relating to a stock ticker symbol, including a summary of the article and a link to the original source.
        :param ticker: Return results that contain this ticker.
        :param published_utc: Return results published on, before, or after this date.
        :param limit: Limit the number of results returned, default is 10 and max is 1000.
        :param sort: Sort field used for ordering.
        :param order: Order results based on the sort field.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: Ticker News
        """
        url = "/v2/reference/news"

        return self._get(
            path=url, params=params, deserializer=TickerNews.from_dict, raw=raw
        )

    def get_ticker_types(
        self,
        asset_class: Optional[AssetClass] = None,
        locale: Optional[Locale] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[TickerTypes, HTTPResponse]:
        """
        List all ticker types that Polygon.io has.
        :param asset_class: Filter by asset class.
        :param locale: Filter by locale.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: Ticker Types
        """
        url = "/v3/reference/tickers/types"

        return self._get(
            path=url, params=params, deserializer=TickerTypes.from_dict, raw=raw
        )


class SplitsClient(BaseClient):
    def list_splits(
        self,
        ticker: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        execution_date: Optional[str] = None,
        execution_lt: Optional[str] = None,
        execution_lte: Optional[str] = None,
        execution_gt: Optional[str] = None,
        execution_gte: Optional[str] = None,
        reverse_split: Optional[bool] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[Iterator[Split], HTTPResponse]:
        """
        Get a list of historical stock splits, including the ticker symbol, the execution date, and the factors of the split ratio.

        :param ticker: Return the stock splits that contain this ticker.
        :param ticker_lt: Ticker less than
        :param ticker_lte: Ticker less than or equal to
        :param ticker_gt: Ticker greater than
        :param ticker_gte: Ticker greater than or equal to
        :param execution_date: Query by execution date with the format YYYY-MM-DD.
        :param execution_date_lt: Execution date less than
        :param execution_date_lte: Execution date less than or equal to
        :param execution_date_gt: Execution date greater than
        :param execution_date_gte: Execution date greater than or equal to
        :param reverse_split: Query for reverse stock splits. A split ratio where split_from is greater than split_to represents a reverse split. By default this filter is not used.
        :param limit: Limit the number of results returned, default is 10 and max is 1000.
        :param sort: Sort field used for ordering.
        :param order: Order results based on the sort field.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: List of splits
        """
        url = "/v3/reference/splits"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_splits, locals()),
            raw=raw,
            deserializer=Split.from_dict,
        )
