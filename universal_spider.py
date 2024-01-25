import scrapy
import json
import config
from items import UniversalSpiderItem
import logging

logging.getLogger("scrapy").setLevel(logging.INFO)


class UniversalSpider(scrapy.Spider):
    name = "universal_spider"
    custom_settings = {
        "FEEDS": {config.REALSOFT_RAW_FILENAME: {"format": "csv", "overwrite": True}},
        "FEED_EXPORT_FIELDS": [
            "url",
            "img_url",
            "title",
            "price",
            "district",
            "street",
            "category",
            "property_type",
            "property_size",
            "property_condition",
        ],
    }

    def start_requests(self):
        with open("config.json", "r") as file:
            self.configs = json.load(file)

        for config in self.configs:
            yield scrapy.Request(
                url=config["start_url"], callback=self.parse, meta={"config": config}
            )

    def parse(self, response):
        config = response.meta["config"]
        hrefs = response.xpath(config["page_selectors"]["hrefs"]).extract()
        for href in hrefs:
            url = response.urljoin(href)
            yield scrapy.Request(
                url, callback=self.parse_ad_contents, meta={"config": config}
            )

        next_page = response.xpath(config["page_selectors"]["next_page"]).get()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse,
                meta={"config": config},
            )

    def parse_ad_contents(self, response):
        config = response.meta["config"]
        item = UniversalSpiderItem()
        item["url"] = response.url

        for field, selector in config["item_selectors"].items():
            item[field] = (
                response.xpath(selector).get().strip()
                if response.xpath(selector).get()
                else None
            )
        yield item

    def extract_value(self, response, selector):
        return response.xpath(selector).get().strip()
