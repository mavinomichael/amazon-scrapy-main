import scrapy
from ..items import AmazonItem
import re
from scrapy.exporters import JsonLinesItemExporter


class AmazonByCategorySpider(scrapy.Spider):
    name = "amazon_product_by_category_spider"
    page_number = 2
    start_urls = \
        [
            "https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A2476517011&dc&page=1"]

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.HEADERS)

    def parse(self, response):
        product = AmazonItem()

        all_products = response.css(".s-main-slot.s-result-list.s-search-results.sg-row")
        # str_last_item= response.css(".s-pagination-item.s-pagination-disabled::text").get()
        # last_item = str_last_item
        # print("==last item==", str_last_item)
        # last_item = response.css(".s-pagination-disabled::text").get()
        # print(last_item,"lastitem")
        last_item = 400
        exporter = JsonLinesItemExporter(open('products.json', 'ab'))

        for prod in all_products:
            name = prod.css(".a-size-base-plus.a-color-base.a-text-normal::text").get()
            price = prod.css(".a-price-whole::text").get()
            image = "https:" + prod.css(".s-image::attr(src)").get()
            url = "https://www.amazon.com" + prod.css("h2>.a-link-normal::attr(href)").get()

            product['name'] = name
            product['price'] = price
            product['image'] = image
            product['source'] = "amazon"
            product['url'] = url
            # product['last_modified'] = datetime.now().isoformat()

            exporter.export_item(product)

            yield product

        next_page = f'https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A2476517011&dc&page={str(self.page_number)}'

        if self.page_number <= last_item:
            self.page_number += 1
            print(next_page)
            yield response.follow(next_page, callback=self.parse, headers=self.HEADERS)
