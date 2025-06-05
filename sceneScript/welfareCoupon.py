from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class welfareCoupon():
    def __init__(self,env):
        self.comMethod=comMethod(env)
        self.jsPath=jsonpath

    def creatCoupon(self):
        """
        新增福利券
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/welfare-coupon/create'
        dataDay_365 = self.comMethod.getAnyDay(365)
        logo = self.comMethod.envData.logoQc.value
        bodyInfo = {
                    "totalNum": 1000,
                    "status": 0,
                    "takeLimit": 20,
                    "couponTypeId": 118,
                    "couponTypeName": "核销002",
                    "validityTime": 1781193600000,
                    "couponTypeObj": "{\"id\":118,\"name\":\"核销002\"}",
                    "couponType": 0,
                    "activityId": "",
                    "grantEndTime": "2025-06-05T03:07:19.322Z",
                    "watchDuration": 1,
                    "activityName": ""
                    }
        bodyInfo1={
                  "totalNum": 1,
                  "status": 1,
                  "takeLimit": 1,
                  "couponTypeId": 120,
                  "couponTypeName": "福利券",
                  "validityTime": 1749744000000,
                  "couponTypeObj": "{\"id\":120,\"name\":\"福利券\"}",
                  "couponType": 1,
                  "activityId": "1834055349401705",
                  "grantEndTime": 1749196346000,
                  "watchDuration": 2,
                  "activityName": "希望123"
                }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def takeCoupon(self,couponId=30544):
        """
        领取福利券
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/app-api/product/user-coupon/take'
        nickname = self.comMethod.envComData.authorizationH5Name.value
        self.comMethod.getHeaders('h5')
        bodyInfo = {
            "couponId": couponId,
            "nickname": nickname,
        }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res