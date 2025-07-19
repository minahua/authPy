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
from commonBase.envData.envData_lll import env_lll
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
        elif env=='lll':
            self.envData=env_lll
        else:
            self.envData = env_kuaile
        self.envComData = baseData
        # self.con = http.client.HTTPSConnection(self.envData.host.value)
        # self.con = requests
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

    def sendRequests(self, method, api, body=None):
        """
        发送https请求：http.client请求
        :param method: 请求方法
        :param api: 请求地址
        :param body: 请求body
        :return: 请求结果
        """
        self.con = http.client.HTTPSConnection(self.envData.host.value)
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
                'result':self.getResultFormatTime(json.loads(response.read().decode()))
                }

    def sendRequests1(self, method, api, body=None):
        """
        发送https请求 request请求
        :param method: 请求方法
        :param api: 请求地址
        :param body: 请求body
        :return: 请求结果
        """
        self.con = requests
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
        print(res.status_code,api,body)
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

    def getResultFormatTime(self,results):
        for res in results:
            if isinstance(results[res],dict):
                res1=self.getResultFormatTime(results[res])
                results[res]=res1
            elif isinstance(results[res],int) and 'time' in res.lower():
                trsTime=int(str(results[res])[:10])
                results[res]=datetime.datetime.fromtimestamp(trsTime).strftime('%Y-%m-%d %H:%M:%S')
        return results

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
            # self.conSjk.close()
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
    import json
    env = 'maimai100'
    demo = comMethod(env)
    demo.conMysql()

    # 批量插入福利券领取数据
    # sql1=f"INSERT INTO `product_user_coupon` ( `creator`, `create_time`, `updater`, `update_time`, `deleted`, `tenant_id`, `user_id`, `user_name`, `coupon_id`, `coupon_type_id`, `coupon_type_name`, `num`, `status`, `validity_time`, `store_id`) VALUES"
    sql1=f"INSERT INTO `live-mall-test`.`product_user_coupon` ( `creator`, `create_time`, `updater`, `update_time`, `deleted`, `tenant_id`, `user_id`, `user_name`, `coupon_id`, `coupon_type_id`, `coupon_type_name`, `num`, `status`, `validity_time`, `use_time`, `verify_user_id`, `verify_user_name`, `merge_flag`, `commodity_id`, `commodity_name`, `store_id`) VALUES"
    # sql1=f"INSERT INTO `live-mall-test`.`product_user_coupon` (`creator`, `create_time`, `updater`, `update_time`, `deleted`, `tenant_id`, `user_id`, `user_name`, `coupon_id`, `coupon_type_id`, `coupon_type_name`, `num`, `status`, `validity_time`, `store_id`) VALUES ( '10200', '2025-06-14 11:25:39', '10200', '2025-06-18 11:03:24', b'0', 166, 10200, 'hh123', 30578, 119, '失效福利券001', 1, -1, '2025-06-14 00:00:00', 28)"
    for i in range(2,168):
        dataYMD = (datetime.datetime.now().date() - datetime.timedelta(i)).strftime('%Y-%m-%d')
        for j in range(10):
            for z in range(11,60,3):
                # sql1+=f"( '10200', '{dataYMD} 1{j}:{z}:{z+3}', '10200', '{dataYMD} 1{j}:{z}:{z+3}', b'0', 166, 10200, '岁月静好', 30553, 107, '鸡蛋', 1, 0, '2025-06-28 00:00:00', 28),"
                sql1+=f" ( '10200', '{dataYMD} 1{j}:{z}:{z-1}', '10200', '{dataYMD} 1{j}:{z}:{z}', b'0', 166, 10106, '拾-梦', 30527, 118, '核销002', 1, 1, '2025-06-28 00:00:00', '{dataYMD} 1{j}:{z}:{z}', 10200, '岁月静好', NULL, NULL, '其他商品', 28),"
                # sql1+=f"( '10200', '{dataYMD} 1{j}:{z}:{z+3}', '10200', '{dataYMD} 1{j}:{z}:{z+3}', b'0', 166, 10200, '岁月静好', 30553, 107, '鸡蛋', 1, 0, '2025-06-28 00:00:00', 28),"
    res1=demo.operateMysql(sql1[:-1],operateType=1)
    print(res1)

    # 批量插入直播统计数据
    # sql1=f"INSERT INTO `live-mall-test`.`live_user_behavior` (`tenant_id`, `activity_id`, `store_id`, `user_id`, `watch_duration`, `watch_time`, `creator`, `create_time`, `updater`, `update_time`, `deleted`) VALUES "
    # for i in range(1,9):
    #     for j in range(3):
    #         da=f'2025-02-{j}{i} '
    #         titi=demo.getTimeStamp(da+'21:00:11')
    #         sql1+=f"(166, '1834221637925018', 28, 10200, 15, {titi}, NULL, '{da} 12:00:04', NULL, '{da} 12:00:04', b'0'),"
    # res1=demo.operateMysql(sql1[:-1],operateType=1)
    # print(res1)

    # 批量插入订单、订单明细数据
    # sql1=f"select max(id) from trade_order"
    # sql2=f"select max(id) from trade_order_item"
    # res1=demo.operateMysql(sql1)
    # print(res1)
    # orderId=int(res1[0]['max(id)'])+1
    # res2=demo.operateMysql(sql2)
    # print(res2)
    # itemId=int(res2[0]['max(id)'])+1
    # for i in range(10):
    #     sql3=f"INSERT INTO `live-mall-test`.`trade_order_item` (`id`, `user_id`, `order_id`, `cart_id`, `spu_id`, `spu_name`, `sku_id`, `properties`, `pic_url`, `count`, `comment_status`, `price`, `discount_price`, `delivery_price`, `adjust_price`, `pay_price`, `coupon_price`, `point_price`, `use_point`, `give_point`, `vip_price`, `after_sale_id`, `after_sale_status`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `tenant_id`, `store_id`, `commission_sharing_ratio`, `coupon_type_id`, `coupon_type_name`, `coupon_quantity`) VALUES "
    #     sql4 = f"INSERT INTO `live-mall-test`.`trade_order` (`id`, `no`, `type`, `terminal`, `user_id`, `user_ip`, `user_remark`, `status`, `product_count`, `cancel_type`, `remark`, `comment_status`, `brokerage_user_id`, `pay_order_id`, `pay_status`, `pay_time`, `pay_channel_code`, `finish_time`, `cancel_time`, `total_price`, `discount_price`, `delivery_price`, `adjust_price`, `pay_price`, `delivery_type`, `logistics_id`, `logistics_no`, `delivery_time`, `receive_time`, `receiver_name`, `receiver_mobile`, `receiver_area_id`, `receiver_detail_address`, `pick_up_store_id`, `pick_up_verify_code`, `refund_status`, `refund_price`, `coupon_id`, `coupon_price`, `use_point`, `point_price`, `give_point`, `refund_point`, `vip_price`, `seckill_activity_id`, `bargain_activity_id`, `bargain_record_id`, `combination_activity_id`, `combination_head_id`, `combination_record_id`, `creator`, `create_time`, `create_day`, `updater`, `update_time`, `deleted`, `tenant_id`, `store_id`, `activity_id`, `if_write_off`, `write_user_id`, `write_user_name`, `write_time`, `history_store_id`, `cancel_user_id`, `cancel_user_name`, `sl_trade_id`, `refund_deadline`, `commission_sharing_ratio`) VALUES "
    #     for j in range(1000):
    #         orderId1=orderId+i*1000+j
    #         itemId1=itemId+i*1000+j
    #         nums=(i+1)*10000+j
    #         sql4+=f"({orderId1}, 'o20250601{nums}12', 0, 0, 10223, '118.112.58.6', '', 10, 1, NULL, NULL, b'0', NULL, 487, b'1', '2025-05-03 14:02:55', 'huifu_wx_pub', NULL, NULL, 1, 0, 0, 0, 1, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, '53532257', 0, 0, NULL, 0, 0, 0, 2, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, '10049', '2025-05-03 15:32:11', 20250603, NULL, '2025-05-03 19:18:05', b'0', 171, 2, '0', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),"
    #         sql3+=f"({itemId1}, 10223, {orderId1}, NULL, 703, 'test3', 165, '"+json.dumps([{"valueId": 0, "valueName": "123", "propertyId": 0, "propertyName": "默认"}])+"', 'https://lplb.oss-cn-chengdu.aliyuncs.com/54b12463ca145ca1236366881aa1e03147b7039e50800fc76cd5b929e930b981.jpg', 1, b'0', 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, NULL, 0, '10106', '2025-05-03 15:32:11', '10106', '2025-05-03 19:18:25', b'0', 171, 12, NULL, '', '', 0),"
    #     print(sql3[:-1])
    #     print(sql4[:-1])
    #     res3=demo.operateMysql(sql3[:-1],operateType=1)
    #     print(res3)
    #     res4=demo.operateMysql(sql4[:-1],operateType=1)
    #     print(res4)

    # 单条插入订单、订单明细数据
    # orderId=19233
    # itemId=19251
    # for i in range(1,50000):
    #     orderId1=orderId+i
    #     itemId1=itemId+i
    #     nums=10000+i
    #     try:
    #         sql1=f"INSERT INTO `live-mall-test`.`trade_order_item` (`id`, `user_id`, `order_id`, `cart_id`, `spu_id`, `spu_name`, `sku_id`, `properties`, `pic_url`, `count`, `comment_status`, `price`, `discount_price`, `delivery_price`, `adjust_price`, `pay_price`, `coupon_price`, `point_price`, `use_point`, `give_point`, `vip_price`, `after_sale_id`, `after_sale_status`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `tenant_id`, `store_id`, `commission_sharing_ratio`, `coupon_type_id`, `coupon_type_name`, `coupon_quantity`) VALUES ({itemId1}, 10223, {orderId1}, NULL, 703, 'test3', 165, '"+json.dumps([{"valueId": 0, "valueName": "123", "propertyId": 0, "propertyName": "默认"}])+"', 'https://lplb.oss-cn-chengdu.aliyuncs.com/54b12463ca145ca1236366881aa1e03147b7039e50800fc76cd5b929e930b981.jpg', 1, b'0', 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, NULL, 0, '10106', '2025-06-03 15:32:11', '10106', '2025-06-03 19:18:25', b'0', 171, 12, NULL, '', '', 0);"
    #         print(sql1)
    #         sql2 = f"INSERT INTO `live-mall-test`.`trade_order` (`id`, `no`, `type`, `terminal`, `user_id`, `user_ip`, `user_remark`, `status`, `product_count`, `cancel_type`, `remark`, `comment_status`, `brokerage_user_id`, `pay_order_id`, `pay_status`, `pay_time`, `pay_channel_code`, `finish_time`, `cancel_time`, `total_price`, `discount_price`, `delivery_price`, `adjust_price`, `pay_price`, `delivery_type`, `logistics_id`, `logistics_no`, `delivery_time`, `receive_time`, `receiver_name`, `receiver_mobile`, `receiver_area_id`, `receiver_detail_address`, `pick_up_store_id`, `pick_up_verify_code`, `refund_status`, `refund_price`, `coupon_id`, `coupon_price`, `use_point`, `point_price`, `give_point`, `refund_point`, `vip_price`, `seckill_activity_id`, `bargain_activity_id`, `bargain_record_id`, `combination_activity_id`, `combination_head_id`, `combination_record_id`, `creator`, `create_time`, `create_day`, `updater`, `update_time`, `deleted`, `tenant_id`, `store_id`, `activity_id`, `if_write_off`, `write_user_id`, `write_user_name`, `write_time`, `history_store_id`, `cancel_user_id`, `cancel_user_name`, `sl_trade_id`, `refund_deadline`, `commission_sharing_ratio`) VALUES ({orderId1}, 'o20250901{nums}12', 0, 0, 10223, '118.112.58.6', '', 10, 1, NULL, NULL, b'0', NULL, 487, b'1', '2025-06-03 14:02:55', 'huifu_wx_pub', NULL, NULL, 1, 0, 0, 0, 1, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, '53532257', 0, 0, NULL, 0, 0, 0, 2, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, '10049', '2025-06-13 15:32:11', 20250603, NULL, '2025-06-03 19:18:05', b'0', 171, 2, '0', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"
    #         print(sql2)
    #         res = demo.operateMysql(sql1,operateType=1)
    #         print(res)
    #         res1 = demo.operateMysql(sql2,operateType=1)
    #         print(res1)
    #     except Exception as e:
    #         print(e)

    # demo.getHeaders()
    # api = '/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10'
    # res1 = demo.sendRequests('get', api)
    # print(res1)

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
