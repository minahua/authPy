from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class welfareCoupon():
    def __init__(self,env):
        self.comMethod=comMethod(env)
        self.jsPath=jsonpath

    def getCouponType(self):
        """
        获取福利券类型
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/product/coupon-type/page?pageNo=1&pageSize=10'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def getCouponPage(self):
        """
        获取福利券列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/product/welfare-coupon/page?pageNo=1&pageSize=10'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def exportCouponPage(self):
        """
        导出福利券
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/product/welfare-coupon/export-excel?pageNo=1&pageSize=10'
        res = self.comMethod.exportSend(reqMethod, apiInfo)
        return res

    def creatLoginCoupon(self):
        """
        新增福利券-注册券
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/welfare-coupon/create'
        dataDay_365 = self.comMethod.getAnyDay(365)
        logo = self.comMethod.envData.logoQc.value
        bodyInfo={
                  "totalNum": 1,
                  "status": 1,
                  "takeLimit": 1,
                  "couponTypeId": 114,
                  "couponTypeName": "测试注册券",
                  "validityTime": 1750953600000,
                  "couponTypeObj": "{\"id\":114,\"name\":\"测试注册券\"}",
                  "couponType": 2,
                  "activityId": "",
                  "grantEndTime": "2025-06-05T09:11:09.463Z",
                  "watchDuration": 1,
                  "activityName": ""
                }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def creatComCoupon(self):
        """
        新增福利券-普通券
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
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def creatTimeCoupon(self):
        """
        新增福利券-时长券
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/welfare-coupon/create'
        dataDay_365 = self.comMethod.getAnyDay(365)
        logo = self.comMethod.envData.logoQc.value
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

    def takeCoupon(self,couponId=30547):
        """
        h5领取福利券
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