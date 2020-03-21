# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:28:24 2020

@author: 09ale
"""

gta_url = 'https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/'
toy_url = 'https://store.steampowered.com/app/1115690/Yes_Your_Grace/'

import pandas as pd 
import numpy as np
import scrapy 
from scrapy.crawler import CrawlerProcess 

class Spider_1 (scrapy.Spider):
    name = 'test_spidur'
    
    def start_requests(self):
        urls = ['https://store.steampowered.com/app/1115690/Yes_Your_Grace/', # ~330 comments
                ]
        for url in urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse)
            
    def parse(self, response):
        #dates = response.css('div.postedDate::text').extract()
        dates = response.css('div.rightcol>a::attr(href)').extract()
        #html_file = 'gtaV_reviews.html'
        #csv_file = ('%s_toy_dates.csv'%(name))
        csv_file = ('toy_links.csv')
        print(dates)
        with open(csv_file, 'wb') as f:
            #f.write(response.body)
            f.writelines([date+'/n' for date in dates])
            
            
process = CrawlerProcess()
process.crawl(Spider_1)
process.start()

