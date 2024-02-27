from fastapi import FastAPI, HTTPException
from datetime import datetime
from scraping.uf_scraper import get_uf_value

app = FastAPI()

@app.get("/uf-value/{date_str}")
async def uf_value(date_str: str):
    """
    Get the value of UF for a specific date.
    """
    if not date_str:
        raise HTTPException(
            status_code=400, 
            detail="Debe proporcionar una fecha."
        )

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=400, 
            detail="Formato de fecha inválido. Por favor use YYYY-MM-DD."
        )
    
    try:
        uf_value = get_uf_value(date.year, date.month, date.day)
        return {"uf_value": uf_value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
