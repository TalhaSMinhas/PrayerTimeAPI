import requests
from bs4 import BeautifulSoup
from hijridate import Hijri, Gregorian
from datetime import datetime, timedelta

DATE_DIFFERENTIAL = 1

# getting hijri date for south africa due difference in global moon sightings
today = datetime.today() - timedelta(days = DATE_DIFFERENTIAL)
today_string = today.strftime("%Y-%m-%d")
year, month, day = map(int, today_string.split('-'))
hijri_date = Gregorian(year,month,day).to_hijri()

formatted_hijri_date = f"{hijri_date.day} {hijri_date.month_name('en')} {hijri_date.year} AH"

print(formatted_hijri_date)
