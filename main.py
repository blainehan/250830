from fastapi import FastAPI, Query
from lookup import PnuLookup

app = FastAPI()
pnu_lookup = PnuLookup("pnu10.csv")

@app.get("/pnu/convert")
def convert(query: str = Query(..., description="지역명 예: 서울 서초구 양재동")):
    return pnu_lookup.lookup(query)