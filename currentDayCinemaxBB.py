# TODO: implement searching films from CInemaxBB
import csv

from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.cine-max.sk/#"
response = requests.get(url)

print(response.text)
