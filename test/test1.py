import requests
import time
import datetime
import asyncio
import aiohttp
from urllib import parse
from jsonpath import jsonpath
from commonBase.commonMethod import comMethod

# a=b'\x01'
# print(type(a))
# print(ord(a))

head={'Authorization': 'f59cae267e354c22ac29cd5e6deffac6',
                        'Content-Type': 'application/json',
                        'Accept': '*/*',
                        'Tenant-id': '166',
                        'accept-encoding': 'gzip, deflate, br, zstd',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
async def fetch_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=head) as response:
            return await response.text()

async def fetch_post(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data,headers=head) as response:
            return await response.json()

# 使用示例
async def main():
    url = "https://api-staging.maimai100.cn/admin-api/trade/delivery/pick-up-store/page?pageNo=1&pageSize=10"
    result = await fetch_get(url)
    print(result)

# async def main1():
#     url = "https://httpbin.org/post"
#     data = {"key": "value"}
#     result = await fetch_post(url, data)
#     print(result)

asyncio.run(main())
# asyncio.run(main1())

# com=comMethod()
# # print(com.getAnyDay(),type(com.getAnyDay()))
# # print(com.getTimeStamp('2025-06-05 14:13:14'),type(com.getTimeStamp('2025-06-05 14:13:14')))
# print(com.getFormatTime(1749744000),type(com.getFormatTime(1781193600)))
# print(com.getFormatTime(1749196346),type(com.getFormatTime(1781193600)))
# print(com.envComData.args)

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
                "id": 120,
                "createTime": 1749106126000,
                "name": "福利券",
                "status": 1,
                "validityStartTime": 1749052800000,
                "validityEndTime": 1780675200000
            },
            {
                "id": 119,
                "createTime": 1748072517000,
                "name": "失效福利券001",
                "status": 1,
                "validityStartTime": 1747929600000,
                "validityEndTime": 1748620800000
            },
            {
                "id": 118,
                "createTime": 1748066729000,
                "name": "核销002",
                "status": 1,
                "validityStartTime": 1747929600000,
                "validityEndTime": 1748275200000
            },
            {
                "id": 117,
                "createTime": 1747806864000,
                "name": "核销券001",
                "status": 1,
                "validityStartTime": 1747670400000,
                "validityEndTime": 1748361600000
            },
            {
                "id": 115,
                "createTime": 1746616163000,
                "name": "测试注册222",
                "status": 1,
                "validityStartTime": 1746028800000,
                "validityEndTime": 1748620800000
            },
            {
                "id": 114,
                "createTime": 1746615441000,
                "name": "测试注册券",
                "status": 1,
                "validityStartTime": 1746547200000,
                "validityEndTime": 1748620800000
            },
            {
                "id": 110,
                "createTime": 1745738100000,
                "name": "111",
                "status": 1,
                "validityStartTime": None,
                "validityEndTime": None
            },
            {
                "id": 109,
                "createTime": 1745547838000,
                "name": "时长券",
                "status": 1,
                "validityStartTime": 1743436800000,
                "validityEndTime": 1775232000000
            },
            {
                "id": 108,
                "createTime": 1745547838000,
                "name": "鞋子",
                "status": 1,
                "validityStartTime": 1743436800000,
                "validityEndTime": 1775232000000
            },
            {
                "id": 107,
                "createTime": 1745547818000,
                "name": "鸡蛋",
                "status": 1,
                "validityStartTime": 1743436800000,
                "validityEndTime": 1774972800000
            }
        ],
        "total": 11
    },
    "msg": ""
}
# b=jsonpath(a,f'$.data.list[?(@.id !={118})].id')
# print(b)
# print(comMethod('maimai100').compareResult(26,b,1))

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
formatTime=datetime.datetime.fromtimestamp(1749193601).strftime('%Y-%m-%d %H:%M:%S')
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