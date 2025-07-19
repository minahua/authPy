import time
import asyncio
from sceneScript import pickUpStore
from sceneScript import welfareCoupon
from sceneScript import mallSaas
from sceneScript import tradeSale
from sceneScript import productSpu
from sceneScript import financialManagement

# env='lll'
env='kuaileyouxuan'
# env='preprod'
# env='maimai100'

# ten=productSpu.productSpu(env)
# res=ten.getCategory()
# res=ten.createCategory()
# res=ten.getBrand()
# res=ten.createBrand()
# res=ten.getProperty()
# res=ten.createProperty()
# res=ten.getSpu()
# for i in range(1,20):
#     supplierName=f'供应商{100+i}'
#     contacts=f'联系人{200+i}'
#     phone=f'135256325{10+i}'
#     name=f'关联商品{100+i}'
#     # res=ten.createSupplier(supplierName,contacts,phone)
#     res=ten.createSpu(name)
#     print(res)

# ten=pickUpStore.pickUpStore(env)
# for i in range(243,262):
#     # res=ten.createCompany(i+1)
#     res=ten.createSupplier(i+1)
#     res=ten.creatStore(i+1)
#     res=ten.deleteStore(i)
#     print(res)
# res=ten.getStore('测试门店')
# res=ten.syncDayStoreStatistics()
# res=ten.runStoreApi()
# res=ten.getOrderCount()
# print(res)

# ten=pickUpStore.companyManege(env)
# res=ten.updateCompany()
# res=ten.bindingCompany()
# res=ten.storeBindingCompany()
# print(res)

# ten=pickUpStore.bossManege(env)
# for i in range(10):
#     res=ten.createBoss(i+2)
#     print(res)
# res=ten.updateBoss()
# res=ten.getBossPage()
# res=ten.getBossDetails()
# res=ten.bindingBoss()
# res=ten.removeBoss()
# res=ten.getBossList()
# res=ten.subAccountPage()
# ten.comMethod.getHeaders('h5')
# res=ten.bossWithdrawal()
# res=ten.getBossAccount()
# res=ten.bindSubAccount()
# res=ten.storeBindingBoss()
# res=ten.resetMemberBossPassword()
# res=ten.setSubAccountPassword()
# res=ten.resetSubAccountPassword()
# print(res)

# ten=welfareCoupon.welfareCoupon(env)
# for i in range(90):
#     couid='30664'
#     res=ten.takeCoupon(couid)
#     print(res)
#     time.sleep(6)
# # res=ten.getCouponType()
# res=ten.getCouponPage()
# res=ten.exportCouponPage()

# ten=mallSaas.mallSaas(env)
# res=ten.getMall()
# print(res)

# ten=tradeSale.tradeOrder(env)
# # res=ten.getOrderList()
# sql="""select id,pay_price from trade_order_item where order_id in(select id from trade_order where user_id='10200'and type=0 and tenant_id=166 and status IN ('10', '30') and pay_price BETWEEN 1 and 500);"""
# # ten.testAfterSale(orderItemId)
# ten.comMethod.conMysql()
# res=ten.comMethod.operateMysql(sql)
# print(res)
# for infos in res:
#     orderItemId, refundPrice=infos['id'],infos['pay_price']
#     afterPrice=ten.manageAfterSale(orderItemId,refundPrice)
#     print(afterPrice)
# res=ten.manageAfterSale(171,100)
# orderids=["79532","79524"]
# res=ten.writeOffOrder(orderids)
# print(res)

# ten=financialManagement.financialManagement(env)
# res=ten.separateOrderDetail()
# print(res)