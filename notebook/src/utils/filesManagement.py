import json
import pandas as pd
from typing import Any, List, Dict

def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r") as file:
        return json.load(file)

def extract_info(json_path: str) -> List[Dict[str, Any]]:
    
    df = pd.read_json(json_path)
    data = []
    
    for index, row in df.iterrows():
        data.append({
            "name": row["name"],
            "municipality": row["localization"]["municipality"],
            "coordinates": [row["localization"]["coordinates"]["latitude"], 
                            row["localization"]["coordinates"]["longitude"]],
            "cuisine": row["cuisine"],
            "services": row["services"],
            "payment": row["payment"],
            "schedules": row["schedules"],
            "food": row["menu"]["food"],
            "drinks": row["menu"]["drinks"]
        })
    
    return data