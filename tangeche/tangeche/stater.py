#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy import cmdline
import os

# scrapy crawl itcast （itcast为爬虫名）
os.system("scrapy crawl tangeche")
# cmdline.execute("scrapy crawl tangeche".split())
