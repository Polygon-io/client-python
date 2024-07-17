from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SipMapping:
    "Contains data for a mapping to a symbol for each SIP that has a given condition."
    CTA: Optional[str] = None
    OPRA: Optional[str] = None
    UTP: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return SipMapping(**d)


@dataclass
class Consolidated:
    "Contains data for aggregation rules on a consolidated (all exchanges) basis."
    updates_high_low: Optional[bool] = None
    updates_open_close: Optional[bool] = None
    updates_volume: Optional[bool] = None

    @staticmethod
    def from_dict(d):
        return Consolidated(**d)


@dataclass
class MarketCenter:
    "Contains data for aggregation rules on a per-market-center basis."
    updates_high_low: Optional[bool] = None
    updates_open_close: Optional[bool] = None
    updates_volume: Optional[bool] = None

    @staticmethod
    def from_dict(d):
        return MarketCenter(**d)


@dataclass
class UpdateRules:
    "Contains data for a list of aggregation rules."
    consolidated: Optional[Consolidated] = None
    market_center: Optional[MarketCenter] = None

    @staticmethod
    def from_dict(d):
        return UpdateRules(
            consolidated=(
                None
                if "consolidated" not in d
                else Consolidated.from_dict(d["consolidated"])
            ),
            market_center=(
                None
                if "market_center" not in d
                else MarketCenter.from_dict(d["market_center"])
            ),
        )


@dataclass
class Condition:
    "Condition contains data for a condition that Polygon.io uses."
    abbreviation: Optional[str] = None
    asset_class: Optional[str] = None
    data_types: Optional[List[str]] = None
    description: Optional[str] = None
    exchange: Optional[int] = None
    id: Optional[int] = None
    legacy: Optional[bool] = None
    name: Optional[str] = None
    sip_mapping: Optional[SipMapping] = None
    type: Optional[str] = None
    update_rules: Optional[UpdateRules] = None

    @staticmethod
    def from_dict(d):
        return Condition(
            abbreviation=d.get("abbreviation", None),
            asset_class=d.get("asset_class", None),
            data_types=d.get("data_types", None),
            description=d.get("description", None),
            exchange=d.get("exchange", None),
            id=d.get("id", None),
            legacy=d.get("legacy", None),
            name=d.get("name", None),
            sip_mapping=(
                None
                if "sip_mapping" not in d
                else SipMapping.from_dict(d["sip_mapping"])
            ),
            type=d.get("type", None),
            update_rules=(
                None
                if "update_rules" not in d
                else UpdateRules.from_dict(d["update_rules"])
            ),
        )
