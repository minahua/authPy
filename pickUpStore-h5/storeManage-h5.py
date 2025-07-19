# -*- coding: utf-8 -*-

import unittest
from commonBase.commonMethod import comMethod

class TestStoreFunc(unittest.TestCase):
    params = None

    @classmethod
    def setUpClass(cls):
        """
        测试执行前，数据准备
        :return:
        """
        if cls.params:
            cls.comMethod=comMethod(cls.params['env'])
        else:
            cls.comMethod = comMethod()

    @classmethod
    def tearDownClass(cls):
        print('end')

    def test_creatStore(self):
        """
        新增门店
        :return:
        """
        reqMethod='post'
        apiInfo='/admin-api/trade/delivery/pick-up-store/create'
        dataDay=self.comMethod.getAnyDay()
        logo=self.comMethod.envData.logoQc.value
        bodyInfo={
                    "name": "测试门店"+dataDay,
                    "phone": "135"+dataDay,
                    "logo": logo,
                    "detailAddress": "测试门店"+dataDay,
                    "introduction": "门店简介"+dataDay,
                    "areaId": 310104,
                    "openingTime": "09:45",
                    "closingTime": "14:30",
                    "latitude": "2",
                    "longitude": "1",
                    "status": 0,
                    "contact": "11"}
        res=self.comMethod.sendRequests(reqMethod,apiInfo,bodyInfo)
        self.assertEqual(res['status'],200)

    def test_getStore(self,StoreName='店铺001'):
        """
        查询门店
        :return:
        """
        reqMethod = 'get'
        storename=self.comMethod.getUrlQuote(StoreName)
        apiInfo = '/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10&status=0&phone=&name='+storename
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        self.assertEqual(res['status'],200)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([TestStoreFunc('test_getStore')])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)