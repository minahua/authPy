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

    def createSpu(self):
        """
        创建商品
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/spu/create'
        bodyInfo={
                "name": "LVLV",
                "remark": 'test水果',
                }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res