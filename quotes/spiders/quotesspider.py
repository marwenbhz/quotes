# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from quotes.items import QuotesItem


class QuotesspiderSpider(scrapy.Spider):
    name = 'quotesspider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    #custom_settings = {
    #'LOG_FILE': 'logs/quotes.log',
    #'LOG_LEVEL':'DEBUG'
    # }


    def parse(self, response):

        print('PROCESSING...' + response.url)

        quotes = response.xpath("//div[@class='quote']")
	for quote in quotes:
	    item = QuotesItem()
	    item['text'] = quote.xpath(".//span[@class='text']/text()").extract_first()
            item['author'] = quote.xpath(".//small//text()").extract_first()
	    item['tags'] = quote.css('div.tags > a::text').extract()
	    yield item

	relative_next_url = response.css('li.next > a::attr(href)').extract_first()
	if relative_next_url is not None:
	    absolute_next_url = response.urljoin(relative_next_url)
	    yield Request(absolute_next_url, callback=self.parse)

