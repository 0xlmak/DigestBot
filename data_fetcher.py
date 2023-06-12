from typing import Dict
from dataclasses import dataclass
from diskcache import Cache
import feedparser


@dataclass
class RSSDataSource:
    rss_url: str

    def get_data(self) -> Dict[str, str]:
        feed = feedparser.parse(self.rss_url)
        # dictionary for articles details
        articles_details = {}
        article_list = []
        i = 0
        for entry in feed.entries:
            tmp = dict()
            i += 1
            tmp["id"] = str(i)
            tmp["title"] = entry.title
            tmp["link"] = entry.link
            tmp["author"] = entry.author
            tmp["time_published"] = entry.published
            tmp["tags"] = [tag.term for tag in entry.tags]
            tmp["authors"] = [author.name for author in entry.authors]
            tmp["summary"] = entry.summary
            article_list.append(tmp)

        
        articles_details["articles"] = article_list

      
        return articles_details

if __name__ == "__main__":
    import json
  
    feed_url = "https://www.jeuneafrique.com/rubriques/politique/feed/"
    ja_feed = RSSDataSource(feed_url)
    data = ja_feed.get_data() 
    
    if data:
        # printing as a json string with indentation level = 2
        print(json.dumps(data, indent=2, ensure_ascii=False)) 
    else:
        print("None")
