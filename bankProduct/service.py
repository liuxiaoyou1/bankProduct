# -*- coding: utf-8 -*-
import gzip
import json

import requests
import logging
from bankProduct.util.dbhelper import MongodbBaseDao
from bankProduct.model.result import ProductDetailInfo
from bankProduct.model.result import ProductBaseInfo
from bankProduct.model.result import ProductMsg
from bankProduct.model.result import BPDataV1
from bankProduct.model.result import TaskResult

from bankProduct.settings import MONGO_URI
from bankProduct.settings import MONGO_DATABASE
from bankProduct.settings import MONGO_COLLECTION


class BankHttpService(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.result_post_url = 'https://rmb-stg.pingan.com.cn/brop/crawler/cust/spider/uploadCrawlerFlowling.do'
        self.file_post_url = 'https://rmb-stg.pingan.com.cn/brop/crawler/cust/spider/uploadCrawlingFile.do'
        self.dao = MongodbBaseDao(MONGO_URI, MONGO_DATABASE)

    def uploadResult(self, condition):
        productMsglist = list()
        # 查询数据
        for bankProductItem in list(self.dao.find(MONGO_COLLECTION, condition)):
            productBaseInfo = ProductBaseInfo(bankProductItem)
            productDetailInfo = ProductDetailInfo(bankProductItem)
            productMsg = ProductMsg(productBaseInfo, productDetailInfo)
            productMsglist.append(productMsg)
        data = BPDataV1(productMsglist)
        taskResult = TaskResult(data=data)
        headers = {"Content-Encoding": "gzip", 'Accept-encoding': 'gzip'}
        upload_data = json.dumps(taskResult.toKeyValue(), ensure_ascii=False)
        upload_data = upload_data.encode('utf-8')
        upload_data = gzip.compress(upload_data)
        # 获取请求数据
        resp = requests.post(self.result_post_url, headers=headers, data=upload_data, verify=False)
        self.logger.info(resp.text)

    # 文件上传
    def uploadFile(self, file_path, bucket_name):
        files = {"file": open(file_path, 'rb')}
        data = {"bucketName": bucket_name}
        resp = requests.post(self.file_post_url, data=data, files=files, verify=False)
        self.logger.info(resp.text)

    # 文件下载
    def downloadFile(self, download_url, file_path):
        resp = requests.get(download_url)
        with open(file_path, "wb") as f:
            f.write(resp.content)
        f.close()


if __name__ == '__main__':
    bank_http_service = BankHttpService()
    bank_http_service.uploadResult({'bankCode': 'czb'})

    pass