import time
import asyncio
from sceneScript import pickUpStore
from sceneScript import welfareCoupon
from sceneScript import mallSaas
from sceneScript import tradeSale
from sceneScript import productSpu

# env='kuaileyouxuan'
# env='preprod'
env='maimai100'

ten=productSpu.productSpu(env)
res=ten.getCategory()
# res=ten.createCategory()
# res=ten.getBrand()
# res=ten.createBrand()
# res=ten.getProperty()
# res=ten.createProperty()
# res=ten.getSpu()
print(res)

# ten=pickUpStore.pickUpStore(env)
# for i in range(1,110):
#     res=ten.creatStore(i+1)
#     print(res)
# res=ten.getStore('测试门店')
# res=ten.runStoreApi()

# ten=welfareCoupon.welfareCoupon(env)
# for i in range(20):
#     # for j in ('30547','30551','30550'):
#     # couid='30547'
#     couid='1209'
#     # couid='30553'
#     # couid='30552'
#     res=ten.takeCoupon(couid)
#     print(res)
#     time.sleep(6)
# res=ten.getCouponType()
# res=ten.getCouponPage()
# res=ten.exportCouponPage()

# ten=mallSaas.mallSaas(env)
# res=ten.getMall()
# print(res)

# ten=tradeSale.tradeOrder(env)
# # res=ten.getOrderList()
# sql="select id,pay_price from trade_order where user_id='10200' and status IN ('10', '30') and pay_price BETWEEN 5 and 500"
# # ten.testAfterSale(orderItemId)
# ten.comMethod.conMysql()
# res=ten.comMethod.operateMysql(sql)
# print(res)
# for infos in res:
#     orderItemId, refundPrice=infos['id'],infos['pay_price']
#     afterPrice=ten.manageAfterSale(orderItemId,refundPrice)
#     print(afterPrice)