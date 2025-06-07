from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

class mallSaas():
    def __init__(self,env):
        self.comMethod=comMethod(env)
        self.jsPath=jsonpath

    def getMall(self):
        """
        查询直播间列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/live/mall-saas/page?pageNo=1&pageSize=10&name=&status=&followerUserName='
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res