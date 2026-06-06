from fastapi import APIRouter, Query
from app.services.alpha_vantage import fetch_all_commodities

router = APIRouter()

@router.get('/commodities')
async def get_commodities(interval: str = Query('monthly')):
    data = await fetch_all_commodities(interval)
    return data
