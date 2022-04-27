from .aggs import *
from .trades import *
from .quotes import *
from .markets import *
from .tickers import *
from .splits import *
from .dividends import *

from enum import Enum


class Sort(Enum):
    ASC = "asc"
    DESC = "desc"


class Order(Enum):
    ASC = "asc"
    DESC = "desc"
