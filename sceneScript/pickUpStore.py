from jsonpath import jsonpath
from commonBase.commonMethod import comMethod


class pickUpStore():
    def __init__(self, env):
        self.comMethod = comMethod(env)
        self.jsPath = jsonpath

    def creatStore(self, num=0):
        """
        新增门店
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/trade/delivery/pick-up-store/create'
        dataDay = self.comMethod.getAnyDay()
        logo = self.comMethod.envData.logoQc.value
        name = f"新增可关联门店{dataDay}-{200 + num}"
        bodyInfo = {
            "name": name,
            "phone": "135" + dataDay,
            "logo": logo,
            "detailAddress": "测试门店" + dataDay,
            "introduction": "可删除数据",
            "areaId": 310104,
            "openingTime": "09:45",
            "closingTime": "14:30",
            "latitude": "2",
            "longitude": "1",
            "status": 0,
            "contact": "11"}
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def getStore(self, StoreName):
        """
        查询门店
        :return:
        """
        reqMethod = 'get'
        storename = self.comMethod.getUrlQuote(StoreName)
        apiInfo = '/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10&status=0&phone=&name=' + storename
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def getOrderCount(self):
        """
        查询门店
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/app-api/trade/order/get-order-count'
        body = {"pageNo": 1, "pageSize": 100}
        self.comMethod.getHeaders('h5')
        res = self.comMethod.sendRequests(reqMethod, apiInfo, body)
        return res

    def deleteStore(self, StoreId):
        """
        删除门店
        :return:
        """
        reqMethod = 'delete'
        apiInfo = f'/admin-api/trade/delivery/pick-up-store/delete?id={StoreId}'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def updateStore(self, StoreId):
        """
        更新门店
        :return:
        """
        reqMethod = 'put'
        apiInfo = f'/admin-api/trade/delivery/pick-up-store/update'
        dataDay = self.comMethod.getAnyDay()
        logo = self.comMethod.envData.logoQc.value
        body = {
            "name": "修改门店" + dataDay,
            "introduction": "门店简介" + dataDay,
            "phone": "135" + dataDay,
            "contact": "门店联系人" + dataDay,
            "areaId": 310104,
            "detailAddress": "修改门店" + dataDay,
            "logo": logo,
            "openingTime": "09:45",
            "closingTime": "14:30",
            "latitude": 2,
            "longitude": 1,
            "status": 0,
            "id": StoreId,
        }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, body)
        return res

    def syncDayStoreStatistics(self, num=0):
        """
        同步门店日报表数据
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/statistics/store/syncDayStoreStatistics'
        bodyInfo = {"startDate": "2025-07-16"}
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def createSupplier(self, num=0):
        """
        创建供应商
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/product/supplier/createSupplier'
        bh = '0' * (3 - len(str(num))) + f'{num}'
        bodyInfo = {"supplierName": "供应商0625" + bh,
                    "contacts": "联系人0625" + bh,
                    "phone": "18112341234",
                    "address": "12" + bh,
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def runStoreApi(self):
        """
        门店流程：新增、查询、修改、查询、删除、查询
        :return:
        """
        resultsInfo = []
        res_create = self.creatStore()
        resultsInfo.append(res_create)
        if res_create.get('status', 0) != 200:
            return resultsInfo
        storeId = res_create.get('result').get('data')
        storeName = "新增测试门店" + self.comMethod.getAnyDay()
        res_get = self.getStore(storeName)
        resultsInfo.append(res_get)
        if res_get.get('status', 0) != 200:
            return resultsInfo
        getStoreNames = jsonpath(res_get.get('result'), f'$.data.list[*].name')
        compareKey = self.comMethod.compareResult(storeName, getStoreNames, 1)
        if not compareKey:
            print('查询结果-新增，不正确')
        res_upStore = self.updateStore(storeId)
        resultsInfo.append(res_upStore)
        if res_upStore.get('status', 0) != 200:
            return resultsInfo
        newStoreName = "修改门店" + self.comMethod.getAnyDay()
        res_get1 = self.getStore(newStoreName)
        resultsInfo.append(res_get1)
        getStoreNames1 = jsonpath(res_get1.get('result'), f'$.data.list[?(@.id=={storeId})].name')
        compareKey = self.comMethod.compareResult(newStoreName, getStoreNames1, 1)
        if not compareKey:
            print('查询结果-修改，不正确')
        res_delete = self.deleteStore(storeId)
        resultsInfo.append(res_delete)
        sql = f'select * from trade_delivery_pick_up_store where id={storeId}'
        self.comMethod.conMysql()
        res_mysql = self.comMethod.operateMysql(sql)
        # print(res_mysql)
        compareKey = self.comMethod.compareResult(1, ord(res_mysql[0]['deleted']), 1)
        if not compareKey:
            print('查询结果-删除，不正确')
        return resultsInfo

class companyManege():
    def __init__(self, env):
        self.comMethod = comMethod(env)
        self.jsPath = jsonpath

    def createCompany(self, num=0):
        """
        创建分公司
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/company/createCompany'
        bh = '0' * (3 - len(str(num))) + f'{num}'
        bodyInfo = {"companyName": "分公司" + bh,
                    "principal": "负责人" + bh,
                    "phone": "18112341234",
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def getCompanyPage(self):
        """
        查询分公司
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/member/company/selectCompanyPage?pageNo=1&pageSize=10'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def updateCompany(self):
        """
        编辑分公司
        :return:
        """
        reqMethod = 'put'
        apiInfo = '/admin-api/member/company/updateCompany'
        bodyInfo = {
                      "id": 11,
                      "companyName": "分公司05",
                      "principal": "负责人0630",
                      "phone": "18112341234"
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def bindingCompany(self):
        """
        绑定分公司管理员
        :return:
        """
        reqMethod = 'put'
        apiInfo = '/admin-api/member/company/bindingCompany'
        bodyInfo = {
                      "companyId": 8,
                      "userId": "10200"
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def storeBindingCompany(self):
        """
        绑定门店
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/trade/delivery/pick-up-store/storeBindingCompany'
        bodyInfo = {
                      "companyId": 14,
                      "companyName": "分公司06",
                      "storeIds": [242,17]
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

class bossManege():
    def __init__(self, env):
        self.comMethod = comMethod(env)
        self.jsPath = jsonpath

    def createBoss(self, num=1):
        """
        创建老板
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/boss/create'
        bh = '0' * (3 - len(str(num))) + f'{num}'
        bodyInfo = {"bossName": "老板编号" + bh,
                    "bossWithdrawName": "提现户姓名" + bh,
                    "phone": "18112341234",
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def getBossPage(self):
        """
        查询boss列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/member/boss/page'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def getBossDetails(self):
        """
        获取boss详情
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/member/boss/getDetails?id=1&storeId=28'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def getBossList(self):
        """
        获取没有子账户的boss列表
        :return:
        """
        reqMethod = 'get'
        apiInfo = '/admin-api/member/boss/getBossList'
        res = self.comMethod.sendRequests(reqMethod, apiInfo)
        return res

    def updateBoss(self):
        """
        编辑boss信息
        :return:
        """
        reqMethod = 'put'
        apiInfo = '/admin-api/member/boss/update'
        bodyInfo = {
                      "id": 4,
                      "bossName": "老板05",
                      "bossWithdrawName": "老板0630",
                      "phone": "18112341234"
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def bindingBoss(self):
        """
        user绑定boss
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/boss/bindingBoss'
        bodyInfo = {
                      "bossId": 3,
                      "bossName": "分公司001",
                      "userId": "10151"
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def storeBindingBoss(self):
        """
        门店绑定boss
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/trade/delivery/pick-up-store/storeBindingBoss'
        bodyInfo = {
                      "bossId": 13,
                      "bossName": "分公司001",
                      "storeIds": [205,207]
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def removeBoss(self):
        """
        user解绑boss
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/boss/removeBindingBoss'
        bodyInfo = {
                      "bossId": 3,
                      "bossName": "分公司001",
                      "userId": "10151"
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def subAccountPage(self):
        """
        子账户管理分页查询
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/subAccount/page'
        bodyInfo = {
                      "pageNo": 1,
                      "pageSize": 10,
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def bindSubAccount(self):
        """
        解绑-绑定子账户
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/subAccount/bindSubAccount'
        bodyInfo = {
                      "subAccountId": 17,
                      "refAccountId": 14,
                      "useStatus": 0,
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def resetMemberBossPassword(self):
        """
        重置子账户密码
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/admin-api/member/boss/resetMemberBossPassword'
        bodyInfo = {
                      "bossId": 17,
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def setSubAccountPassword(self):
        """
        设置子账户密码
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/app-api/member/boss/setMemberBossPassword'
        bodyInfo = {
                      "bossId": 17,
                      "password": '111222',
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def bossWithdrawal(self):
        """
        老板提现
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/app-api/member/separateAccount/bossWithdrawal'
        bodyInfo = {
                      "bossId": '14',
                      "refSubAccountId": '17',
                      "accountWalletId": '7',
                      "password": '111222',
                      "withdrawAmt": '2',
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res

    def getBossAccount(self):
        """
        查询门店钱包
        :return:
        """
        reqMethod = 'post'
        apiInfo = '/app-api/member/account/getAccount'
        bodyInfo = {
                      "bossId": '14',
                      "accountWalletId": '250',
                    }
        res = self.comMethod.sendRequests(reqMethod, apiInfo, bodyInfo)
        return res