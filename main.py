# main.py
from lookup import PnuLookup
from fastapi import FastAPI, Query
import os

app = FastAPI()
csv_path = os.path.join(os.path.dirname(__file__), "pnu10.csv")
pnu_lookup = PnuLookup(csv_path)

@app.get("/")
def root():
    return {"message": "✅ PNU 변환 API. 예시: /pnu/convert?query=서울 서초구 양재동"}

@app.get("/pnu/convert")
def convert(query: str = Query(..., description="예: 서울 서초구 양재동")):
    return pnu_lookup.lookup(query)
