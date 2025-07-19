from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class tradeOrder():
    def __init__(self,env):
        self.comMethod=comMethod(env)
        self.jsPath=jsonpath

    def getOrderList(self):
        """
        查询订单列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/trade/order/page?pageNo=1&pageSize=10'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def getOrderDetail(self,orderId):
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
        :param orderItemId: 商户单号
        :param refundPrice:付款金额
        :return:
        """
        reqMethod = 'post'
        apiInfo = f'/admin-api/trade/after-sale/manageAfterSale'
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

    def createFlOrder(self,orderItemId):
        """
        福利商品兑换
        :return:
        """
        reqMethod = 'post'
        apiInfo = f'/app-api/trade/order/create'
        bodyInfo={
                "nonceStr": 1749695043818,
                "items": [
                    {
                        "skuId": 346,
                        "count": "20"
                    }
                ],
                "pickUpStoreId": 28,
                "deliveryType": 2,
                "pointStatus": False,
                "remark": ""
            }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def createScOrder(self,orderItemId):
        """
        福利商品兑换
        :return:
        """
        reqMethod = 'post'
        apiInfo = f'/app-api/trade/order/create'
        bodyInfo={
                "nonceStr": 1749695043818,
                "items": [
                    {
                        "skuId": 346,
                        "count": "20"
                    }
                ],
                "pickUpStoreId": 28,
                "deliveryType": 2,
                "pointStatus": False,
                "remark": ""
            }
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def writeOffOrder(self,orderIds):
        """
        核销订单
        :return:
        """
        reqMethod = 'post'
        apiInfo = f'/app-api/trade/order/writeOffOrder'
        bodyInfo={"orderIds":orderIds}
        res = self.comMethod.sendRequests(reqMethod, apiInfo,body=bodyInfo)
        return res

    def testAfterSale(self,orderId):
        resultsInfo = []
        res_getOrder=self.getOrderDetail(orderId)
        resultsInfo.append(res_getOrder)
        orderItemId=jsonpath(res_getOrder.get('result'),'$.data.id')
        refundPrice=jsonpath(res_getOrder.get('result'),'$.data.payPrice')
        res_afterSale=self.manageAfterSale(orderItemId,refundPrice)
        resultsInfo.append(res_afterSale)