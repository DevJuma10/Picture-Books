import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['https://openlibrary.org/subjects/picture_books']
    start_urls = ['http://https://openlibrary.org/subjects/picture_books/']

    def parse(self, response):
        pass
