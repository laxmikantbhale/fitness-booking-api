from datetime import datetime
from zoneinfo import ZoneInfo

def convert_to_timezone(dt: datetime, tz: str) -> datetime:
    return dt.astimezone(ZoneInfo(tz))