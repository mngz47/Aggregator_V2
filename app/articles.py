
from bs4 import BeautifulSoup

import requests

class articles:

    category = ''
    
    def __init__(self, category):
        self.category = category
    
    categories = []
   
    articles = []
    
    def findCategories(self):
        r = requests.get('https://plrplr.com')
        soup = BeautifulSoup(r.content, 'html.parser')
        for a_tag in soup.find_all('a'):
            if category.__contains__(a_tag.get_text()):
                link = str(a_tag.get('href'))
            if link.startswith('https://www.plrplr.com/') and not (link.endswith(".html") or link.endswith('.htm')) and link not in self.excludedlinks:
                self.categories.append(link)

    def findArticles(self):
        for aa in self.categories:
            r = requests.get(aa)
            soup = BeautifulSoup(r.content, 'html.parser')
            for a_tag in soup.find_all('a'):
                link = str(a_tag.get('href'))
                if link.startswith('https://www.plrplr.com/') and not (link.endswith(".html") or link.endswith('.htm')) and link not in self.excludedlinks:
                    self.articles.append(link)

    def getArticleBody(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        body = []
        body[0] = soup.find('h', attrs={'class': 'entry-title'}).get_text()
        body[1] = soup.find('div', attrs={'class': 'entry-content'}).get_text()
        return body
