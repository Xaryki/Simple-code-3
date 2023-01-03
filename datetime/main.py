from datetime import datetime
from pytz import timezone


def date_changer(day: int):
    dt_now = datetime.now(timezone('Europe/Moscow'))
    dt_now = dt_now.replace(day=dt_now.day + day)
    week= dt_now.isocalendar().week
    dt_now = dt_now.strftime("%Y-%m-%d")
    return dt_now,week
