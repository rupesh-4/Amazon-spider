import scrapy
from ..items import AmazontutorialItem  #AmazontutorialItem is a class present in items.py file

class AmazonSpiderSpider(scrapy.Spider):

    name = 'amazon'
    start_urls = [
        "https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on&p%5B%5D=facets.latest_arrivals%255B%255D%3DLast%2B30%2BDays"
    ]

    def parse(self, response, **kwargs):
        items = AmazontutorialItem()    #create a instance called items for the AmazontutorialItem class

        product_name = response.css('.s1Q9rs').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_image_link = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image_link'] = product_image_link

        yield items

