import json
import requests as re
from bs4 import BeautifulSoup
import pandas as pd

film_output  = []
json_film_output = 'file_out.json'

def get_all_pages():
    BASE_URL = "https://www.scrapethissite.com/pages/ajax-javascript/"
    response = re.get(BASE_URL)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    years = sorted([int(year.text.strip()) for year in soup.find_all('a', class_='year-link')])
    
    pages = []
    for year in years:
        pages.append(f"{BASE_URL}?ajax=true&year={year}")
    return pages

def request(URL):
    response = re.get(URL)
    response.raise_for_status()
    data = response.json()
    film_output.extend(data)
       

def output():
    with open(json_film_output, 'w') as file:
            json.dump(film_output, file, indent=4)
    
    df = pd.read_json(json_film_output)
    df.to_csv('film_info.csv', index=False)
    df.to_excel('film_info.xlsx', index=False)
   
def main():
    for page in get_all_pages():
        request(page)
    output()
    
if __name__ == '__main__':
    main()
 
