from dataclasses import dataclass
from typing import Optional


@dataclass
class Dividend:
    "Dividend contains data for a historical cash dividend, including the ticker symbol, declaration date, ex-dividend date, record date, pay date, frequency, and amount."
    cash_amount: Optional[float] = None
    currency: Optional[str] = None
    declaration_date: Optional[str] = None
    dividend_type: Optional[str] = None
    ex_dividend_date: Optional[str] = None
    frequency: Optional[int] = None
    pay_date: Optional[str] = None
    record_date: Optional[str] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Dividend(**d)
