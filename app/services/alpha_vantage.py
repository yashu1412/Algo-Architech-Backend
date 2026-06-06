from fastapi import HTTPException
import httpx, os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = 'https://www.alphavantage.co/query'

async def fetch_all_commodities(interval: str = 'monthly'):
    params = {
        'function': 'ALL_COMMODITIES',
        'interval': interval,
        'apikey': os.getenv('ALPHA_VANTAGE_API_KEY', 'demo'),
    }
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(BASE_URL, params=params)
            r.raise_for_status()
            data = r.json()
            
            # Alpha Vantage returns 200 OK even for errors, but with specific keys
            if "Error Message" in data:
                raise HTTPException(status_code=400, detail=data["Error Message"])
            if "Note" in data:
                # This is usually the API limit reached message
                raise HTTPException(status_code=429, detail=data["Note"])
            if "Information" in data:
                raise HTTPException(status_code=200, detail=data["Information"])
                
            return data
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"API Request failed: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
