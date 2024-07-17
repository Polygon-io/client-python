from dataclasses import dataclass
from typing import Optional


@dataclass
class Split:
    "Split contains data for a historical stock split, including the ticker symbol, the execution date, and the factors of the split ratio."
    execution_date: Optional[str] = None
    split_from: Optional[int] = None
    split_to: Optional[int] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Split(**d)
