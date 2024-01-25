from scrapy.item import Item, Field


class UniversalSpiderItem(Item):
    url = Field()
    img_url = Field()
    title = Field()
    price = Field()
    district = Field()
    street = Field()
    category = Field()
    property_type = Field()
    property_size = Field()
    property_condition = Field()
