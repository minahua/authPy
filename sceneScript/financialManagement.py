from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class financialManagement():
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

    def separateOrderDetail(self):
        """
        新增福利券-注册券
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/separateAccount/separateOrderDetail'
        bodyInfo={'separateOrderId':'182'}
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res