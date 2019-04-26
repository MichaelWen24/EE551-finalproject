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

            try:
                title = quotes.css("span.text::text").extract()
            except:
                print("Something Wrong while finding title using css")

            try:
                author = quotes.css(".author::text").extract()
            except:
                print("Something Wrong while finding author using css")

            try:
                tag = quotes.css(".tag::text").extract()
            except:
                print("Something Wrong while finding tag using css")

            # try:
            #     title = quotes.xpath("//span[@class='text']/text()").extract()
            # except:
            #     print("Something Wrong while finding title using Xpath")
            #
            # try:
            #     author = quotes.xpath("//span/small[@class='author']/text()").extract()
            # except:
            #     print("Something Wrong while finding author using Xpath")
            #
            # try:
            #     tag = quotes.xpath("//div/a[@class='tag']/text()").extract()
            # except:
            #     print("Something Wrong while finding tag using Xpath")

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


        #after done first page, go to search next page
        try:
            nextpage = response.css('li.next a::attr(href)').get()
        except:
            print("Something wrong while searching next page")

        if nextpage is not None:
            yield response.follow(nextpage, callback = self.parse)