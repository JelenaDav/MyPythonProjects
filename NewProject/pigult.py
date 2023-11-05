import pandas as pd
import requests
from bs4 import BeautifulSoup

def pigu_scraper():
    url = "https://pigu.lt/lt/pristatymas"
    response = requests.get(url)  # headers=headers)
    #soup = BeautifulSoup(response.content,"html.parser")
    #pristatymas = soup.find_all()

    print(response.status_code)
pigu_scraper()