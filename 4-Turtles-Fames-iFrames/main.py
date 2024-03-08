import json
import requests as re
from bs4 import BeautifulSoup
import pandas as pd

turtle_info = []
BASE_URL = "https://www.scrapethissite.com"

def get_iframe_link():
    URL = "https://www.scrapethissite.com/pages/frames"
    response = re.get(URL)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    iframe = soup.find(id="iframe")['src']
    return f"{BASE_URL}{iframe}"

def get_iframe_info(URL):
    response = re.get(URL)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    turtles = soup.find_all(class_="turtle-family-card")
    for turtle in turtles:
       turtle_data = {
            "name": turtle.find('h3', class_="family-name").text.strip(),
            "image": turtle.find(class_="turtle-image")['src'],
            "learn_more": f"{BASE_URL}{turtle.find(class_='btn')['href']}"
            
        }

       turtle_info.append(turtle_data)

def output():
    df = pd.DataFrame(turtle_info)
    df.to_csv('turtle_info.csv', index=False)
    df.to_excel('turtle_info.xlsx', index=False)
    df.to_csv      

def main():
    get_iframe_info(get_iframe_link())
    output()
    # for turtle in turtle_info:
    #     print(turtle["name"])
        
    
    
if __name__ == '__main__':
    main()
 

        
    # BASE_URL = "https://www.scrapethissite.com/pages/frames"
    # response = re.get(BASE_URL)
    # webpage = response.text
    # soup = BeautifulSoup(webpage, "html.parser")
    # test = soup.find(id="iframe")
    # print(test['src'])
    # years = sorted([int(year.text.strip()) for year in soup.find_all('a', class_='year-link')])
    
    # pages = []
    # for year in years:
    #     pages.append(f"{BASE_URL}?ajax=true&year={year}")
    # return pages



# BASE_URL = "https://www.scrapethissite.com/pages/frames"
# response = re.get(BASE_URL)
# webpage = response.text
# soup = BeautifulSoup(webpage, "html.parser")
# test = soup.find(id="iframe")
# print(test['src'])
