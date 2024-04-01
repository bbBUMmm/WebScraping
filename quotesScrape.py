from bs4 import BeautifulSoup
import requests
import csv

target = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(target.text, "html.parser")
quotes = soup.findAll("span", attrs={"class": "text"})

file = open("quotes.csv", "w", newline='', encoding='utf-8')  # Add encoding and newline=''
writer = csv.writer(file)

writer.writerow(["Quotes"])  # Pass the header as a list

# all quotes
for quote in quotes:
    writer.writerow([quote.text])  # Pass each quote as a list containing only one element

file.close()
