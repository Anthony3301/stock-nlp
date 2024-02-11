import requests
from bs4 import BeautifulSoup

def scrape_yahoo_finance_articles():
    """scrapes recent articles of stock information from yahoo finance

    Returns:
        list(pair(str, str)): list of source and headline
    """
    totalArticles = []
    
    base_url = 'https://finance.yahoo.com/news/'

    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', {'class': "Ov(h) Pend(44px) Pstart(25px)"})

        for article in articles:
            source = article.find('div').text
            headline = article.find('a').text
            
            totalArticles.append([source, headline])


    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        
    
    return totalArticles
