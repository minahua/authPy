import http.client
import gzip
import requests
import json
import pymysql
import time
import datetime
from urllib import parse
from commonBase.envData.envData_maimai100 import env_maimai
from commonBase.envData.envData_kuaileyouxuan import env_kuaile
from commonBase.envData.envData_preprod import env_preprod
from commonBase.envData.commonData import baseData


class comMethod():
    def __init__(self, env=None):
        """
        根据使用环境，初始化数据
        :param env: 使用环境
        """
        if env == 'kuaileyouxuan':
            self.envData = env_kuaile
        elif env=='preprod':
            self.envData = env_preprod
        else:
            self.envData = env_maimai
        self.envComData = baseData
        # self.con = http.client.HTTPSConnection(self.envData.host.value)
        self.con = requests
        self.getHeaders()

    def getHeaders(self,loginId='manage'):
        """
        拼接请求头信息
        :return:
        """
        tenantid = self.envData.tenantId.value
        if loginId=='manage':
            authorization = self.envComData.authorization.value
        else:
            authorization = self.envComData.authorizationH5.value
        self.headers = {'Authorization': authorization,
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Tenant-id': tenantid,
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}

    def sendRequests1(self, method, api, body=None):
        """
        发送https请求：http.client请求
        :param method: 请求方法
        :param api: 请求地址
        :param body: 请求body
        :return: 请求结果
        """
        if method == 'get':
            self.con.request('GET', api, headers=self.headers)
        elif method == 'post':
            self.con.request('POST', api, headers=self.headers, body=json.dumps(body))
        elif method == 'put':
            self.con.request('PUT', api, headers=self.headers, body=json.dumps(body))
        elif method == 'delete':
            self.con.request('DELETE', api, headers=self.headers, body=json.dumps(body))
        else:
            return {'status':999,'msg':self.envComData.err_req.value}
        response=self.con.getresponse()
        # msg=response.read()
        # print(response.status,msg.decode('utf-8'))
        return {'status':response.status,
                'method':method,
                'api':api,
                'body':body,
                # 'result':json.loads(gzip.decompress(response.read()).decode())
                'result':response.read().decode()
                }

    def sendRequests(self, method, api, body=None):
        """
        发送https请求 request请求
        :param method: 请求方法
        :param api: 请求地址
        :param body: 请求body
        :return: 请求结果
        """
        url='https://'+self.envData.host.value+api
        if method == 'get':
            res=self.con.request('GET', url, headers=self.headers)
        elif method == 'post':
            res=self.con.request('POST', url, headers=self.headers, json=body)
        elif method == 'put':
            res=self.con.request('PUT', url, headers=self.headers, json=body)
        elif method == 'delete':
            res=self.con.request('DELETE', url, headers=self.headers, json=body)
        else:
            return {'status':999,'msg':self.envComData.err_req.value}
        # response=res.json()
        # print(res.status_code,api,body)
        return {'status':res.status_code,
                'method':method,
                'api':api,
                'body':body,
                'result':res.json()
                }

    def exportSend(self,method, api):
        """
        导出数据至Excel
        :param method:
        :param api:
        :return:
        """
        con = http.client.HTTPSConnection(self.envData.host.value)
        tenantid = self.envData.tenantId.value
        authorization = self.envComData.authorization.value
        headers = {'Authorization': authorization,
                   'Content-Type': 'text/html; charset=utf-8',
                   'Accept': 'application/json',
                   'Tenant-id': tenantid,
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
        con.request('GET', api, headers=headers)
        with open(r'D:\authPy\test\test.xlsx', 'wb') as f:
            f.write(con.getresponse().read())
        return '下载保存成功'

    def compareResult(self, exceptInfo, resultInfo,comType):
        """
        断言判断
        :param exceptInfo: 预期值
        :param resultInfo: 实际值
        :param comType: 判断方式 1：预期值与实际值相同 2：预期值包含实际值 3：实际值包含预期值
        :return:
        """
        if isinstance(resultInfo,list):
            comparisonResults=True
            for res in resultInfo:
                comparisonResults&=self.compareResult(exceptInfo,res,comType)
            return comparisonResults
        if comType==1:
            return exceptInfo==resultInfo
        elif comType==2:
            return resultInfo in exceptInfo
        elif comType==3:
            return exceptInfo in resultInfo
        else:
            return self.envComData.err_comTpye.value

    def conMysql(self):
        """
        连接mysql数据库
        :return:
        """
        host = self.envData.mysqlHost.value
        port = int(self.envData.mysqlPort.value)
        username = self.envData.mysqlUser.value
        password = self.envData.mysqlPassword.value
        baseTable = self.envData.mysqlTable.value
        self.conSjk = pymysql.connect(host=host, port=port, user=username, password=password, database=baseTable,
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.conSjk.cursor()

    def operateMysql(self, sql, operateType=None):
        """
        执行sql
        :param sql: sql语句
        :param operateType: 执行方式，默认查询
        :return:
        """
        self.cur.execute(sql)
        if operateType:
            self.conSjk.commit()
            self.conSjk.close()
            res = '数据提交成功'
        else:
            res = self.cur.fetchall()
        return res

    def getTimeStamp(self, strTime):
        """
        标准时间转化为时间戳
        :param strTime: 标准时间
        :return: 时间戳
        """
        return time.mktime(time.strptime(strTime, "%Y-%m-%d %H:%M:%S"))

    def getFormatTime(self,timeStamp):
        """
        时间戳转化为标准时间
        :param timeStamp: 时间戳
        :return: 标准时间
        """
        return datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')

    def getAnyDay(self,numDay=0):
        """
        获取当前时间之前之后时间，格式：%Y%m%d
        :param numDay: 之前几天使用负数，之后几天使用正数
        :return:
        """
        return (datetime.datetime.now().date()-datetime.timedelta(numDay)).strftime('%Y%m%d')

    def getUrlQuote(self,strUrl):
        """
        编码中文字符
        :param strUrl:
        :return:
        """
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
