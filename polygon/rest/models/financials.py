from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class DataPoint:
    "An individual financial data point."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return DataPoint(**d)


@dataclass
class ExchangeGainsLosses:
    "Contains exchange gains losses data for a cash flow statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return ExchangeGainsLosses(**d)


@dataclass
class NetCashFlow:
    "Contains net cash flow data for a cash flow statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return NetCashFlow(**d)


@dataclass
class NetCashFlowFromFinancingActivities:
    "Contains net cash flow from financing activities data for a cash flow statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return NetCashFlowFromFinancingActivities(**d)


@dataclass
class CashFlowStatement:
    "Contains cash flow statement data."
    exchange_gains_losses: Optional[ExchangeGainsLosses] = None
    net_cash_flow: Optional[NetCashFlow] = None
    net_cash_flow_from_financing_activities: Optional[
        NetCashFlowFromFinancingActivities
    ] = None

    @staticmethod
    def from_dict(d):
        return CashFlowStatement(
            exchange_gains_losses=(
                None
                if "exchange_gains_losses" not in d
                else ExchangeGainsLosses.from_dict(d["exchange_gains_losses"])
            ),
            net_cash_flow=(
                None
                if "net_cash_flow" not in d
                else NetCashFlow.from_dict(d["net_cash_flow"])
            ),
            net_cash_flow_from_financing_activities=(
                None
                if "net_cash_flow_from_financing_activities" not in d
                else NetCashFlowFromFinancingActivities.from_dict(
                    d["net_cash_flow_from_financing_activities"]
                )
            ),
        )


@dataclass
class ComprehensiveIncomeLoss:
    "Contains comprehensive income loss data for comprehensive income."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return ComprehensiveIncomeLoss(**d)


@dataclass
class ComprehensiveIncomeLossAttributableToParent:
    "Contains comprehensive income loss attributable to parent data for comprehensive income."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return ComprehensiveIncomeLossAttributableToParent(**d)


@dataclass
class OtherComprehensiveIncomeLoss:
    "Contains other comprehensive income loss data for comprehensive income."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OtherComprehensiveIncomeLoss(**d)


@dataclass
class ComprehensiveIncome:
    "Contains comprehensive income data."
    comprehensive_income_loss: Optional[ComprehensiveIncomeLoss] = None
    comprehensive_income_loss_attributable_to_parent: Optional[
        ComprehensiveIncomeLossAttributableToParent
    ] = None
    other_comprehensive_income_loss: Optional[OtherComprehensiveIncomeLoss] = None

    @staticmethod
    def from_dict(d):
        return ComprehensiveIncome(
            comprehensive_income_loss=(
                None
                if "comprehensive_income_loss" not in d
                else ComprehensiveIncomeLoss.from_dict(d["comprehensive_income_loss"])
            ),
            comprehensive_income_loss_attributable_to_parent=(
                None
                if "comprehensive_income_loss_attributable_to_parent" not in d
                else ComprehensiveIncomeLossAttributableToParent.from_dict(
                    d["comprehensive_income_loss_attributable_to_parent"]
                )
            ),
            other_comprehensive_income_loss=(
                None
                if "other_comprehensive_income_loss" not in d
                else OtherComprehensiveIncomeLoss.from_dict(
                    d["other_comprehensive_income_loss"]
                )
            ),
        )


@dataclass
class BasicEarningsPerShare:
    "Contains basic earning per share data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return BasicEarningsPerShare(**d)


@dataclass
class CostOfRevenue:
    "Contains cost of revenue data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return CostOfRevenue(**d)


@dataclass
class GrossProfit:
    "Contains gross profit data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return GrossProfit(**d)


@dataclass
class OperatingExpenses:
    "Contains operating expenses data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OperatingExpenses(**d)


@dataclass
class Revenues:
    "Contains revenues data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Revenues(**d)


@dataclass
class IncomeStatement:
    "Contains income statement data."
    basic_earnings_per_share: Optional[BasicEarningsPerShare] = None
    cost_of_revenue: Optional[CostOfRevenue] = None
    gross_profit: Optional[GrossProfit] = None
    operating_expenses: Optional[OperatingExpenses] = None
    revenues: Optional[Revenues] = None

    @staticmethod
    def from_dict(d):
        return IncomeStatement(
            basic_earnings_per_share=(
                None
                if "basic_earnings_per_share" not in d
                else BasicEarningsPerShare.from_dict(d["basic_earnings_per_share"])
            ),
            cost_of_revenue=(
                None
                if "cost_of_revenue" not in d
                else CostOfRevenue.from_dict(d["cost_of_revenue"])
            ),
            gross_profit=(
                None
                if "gross_profit" not in d
                else GrossProfit.from_dict(d["gross_profit"])
            ),
            operating_expenses=(
                None
                if "operating_expenses" not in d
                else OperatingExpenses.from_dict(d["operating_expenses"])
            ),
            revenues=None if "revenues" not in d else Revenues.from_dict(d["revenues"]),
        )


@dataclass
class Financials:
    "Contains financial data."
    balance_sheet: Optional[Dict[str, DataPoint]] = None
    cash_flow_statement: Optional[CashFlowStatement] = None
    comprehensive_income: Optional[ComprehensiveIncome] = None
    income_statement: Optional[IncomeStatement] = None

    @staticmethod
    def from_dict(d):
        return Financials(
            balance_sheet=(
                None
                if "balance_sheet" not in d
                else {
                    k: DataPoint.from_dict(v) for (k, v) in d["balance_sheet"].items()
                }
            ),
            cash_flow_statement=(
                None
                if "cash_flow_statement" not in d
                else CashFlowStatement.from_dict(d["cash_flow_statement"])
            ),
            comprehensive_income=(
                None
                if "comprehensive_income" not in d
                else ComprehensiveIncome.from_dict(d["comprehensive_income"])
            ),
            income_statement=(
                None
                if "income_statement" not in d
                else IncomeStatement.from_dict(d["income_statement"])
            ),
        )


@dataclass
class StockFinancial:
    "StockFinancial contains historical financial data for a stock ticker."
    cik: Optional[str] = None
    company_name: Optional[str] = None
    end_date: Optional[str] = None
    filing_date: Optional[str] = None
    financials: Optional[Financials] = None
    fiscal_period: Optional[str] = None
    fiscal_year: Optional[str] = None
    source_filing_file_url: Optional[str] = None
    source_filing_url: Optional[str] = None
    start_date: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return StockFinancial(
            cik=d.get("cik", None),
            company_name=d.get("company_name", None),
            end_date=d.get("end_date", None),
            filing_date=d.get("filing_date", None),
            financials=(
                None if "financials" not in d else Financials.from_dict(d["financials"])
            ),
            fiscal_period=d.get("fiscal_period", None),
            fiscal_year=d.get("fiscal_year", None),
            source_filing_file_url=d.get("source_filing_file_url", None),
            source_filing_url=d.get("source_filing_url", None),
            start_date=d.get("start_date", None),
        )
