import scrapy
from ..items import AnotherItem

class AnotherSpider(scrapy.Spider):
    name = 'another'

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = AnotherItem()

        allquotes = response.css('div.quote')

        for quotes in allquotes:

            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            if title:
                items["title"] = title
            else:
                items["title"] = [""]


            if title:
                items["author"] = author
            else:
                items["author"] = [""]


            if tag:
                items["tag"] = tag
            else:
                items["tag"] = [""]

            yield items

        nextpage = response.css('li.next a::attr(href)').get()

        if nextpage is not None:
            yield response.follow(nextpage, callback = self.parse)