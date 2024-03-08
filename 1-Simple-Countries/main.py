import requests as re
from bs4 import BeautifulSoup
import pandas as pd

countries_list = []

def request():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = re.get(url)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    return soup

def parse(soup):
    countries_find_all = soup.find_all('h3', class_="country-name")
    capital_find_all = soup.find_all('span', class_="country-capital")
    population_find_all = soup.find_all('span', class_="country-population")
    area_find_all = soup.find_all('span', class_="country-area")
    countries = [country.text.strip() for country in countries_find_all]
    capitals = [capital.text.strip() for capital in capital_find_all]
    populations = [population.text.strip() for population in population_find_all]
    areas = [area.text.strip() for area in area_find_all]
    for n in range(len(countries)):
        country = {
        "name": countries[n],
        "capital": capitals[n],
        "population": int(populations[n]),
        "area": float(areas[n])}
        countries_list.append(country)

def output():
    df = pd.DataFrame(countries_list)
    df.to_csv('1-Simple-Countries.csv', index=False)
    df.to_excel('1-Simple-Countries.xlsx', index=False)
    df.to_csv
    
def main():
    soup = request()
    parse(request())
    output()
    

if __name__ == '__main__':
    main()
