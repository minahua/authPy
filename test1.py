import requests
import time
import datetime
import asyncio
from urllib import parse

async def task1():
    print(datetime.datetime.now(),111)
    await asyncio.sleep(1)
    print(datetime.datetime.now(),112)
    return "任务1完成"

async def task2():
    print(datetime.datetime.now(),221)
    await asyncio.sleep(2)
    print(datetime.datetime.now(),222)
    return "任务2完成"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)  # ['任务1完成', '任务2完成']

asyncio.run(main())

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