from .filesManagement import load_json

def get_municipe_by_id(ID: str) -> str:
    MUNICIPALITIES_INFO = load_json(".\\src\\files\\helps\\municipalities.json")
    
    for item in MUNICIPALITIES_INFO:
        if item["id"] == ID:
            return item["name"]
        else:
            None

def drill_schedule(schedule: dict) -> str:
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    days_spanish = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    schedule_html = ""
    for day, day_spanish in zip(days, days_spanish):
        if day in schedule:
            schedule_html += f"<li>{day_spanish.capitalize()}: {schedule[day]['start_time']} - {schedule[day]['end_time']}</li>"
    return schedule_html
