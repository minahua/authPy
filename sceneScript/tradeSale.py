from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class tradeOrder():
    def __init__(self,env):
        self.comMethod=comMethod(env)
        self.jsPath=jsonpath

    def getOderList(self):
        """
        查询订单列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/trade/order/page?pageNo=1&pageSize=10'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def getOderDetail(self,orderId):
        """
        查询订单列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = f'/admin-api/trade/order/get-detail?id={orderId}'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def manageAfterSale(self,orderItemId,refundPrice):
        """
        申请售后
        :return:
        """
        reqMethod = 'post'
        apiInfo = f'admin-api/trade/after-sale/manageAfterSale'
        bodyInfo={
                "orderItemId": orderItemId,
                "way": 10,
                "refundPrice": refundPrice,
                "applyReason": ""
                }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def pickUpOrder(self,orderItemId):
        """
        核销
        :return:
        """
        reqMethod = 'put'
        apiInfo = f'/admin-api/trade/order/pick-up-by-id?id={orderItemId}'
        bodyInfo={"id": orderItemId}
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res