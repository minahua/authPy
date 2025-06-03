from commonBase.commonMethod import comMethod

class pickUpStory():
    def __init__(self,env):
        self.comMethod=comMethod(env)

    def creatStory(self):
        reqMethod='post'
        apiInfo='/admin-api/trade/delivery/pick-up-store/create'
        dataDay=self.comMethod.getAnyDay()
        logo=self.comMethod.envData.logoQc.value
        bodyInfo={
                    "name": "测试门店"+dataDay,
                    "phone": "135"+dataDay,
                    "logo": logo,
                    "detailAddress": "测试门店"+dataDay,
                    "introduction": "",
                    "areaId": 310104,
                    "openingTime": "09:45",
                    "closingTime": "14:30",
                    "latitude": "2",
                    "longitude": "1",
                    "status": 0,
                    "contact": "11"}
        res=self.comMethod.sendRequests(reqMethod,apiInfo,bodyInfo)
        return res

    def getStory(self,stroyName):
        reqMethod = 'get'
        stroyname=self.comMethod.getUrlQuote(stroyName)
        apiInfo = '/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10&status=0&phone=&name='+stroyname
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def deleteStory(self,storyId):
        reqMethod = 'delete'
        apiInfo = f'/admin-api/trade/delivery/pick-up-store/delete?id={storyId}'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def updateStory(self,storyId):
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
                "id": storyId,
            }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body)
        return res