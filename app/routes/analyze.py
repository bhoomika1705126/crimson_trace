from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.services.analyzer import analyze_csv

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(400, "Only CSV files allowed")
    content = await file.read()
    csv_str = content.decode()
    try:
        result = analyze_csv(csv_str)
        return result
    except Exception as e:
        raise HTTPException(500, str(e))
