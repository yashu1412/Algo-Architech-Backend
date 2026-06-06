from pydantic import BaseModel
from typing import List

class DataPoint(BaseModel):
    date: str
    value: str

class CommodityResponse(BaseModel):
    name: str
    interval: str
    unit: str
    data: List[DataPoint]
