import scrapy
import requests
from bs4 import BeautifulSoup


class spider(scrapy.Spider):
    name = 'grant-spider'
    custom_settings = {

    'DOWNLOAD_DELAY': 5,
    'CONCURRENT_REQUESTS_PER_DOMAIN' : 16,
    'CONCURRENT_REQUESTS_PER_IP' : 16,
    'AUTOTHROTTLE_ENABLED': True,
    'AUTOTHROTTLE_START_DELAY' : 5,

    }
    start_urls = ['https://www.bankofamerica.com/philanthropic/search/?program=4003&area=CT']
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')