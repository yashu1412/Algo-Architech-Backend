from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import commodities

app = FastAPI(title='Commodity Price API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://localhost:3001'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(commodities.router, prefix='/api')
