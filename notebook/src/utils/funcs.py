from .filesManagement import load_json
from typing import Any, List, Dict

def get_municipe_by_id(ID: str) -> str | None:
    MUNICIPALITIES_INFO = load_json(".\\src\\files\\helps\\municipalities.json")
    
    for item in MUNICIPALITIES_INFO:
        if item["id"] == ID:
            return item["name"]
        else:
            None

def drill_schedule(schedule: dict) -> str:
    days: List[str] = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    days_spanish: List[str] = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    schedule_html: str = ""
    for day, day_spanish in zip(days, days_spanish):
        if day in schedule:
            schedule_html += f"<li>{day_spanish.capitalize()}: {schedule[day]['start_time']} - {schedule[day]['end_time']}</li>"
    return schedule_html


def filter_lists(data_list: List[Dict[str, Any]], key: str) -> List[Dict[str, List[str]]]:
    mun_with_info: Dict = {}

    for item in data_list:
        if item.get(key) is not None:
            municipality: str = item["municipality"]

            if municipality in mun_with_info:
                mun_with_info[municipality].extend(item[key])
            else:
                mun_with_info[municipality] = item[key]

    result = [{municipality: new_filter} for municipality, new_filter in mun_with_info.items()]

    return result