from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class pickUpStore():
    def __init__(self,env):
        self.comMethod=comMethod(env)
        self.jsPath=jsonpath

    def creatStore(self):
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
        return res

    def getStore(self,StoreName):
        """
        查询门店
        :return:
        """
        reqMethod = 'get'
        storename=self.comMethod.getUrlQuote(StoreName)
        apiInfo = '/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10&status=0&phone=&name='+storename
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def deleteStore(self,StoreId):
        """
        删除门店
        :return:
        """
        reqMethod = 'delete'
        apiInfo = f'/admin-api/trade/delivery/pick-up-store/delete?id={StoreId}'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def updateStore(self,StoreId):
        """
        更新门店
        :return:
        """
        reqMethod = 'put'
        apiInfo = f'/admin-api/trade/delivery/pick-up-store/update'
        dataDay = self.comMethod.getAnyDay()
        logo = self.comMethod.envData.logoQc.value
        body={
                "name": "修改门店"+dataDay,
                "introduction": "门店简介"+dataDay,
                "phone": "135"+dataDay,
                "contact": "门店联系人"+dataDay,
                "areaId": 310104,
                "detailAddress": "修改门店"+dataDay,
                "logo": logo,
                "openingTime": "09:45",
                "closingTime": "14:30",
                "latitude": 2,
                "longitude": 1,
                "status": 0,
                "id": StoreId,
            }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body)
        return res

    def runStoreApi(self):
        """
        门店流程：新增、查询、修改、查询、删除、查询
        :return:
        """
        res_create=self.creatStore()
        StoreId=1
