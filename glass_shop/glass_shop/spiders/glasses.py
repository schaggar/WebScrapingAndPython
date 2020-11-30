# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        for glasses in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']"):
            title = glasses.xpath(".//div[@class='p-title']/a/@title").get()
            url = glasses.xpath(".//div[@class='p-title']/a/@href").get()
            price = glasses.xpath(".//div[@class='p-price']/div/span/text()").get()
            image = glasses.xpath(".//div[@class='product-img-outer']/a/img[@class='lazy d-block w-100 product-img-default']/@src").get()
            yield{
                'title':title,
                'url':url,
                'price':price,
                'ImageURL': image
            }

        next_page = response.xpath("//a[@class='page-link']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)
        

