import scrapy
from scrapy.exceptions import CloseSpider
import json

class BooksSpider(scrapy.Spider):
    name = 'books'
    # allowed_domains = ['https://openlibrary.org/subjects/picture_books']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12&offset=12']

    INCREMENTED_BY = 12
    offset = 0 


    def parse(self, response):

        if response.status == 500:
            raise CloseSpider("REACHED LAST PAGE")


        resp = json.loads(response.body)
        works  = resp.get("works")
        
    
        print(response.status)

        for work in works:
            yield{
            "title" :  work.get("title"), 
            # "author" : work.get("authors")[0].get("name")
        }
        
        
        self.offset += self.INCREMENTED_BY
        yield scrapy.Request(
            url =  f'https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}',
            callback = self.parse
        )
        