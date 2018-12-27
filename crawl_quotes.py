from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes.spiders.quotesspider import QuotesspiderSpider

process = CrawlerProcess(get_project_settings())
process.crawl(QuotesspiderSpider)
process.start()
