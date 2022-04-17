import scrapy
import json

class BooksSpider(scrapy.Spider):
    name = 'books'
    # allowed_domains = ['https://openlibrary.org/subjects/picture_books']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12&offset=12']

    def parse(self, response):
        resp = json.loads(response.body)
        works  = resp.get("works")

        print(response.status)

        for work in works:
            yield{
            "title" :  work.get("title"),
            "author" : work.get("authors")[0].get("name")
        }

        # if response.status == 200:
        #     yield scrapy.Request(
        #         url =  f'https://openlibrary.org/subjects/picture_books.json?limit=12&offset=24',
        #         callback = self.parse
        #     )
        