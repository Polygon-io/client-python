from dataclasses import dataclass
from typing import Optional


@dataclass
class Exchange:
    "Exchange contains data for a condition that Polygon.io uses."
    acronym: Optional[str] = None
    asset_class: Optional[str] = None
    id: Optional[int] = None
    locale: Optional[str] = None
    mic: Optional[str] = None
    name: Optional[str] = None
    operating_mic: Optional[str] = None
    participant_id: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Exchange(**d)
