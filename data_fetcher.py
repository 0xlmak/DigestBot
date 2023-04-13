import bs4
import requests
import lxml
from bs4 import BeautifulSoup
from typing import List
 
 
class JeuneAfriqueRSSDataSource:
    
    def __init__(self, rss_url: str) -> None:
        self.url = rss_url
        self.r = None
        self.status_code = None
        self.soup = None
        self.articles = None
        self.articles_dicts = None
        self.urls: List[str] = []
        self.titles: List[str] = []
        self.descriptions: List[str] = []
        self.pub_dates: List[str] = []
        
    def get_data(self) -> None:
        try:
            self.r = requests.get(self.url)
            self.status_code = self.r.status_code
        except Exception as e:
            print("Error fetching the URL: ", self.url)
            print(e)
        try:
            self.soup = BeautifulSoup(self.r.text, "lxml")
        except Exception as e:
            print("Could not parse the xml: ", self.url)
            print(e)
        self.articles = self.soup.findAll("item")
        self.articles_dicts = [{"title":a.find("title").text.replace("<![CDATA[", "").replace("]]>", "").replace("\n", "").replace("\t", "").replace("\xa0", "").strip(),"link":a.link.next_sibling.replace("<![CDATA[", "").replace("]]>", "").replace("\n", "").replace("\t", "").strip(),"description":a.find("description").text.replace("<![CDATA[", "").replace("]]>", "").strip(),"pubdate":a.find("pubdate").text.replace("<![CDATA[", "").replace("]]>","").strip()} for a in self.articles]
        self.urls = [d["link"] for d in self.articles_dicts if "link" in d]
        self.titles = [d["title"] for d in self.articles_dicts if "title" in d]
        self.descriptions = [d["description"] for d in self.articles_dicts if "description" in d]
        self.pub_dates = [d["pubdate"] for d in self.articles_dicts if "pubdate" in d]

if __name__ == '__main__':
    # ja_intl_feed = JeuneAfriqueRSSDataSource("https://www.jeuneafrique.com/pays/international/feed/")  # Top international news 
    ja_cmr_feed = JeuneAfriqueRSSDataSource("https://www.jeuneafrique.com/pays/cameroon/feed/")  # Top cameroonian news
    ja_cmr_feed.get_data()
    print(ja_cmr_feed.titles)
