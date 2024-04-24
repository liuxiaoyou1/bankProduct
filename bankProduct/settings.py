# -*- coding: utf-8 -*-


BOT_NAME = 'bankProduct'

SPIDER_MODULES = ['bankProduct.spiders']
NEWSPIDER_MODULE = 'bankProduct.spiders'



# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'bankProduct.pipelines.MongoPipeline': 300,
   'bankProduct.pipelines.FilePipeline': 500
}

#MONGO_URI = 'mongodb://192.168.0.235:30000'
WEBDRIVER_CHROME_PATH = '/opt/webdriver/chrome/chromedriver'
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'bank'
MONGO_COLLECTION = "bankProduct"  # collection名
SAVE_PATH = '/Users/liuxiaoshuai/Downloads/'