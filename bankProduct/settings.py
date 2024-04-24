# -*- coding: utf-8 -*-


BOT_NAME = 'bankProduct'

SPIDER_MODULES = ['bankProduct.spiders']
NEWSPIDER_MODULE = 'bankProduct.spiders'



# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'bankproduct.pipelines.MongoPipeline': 300,
   'bankproduct.pipelines.FilePipeline': 500
}

#MONGO_URI = 'mongodb://192.168.0.235:30000'
WEBDRIVER_CHROME_PATH = '/opt/webdriver/chrome/chromedriver'
MONGO_URI = 'mongodb://127.0.0.1:27017'
MONGO_DATABASE = 'bank'
MONGO_COLLECTION = "bankProduct"  # collection名
SAVE_PATH = '/tmp/file'