import csv

from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all("table")[0]

ths = table.find_all("th", {"scope": "col"} or {"rowspan": 2} or {})

clear_ths = [th.text.strip() for th in ths]
clear_ths.pop(0)
clear_ths.pop(-1)
clear_ths.pop(-1)

data_frame = pd.DataFrame(columns=clear_ths)

column_data = table.find_all('tr')
for row in column_data[2:]:
    row_datas = row.find_all('td')
    cl_row_data = [row_data.text.strip() for row_data in row_datas]
    # Check if the length of the row matches the length of the column headers
    # print(str(len(cl_row_data)) + " clear ths : len: " + str(len(clear_ths)))
    if len(cl_row_data) == len(clear_ths):
        lenght_of_df = len(data_frame)
        data_frame.loc[lenght_of_df] = cl_row_data
    else:
        print("Mismatched columns in row:", cl_row_data)

data_frame.to_csv("wikiTabel.csv", index=False, quoting=csv.QUOTE_ALL)
