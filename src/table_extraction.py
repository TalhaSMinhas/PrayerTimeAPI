import pymupdf
import pandas as pd

doc = pymupdf.open("/home/tsminhas/PycharmProjects/PrayerTimeAPI/files/times.pdf")
# page 0 is page 1

list_of_times = []

for i in range(0,12):
    page = doc[i]
    find = page.find_tables()
    table = find.tables[0]
    list_of_times.append(table)

extracted_times = []

for table in list_of_times:
    extracted_table = table.extract()
    extracted_times.append(extracted_table)

prayer_df = pd.DataFrame(extracted_times)

months = ["January", "February", "March", "April", "May","June", "July", "August", "September","October","November","December"]

print(prayer_df[months.index("January")])