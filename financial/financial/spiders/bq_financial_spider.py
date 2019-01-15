# -*- coding: utf-8 -*-

# 百全好车 www.bqhaoche.com

import sys
sys.path.append('/Users/zhuangganglong/car_spider/')
import scrapy
from ..items import FinancialItem
from scrapy_splash import SplashRequest
import requests
import json
import re
import time
from class_func import func


class bqFinancialSpider(scrapy.Spider):
    name = "bq"
    allowed_domains = ["www.bqhaoche.com"]
    url = 'http://www.bqhaoche.com/product.php?'

    def start_requests(self):
        for i in range(1, 4):
            yield scrapy.Request(url=self.url + 'page=' + str(i), callback=self.parse)

    def parse(self, response):
        carList = response.xpath('/html/body/div[2]/article[@class="car-buy"]/section/ul[@class="buy-con"]/li')
        for car in carList:
            link = car.xpath('a/@href')[0].extract()
            carId = (link.split('='))[1]
            yield scrapy.Request(url=link, callback=self.detail_parse, meta={'carId': carId})

    def detail_parse(self, response):
        brandList = ['起亚', '别克', '大众', '中华', '标致', '雪佛兰', '福特', '迈腾',
                     '现代', '开瑞', '长安', '众泰', '丰田', '北汽幻速', 'Jeep', '哈弗']
        item = FinancialItem()
        detail = response.xpath('/html/body/div[@class="header"]/div[@class="w"]/div/div[1]/div[2]')
        carName = detail.xpath('div[1]/h1/text()')[0].extract()
        item['original_id'] = response.meta['carId']
        for brand in brandList:
            if carName.count(brand) > 0:
                item['brand_name'] = brand
                carName = carName.replace(item['brand_name'], '')
        item['series_name'] = (carName.split())[0]
        item['model_name'] = carName
        guidance_price = detail.xpath('div[@class="basic-box"]/div[1]/span/text()')[0].extract()
        item['guidance_price'] = func.conversion_price(guidance_price)
        schemes = []
        first_price = func.conversion_price(detail.xpath('div[2]/div[2]/span/em/text()')[0].extract(), True)
        period = (detail.xpath('div[2]/div[3]/i/text()')[0].extract())[0:2]
        month_price = detail.xpath('div[2]/div[3]/span/em/text()')[0].extract()
        scheme = func.json_schemes(period, first_price, month_price)
        schemes.append(scheme)
        period = (detail.xpath('div[2]/div[4]/i/text()')[0].extract())[0:2]
        month_price = detail.xpath('div[2]/div[4]/span/em/text()')[0].extract()
        scheme = func.json_schemes(period, first_price, month_price)
        schemes.append(scheme)
        period = (detail.xpath('div[2]/div[5]/i/text()')[0].extract())[0:2]
        month_price = detail.xpath('div[2]/div[5]/span/em/text()')[0].extract()
        scheme = func.json_schemes(period, first_price, month_price)
        schemes.append(scheme)
        item['schemes'] = json.dumps(schemes)
        item['source_id'] = 25
        item['pickup_mode'] = '到店提车'
        yield item
