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
                    "name": "新增测试门店"+dataDay,
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
        resultsInfo=[]
        res_create=self.creatStore()
        resultsInfo.append(res_create)
        if res_create.get('status',0)!=200:
            return resultsInfo
        storeId=res_create.get('result').get('data')
        storeName="新增测试门店"+self.comMethod.getAnyDay()
        res_get=self.getStore(storeName)
        resultsInfo.append(res_get)
        if res_get.get('status',0)!=200:
            return resultsInfo
        getStoreNames=jsonpath(res_get.get('result'),f'$.data.list[*].name')
        compareKey=self.comMethod.compareResult(storeName,getStoreNames,1)
        if not compareKey:
            print('查询结果-新增，不正确')
        res_upStore=self.updateStore(storeId)
        resultsInfo.append(res_upStore)
        if res_upStore.get('status',0)!=200:
            return resultsInfo
        newStoreName="修改门店"+self.comMethod.getAnyDay()
        res_get1 = self.getStore(newStoreName)
        resultsInfo.append(res_get1)
        getStoreNames1 = jsonpath(res_get1.get('result'), f'$.data.list[?(@.id=={storeId})].name')
        compareKey = self.comMethod.compareResult(newStoreName, getStoreNames1, 1)
        if not compareKey:
            print('查询结果-修改，不正确')
        res_delete=self.deleteStore(storeId)
        resultsInfo.append(res_delete)
        sql=f'select * from trade_delivery_pick_up_store where id={storeId}'
        self.comMethod.conMysql()
        res_mysql=self.comMethod.operateMysql(sql)
        # print(res_mysql)
        compareKey = self.comMethod.compareResult(1, ord(res_mysql[0]['deleted']), 1)
        if not compareKey:
            print('查询结果-删除，不正确')
        return resultsInfo

