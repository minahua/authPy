from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class productSpu():
    def __init__(self,env):
        self.comMethod=comMethod(env)
        self.jsPath=jsonpath

    def getCategory(self):
        """
        查询商品分类
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/product/category/list'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def createCategory(self):
        """
        创建商品分类
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/category/create'
        picUrl=self.comMethod.envData.logoQc.value
        bodyInfo={
                "name": "水果",
                "picUrl": picUrl,
                "status": 0,
                "parentId": 0,
                "sort": 1
                }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def getBrand(self):
        """
        查询商品品牌
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/product/brand/page?pageNo=1&pageSize=10'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def createBrand(self):
        """
        创建商品品牌
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/brand/create'
        picUrl=self.comMethod.envData.logoQc.value
        bodyInfo={
                "name": "LVLV",
                "picUrl": picUrl,
                "status": 0,
                "description": 'test水果',
                "sort": 1
                }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def getProperty(self):
        """
        查询商品属性
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/product/property/page?pageNo=1&pageSize=10'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def createProperty(self):
        """
        创建商品属性
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/property/create'
        bodyInfo={
                "name": "LVLV",
                "remark": 'test水果',
                }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def getSpu(self):
        """
        查询商品列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/product/spu/page?pageNo=1&pageSize=10&tabType=1&name='
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def createSpu(self,name):
        """
        创建商品
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/spu/create'
        bodyInfo={
                "name": name,
                "categoryId": 111,
                "productType": 0,
                "keyword": name,
                "picUrl": "https://static.kuaileyouxuan.com/e0ae5b3134e480423d3e3801adc3f8f1e54f0594d0bf467fa516a6d6f8f426ed.png",
                "sliderPicUrls": [
                    "https://static.kuaileyouxuan.com/e0ae5b3134e480423d3e3801adc3f8f1e54f0594d0bf467fa516a6d6f8f426ed.png"
                ],
                "introduction": name,
                "deliveryTypes": [
                    2
                ],
                "brandId": 13,
                "specType": False,
                "subCommissionType": False,
                "skus": [
                    {
                        "price": 10,
                        "marketPrice": 10,
                        "costPrice": 10,
                        "barCode": "",
                        "picUrl": "https://static.kuaileyouxuan.com/ed725371c8a14c9c7ccb7161627d65f2b3bc7d15e6c4dfea6f7eedcc9073ea75.png",
                        "stock": 123,
                        "weight": 0.1,
                        "volume": 0.1,
                        "firstBrokeragePrice": 0,
                        "secondBrokeragePrice": 0,
                        "name": name
                    }
                ],
                "description": "<p>大声道</p>",
                "sort": 0,
                "giveIntegral": 0,
                "virtualSalesCount": 0,
                "refundDeadline": 1751212800000,
                "buyLimitNum": 0,
                "buyLimitTimes": 0,
                "userBuyLimit": "0,1,2,",
                "visibleType": "0",
                "storeScope": "",
                "status": 0,
                "couponQuantity": 1,
                "pointQuantity": 1
            }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def createSupplier(self,supplierName,contacts,phone):
        """
        创建供应商
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/supplier/createSupplier'
        bodyInfo={
                "supplierName": supplierName,
                "contacts": contacts,
                "phone": phone,
                "address": "111"
            }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res