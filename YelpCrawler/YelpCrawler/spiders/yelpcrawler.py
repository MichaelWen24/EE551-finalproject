import scrapy
from ..items import YelpcrawlerItem


class YelpSpider(scrapy.Spider):
    name = "yelp"

#   Define your scrape websites here
    start_urls = [
        #"https://www.yelp.com/search?find_desc=&find_loc=hoboken%2C+NJ&ns=1"
        "https://www.yelp.com/biz/fiore-deli-of-hoboken-hoboken"
    ]


    def parse(self, response):
# #---------------------------this part is testing this crawler whether is able to download or not
#         items = YelpcrawlerItem()
#         Name = response.xpath(
#             '//div[contains(@class, "biz-page-header")]//h1[contains(@class, "biz-page-title")]/text()').extract()
#         Category = response.xpath('//span[@class="category-str-list"]/a/text()').extract()
#         Rating = response.xpath(
#             '//div[contains(@class, "biz-page-header")]//div[contains(@class, "biz-rating")]/div[contains(@class, "i-stars")]/@title').extract()
#         Address = response.css("address::text").extract()
#         # response.xpath("//div[contains(@class, 'mapbox-address')]//text()").extract()
#         PhoneNumber = response.css("span.biz-phone::text").extract()
#
#         items["Name"] = Name
#         items["Category"] = Category
#         items["Rating"] = Rating
#         items["Address"] = Address
#         items["PhoneNumber"] = PhoneNumber
#
#         yield items
# #------------------------------------------------------------

        for pageurl in response.xpath('//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div[2]/div/div/a/@href').extract():
             pageurl = response.urljoin(pageurl)
             try:
                yield scrapy.Request(pageurl, callback=self.allpages)
             except:
                 print("Something wrong with page lists")

    def allpages(self, response):

        for pages in response.xpath('//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/ul/li/div/div/div/div/div[2]/div[1]'):
            if pages.xpath('div[1]/div[1]/div[1]/h3/span').extract():
                continue
            restauranturl = response.urljoin(pages.xpath('div[1]/div[1]/div[1]/h3/a/@href').extract_first())
            try:
                yield scrapy.Request(restauranturl,meta=restauranturl, callback=self.restaurantdetails)
            except:
                print("Something wrong with pages")


    def restaurantdetails(self, response):

        items = YelpcrawlerItem()
        Name = response.xpath(
            '//div[contains(@class, "biz-page-header")]//h1[contains(@class, "biz-page-title")]/text()').extract()
        Category = response.xpath('//span[@class="category-str-list"]/a/text()').extract()
        Rating = response.xpath(
            '//div[contains(@class, "biz-page-header")]//div[contains(@class, "biz-rating")]/div[contains(@class, "i-stars")]/@title').extract()
        Address = response.css("address::text").extract()
        # response.xpath("//div[contains(@class, 'mapbox-address')]//text()").extract()
        PhoneNumber = response.css("span.biz-phone::text").extract()

        items["Name"] = Name
        items["Category"] = Category
        items["Rating"] = Rating
        items["Address"] = Address
        items["PhoneNumber"] = PhoneNumber

        yield items
        #restaurant_name_section = response.xpath('//*[starts-with(@class, "biz-page-header-left")]')
        #restaurant_name = restaurant_name_section.xpath('//*/h1/text()').extract()
        ##restaurant_name = restaurant_name_section.xpath('//*/h1/text()').extract_first()
        #try:
        #    restaurantname = '|'.join(
        #        restaurant_name_section.xpath('//*[starts-with(@class, "alternate-names")]/text()').extract()).strip()
        #    alter_names = alter_names
        #except Exception as e:

        # restaurant_name = response.xpath('//div[contains(@class, "biz-page-header")]//h1[contains(@class, "biz-page-title")]/text()').extract()
         # restaurant_category = response.xpath('//span[@class="category-str-list"]/a/text()').extract()
         # restaurant_rating = response.xpath('//div[contains(@class, "biz-page-header")]//div[contains(@class, "biz-rating")]/div[contains(@class, "i-stars")]/@title').extract()
         # restaurant_address =  response.css("address::text").extract()
         # # response.xpath("//div[contains(@class, 'mapbox-address')]//text()").extract()
         # restaurant_phone = response.css("span.biz-phone::text").extract(
         #
         # yield {
         #     "Name": restaurant_name,
         #     "Category": restaurant_category,
         #     "rating": restaurant_rating,
         #     "Address": restaurant_address,
         #     "PhoneNumber": restaurant_phone
         # }
