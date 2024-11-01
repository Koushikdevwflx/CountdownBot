import os
from datetime import date, timedelta
from json import dumps

try:
    # Calculate countdown
    days = date(2024, 9, 27) - date.today() - timedelta(days=1)
    cd = dumps(days.days, default=str)
    print("Days countdown:", cd)  # Print instead of tweeting
except Exception as e:
    print("An error occurred:", e)
