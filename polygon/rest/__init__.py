from .aggs import AggsClient
from .trades import TradesClient
from .quotes import QuotesClient
from .snapshot import SnapshotClient
from .reference import (
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
)
from .vx import VXClient


class RESTClient(
    AggsClient,
    TradesClient,
    QuotesClient,
    SnapshotClient,
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = VXClient(*args, **kwargs)
