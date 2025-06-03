import http.client
import gzip
import json
import pymysql
import time
import datetime
from urllib import parse
from commonBase.envData.envData_maimai100 import env_maimai
from commonBase.envData.envData_kuaileyouxuan import env_kuaile
from commonBase.envData.commonData import baseData


class comMethod():
    def __init__(self, env):
        if env == 'kuaileyouxuan':
            self.envData = env_kuaile
        else:
            self.envData = env_maimai
        self.envComData = baseData
        self.con = http.client.HTTPSConnection(self.envData.host.value)
        self.getHeaders()

    def getHeaders(self):
        tenantid = self.envData.tenantId.value
        authorization = self.envComData.authorization.value
        self.headers = {'Authorization': authorization,
                        'Content-Type': 'application/json',
                        'Accept': '*/*',
                        'Tenant-id': tenantid,
                        'accept-encoding': 'gzip, deflate, br, zstd',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}

    def sendRequests(self, method, api, body=None):
        if method == 'get':
            self.con.request('GET', api, headers=self.headers)
            res = gzip.decompress(self.con.getresponse().read()).decode()
        elif method == 'post':
            self.con.request('POST', api, headers=self.headers, body=json.dumps(body))
            res = gzip.decompress(self.con.getresponse().read()).decode()
        elif method == 'put':
            self.con.request('PUT', api, headers=self.headers, body=json.dumps(body))
            res = gzip.decompress(self.con.getresponse().read()).decode()
        elif method == 'delete':
            self.con.request('DELETE', api, headers=self.headers, body=json.dumps(body))
            res = gzip.decompress(self.con.getresponse().read()).decode()
        else:
            res = ''
        return res

    def compareResult(self, exceptInfo, resultInfo,comType):
        pass

    def conMysql(self):
        host = self.envData.mysqlHost.value
        port = int(self.envData.mysqlPort.value)
        username = self.envData.mysqlUser.value
        password = self.envData.mysqlPassword.value
        baseTable = self.envData.mysqlTable.value
        self.conSjk = pymysql.connect(host=host, port=port, user=username, password=password, database=baseTable,
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.conSjk.cursor()

    def operateMysql(self, sql, operateType=None):
        self.cur.execute(sql)
        if operateType:
            self.conSjk.commit()
            self.conSjk.close()
            res = '数据提交成功'
        else:
            res = self.cur.fetchall()
        return res

    def getTimeStamp(self, strTime):
        return int(time.mktime(time.strptime(strTime, "%Y-%m-%d %H:%M:%S")))

    def getFormatTime(self,timeStamp):
        return datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')

    def getAnyDay(self,numDay=0):
        return (datetime.datetime.now().date()-datetime.timedelta(numDay)).strftime('%Y%m%d')

    def getUrlQuote(self,strUrl):
        return parse.quote(strUrl)

if __name__ == '__main__':
    env = 'maimai100'
    demo = comMethod(env)
    demo.conMysql()
    sql = 'select * from infra_api_error_log where id =1'
    res = demo.operateMysql(sql)
    for i in res:
        print(i['exception_message'])
    demo.getHeaders()
    api = '/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10'
    res1 = demo.sendRequests('get', api)
    print(res1)

# baseUrl_maimai100='api-staging.maimai100.cn'
# # baseUrl_maimai100='syams-staging.maimai100.cn'
# baseUrl_kuaileyouxuan='https://staging-syams.kuaileyouxuan.com'
# authorization='902bd97aff8e47319cd7eef58ea23105'
# tenantid='166'
# head={'Authorization':authorization,
#       'Content-Type':'application/json',
#       'Accept':'*/*',
#       'Tenant-id':tenantid,
#       'accept-encoding':'gzip, deflate, br, zstd',
#       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
#
# api_store_create='/admin-api/trade/delivery/pick-up-store/create'
# api_store_page='/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10'
# body_store_create={
# 	"name": "门店统计003",
# 	"phone": "13525632563",
# 	"logo": "https://static.kuaileyouxuan.com/662a8885ee71c12aed3c10ce2afbcb48ddc6cf79c57d3d3a7a77e53665aaa1f1.png",
# 	"detailAddress": "撒旦萨芬123",
# 	"introduction": "",
# 	"areaId": 310104,
# 	"openingTime": "09:45",
# 	"closingTime": "14:30",
# 	"latitude": "2",
# 	"longitude": "1",
# 	"status": 0,
# 	"contact": "11"}
#
# url=baseUrl_maimai100+api_store_create
# url1=baseUrl_maimai100+api_store_page
# # for i in range(2,3):
# #     body_store_create['name']='门店统计00'+str(i)
# #     print(url)
# #     print(body_store_create)
# #     res=requests.post(url=url,json=api_store_create,headers=head)
# #     print(res.status_code)
# #     print(res.json())
# #     res=requests.post(url=url,json=api_store_create,headers=head)
#
# # res=requests.get(url,headers=head)
# con=http.client.HTTPSConnection(baseUrl_maimai100)
# # con.request('GET',api_store_page,headers=head)
# # res=con.getresponse().read()
# # res1=gzip.decompress(res)
# # print(res1)
# # print(res1.decode())
# con.request('POST',api_store_create,headers=head,body=json.dumps(body_store_create))
# res=con.getresponse().read()
# res1=gzip.decompress(res)
# print(res1)
# print(res1.decode())
# con.close()
