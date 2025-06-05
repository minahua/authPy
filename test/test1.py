import requests
import time
import datetime
import asyncio
from urllib import parse
from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

com=comMethod()
print(com.getAnyDay(),type(com.getAnyDay()))
print(com.getTimeStamp('2025-06-05 14:13:14'),type(com.getTimeStamp('2025-06-05 14:13:14')))
print(com.getFormatTime(1781193600),type(com.getFormatTime(1781193600)))

# def compareResult(exceptInfo, resultInfo, comType):
#     """
#     断言判断
#     :param exceptInfo: 预期值
#     :param resultInfo: 实际值
#     :param comType: 判断方式 1：预期值与实际值相同 2：预期值包含实际值 3：实际值包含预期值
#     :return:
#     """
#     print(locals())
#     if isinstance(resultInfo, list):
#         comparisonResults = True
#         for res in resultInfo:
#             comparisonResults &= compareResult(exceptInfo, res, comType)
#         return comparisonResults
#     if comType == 1:
#         return exceptInfo == resultInfo
#     elif comType == 2:
#         return resultInfo in exceptInfo
#     elif comType == 3:
#         return exceptInfo in resultInfo
a={
    "code": 0,
    "data": {
        "list": [
            {
                "name": "店铺001",
                "introduction": "dsad",
                "phone": "18125632563",
                "contact": "cm",
                "areaId": 510107,
                "detailAddress": "fff21434",
                "logo": "https://static.kuaileyouxuan.com/662a8885ee71c12aed3c10ce2afbcb48ddc6cf79c57d3d3a7a77e53665aaa1f1.png",
                "openingTime": "10:00",
                "closingTime": "15:30",
                "latitude": 2.0,
                "longitude": 32.0,
                "status": 0,
                "id": 28,
                "createTime": 1747722823000,
                "ifLock": 1,
                "userName": "一路有光",
                "userId": 10200,
                "memberCount": 5,
                "saleAmount": 15
            },
            {
                "name": "qbcs",
                "introduction": "",
                "phone": "17767563309",
                "contact": "1",
                "areaId": 150303,
                "detailAddress": "1",
                "logo": "https://static.kuaileyouxuan.com/693f66a4c2f20ec651cc637ed43960c1026f042706440f49ea03be5d7f798255.png",
                "openingTime": "08:30",
                "closingTime": "13:30",
                "latitude": 1.0,
                "longitude": 1.0,
                "status": 0,
                "id": 26,
                "createTime": 1747386241000,
                "ifLock": 0,
                "userName": None,
                "userId": None,
                "memberCount": 1,
                "saleAmount": 0
            },
            {
                "name": "AAA",
                "introduction": "",
                "phone": "19138809365",
                "contact": "11",
                "areaId": 110101,
                "detailAddress": "1",
                "logo": "https://lplb.oss-cn-chengdu.aliyuncs.com/b77920bdbc70c121c5447f0825b3851258f05685bec146e6c994d83179efcb92.jpeg",
                "openingTime": "08:30",
                "closingTime": "19:45",
                "latitude": 1.0,
                "longitude": 1.0,
                "status": 0,
                "id": 17,
                "createTime": 1746008737000,
                "ifLock": 1,
                "userName": "Tsuki",
                "userId": 10151,
                "memberCount": 5,
                "saleAmount": 101
            },
            {
                "name": "AAB测试门店",
                "introduction": "",
                "phone": "18900000000",
                "contact": "小张",
                "areaId": 110101,
                "detailAddress": "12",
                "logo": "https://lplb.oss-cn-chengdu.aliyuncs.com/3b41979098fdebb0644567a2b5b5c0598fd2f52dd106d93c5dc0bbe387df1df7.jpeg",
                "openingTime": "08:30",
                "closingTime": "21:00",
                "latitude": 0.0,
                "longitude": 0.0,
                "status": 0,
                "id": 13,
                "createTime": 1742555083000,
                "ifLock": 1,
                "userName": "臻选岛创始人-肖祥",
                "userId": 10208,
                "memberCount": 5,
                "saleAmount": 4
            },
            {
                "name": "AAA测试门店",
                "introduction": "",
                "phone": "18988888869",
                "contact": "小胡",
                "areaId": 510104,
                "detailAddress": "1",
                "logo": "https://lplb.oss-cn-chengdu.aliyuncs.com/ee2ee3debbd0a3edf24b4975d30e400a952bfaf00f8dc4ca2a73fe634ad0d261.png",
                "openingTime": "08:30",
                "closingTime": "23:30",
                "latitude": 0.0,
                "longitude": 0.0,
                "status": 0,
                "id": 12,
                "createTime": 1732632328000,
                "ifLock": 1,
                "userName": "拾-梦",
                "userId": 10106,
                "memberCount": 5,
                "saleAmount": 221
            }
        ],
        "total": 5
    },
    "msg": ""
}
b=jsonpath(a,f'$.data.list[?(@.id=={26})].id')
print(comMethod('maimai100').compareResult(26,b,1))

# async def task1():
#     print(datetime.datetime.now(),111)
#     await asyncio.sleep(1)
#     print(datetime.datetime.now(),112)
#     return "任务1完成"
#
# async def task2():
#     print(datetime.datetime.now(),221)
#     await asyncio.sleep(2)
#     print(datetime.datetime.now(),222)
#     return "任务2完成"
#
# async def main():
#     results = await asyncio.gather(task1(), task2())
#     print(results)  # ['任务1完成', '任务2完成']
#
# asyncio.run(main())

# a='%E9%97%A8%E5%BA%97%E7%BB%9F%E8%AE%A120250528'
# b='门店统计20250528'
# print(parse.unquote(a))
# print(parse.quote(b))

# def demo1():
#     a=1
#     b=2
#     c=datetime.datetime.now().date()
#     return locals()
# print(demo1())
#
# def demo2(*p1,**p2):
#     for i in p1:
#         print(i)
#     for j in p2:
#         print(j,p2[j])
#     print(123)
#
# a=(1,2,3)
# b={'a':4,'b':5}
# demo2(*a,**b)
# demo2()

# time_str = str(datetime.datetime.now().date())+" 18:00:00"
# timestamp = int(time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S")))*1000
# print(timestamp)
# print(datetime.datetime.now().date())
formatTime=datetime.datetime.fromtimestamp(1748615996).strftime('%Y-%m-%d %H:%M:%S')
print(formatTime)
# addDataday=datetime.datetime.now().date()-datetime.timedelta(-1)
# print(addDataday.strftime('%Y%m%d'))
# url='https://fund.eastmoney.com/217021.html?spm=search'
# res=requests.get(url)
# res.encoding='utf8'
# print(res.text)

# a=input()
# while a:
#     b=a.split()
#     print(f'"{b[0]}":"{b[-1]}",')
#     a=input()