import requests as re
from bs4 import BeautifulSoup
import pandas as pd

team_output = []

def get_all_pages():
    BASE_URL =  "https://www.scrapethissite.com"
    URL = "https://www.scrapethissite.com/pages/forms"
    response = re.get(URL)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    
    pagination = soup.find('ul', class_="pagination")
    pages = []
    for link in pagination.find_all('a'):
        if f"{BASE_URL}{link['href']}" not in pages:
            pages.append(f"{BASE_URL}{link['href']}")
    return pages

def request(URL):

    response = re.get(URL)
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")
    table_data = soup.find('table', class_="table")

    for row in table_data.find_all('tr', class_='team'):
        team_info = {
            "name" : row.find('td', class_="name").text.strip(),
            "year" : row.find('td', class_="year").text.strip(),
            "wins" : row.find('td', class_="wins").text.strip(),
            "losses" : row.find('td', class_="losses").text.strip(),
            "ot_losses" : row.find('td', class_="ot-losses").text.strip(),
            "win_pct" : row.find('td', class_="pct").text.strip(),
            "goals_for" : row.find('td', class_="gf").text.strip(),
            "goals_against" : row.find('td', class_="ga").text.strip(),
            "plus_minus":  row.find('td', class_="diff").text.strip()
        }
        
        team_output.append(team_info)

def output():
    df = pd.DataFrame(team_output)
    df.to_csv('team_info.csv', index=False)
    df.to_excel('team_info.xlsx', index=False)
    df.to_csv       
        
def main():
    for url in get_all_pages():
        request(url)
    output()
    
  
if __name__ == '__main__':
    main()
 
