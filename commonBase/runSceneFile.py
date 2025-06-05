import time
from sceneScript import pickUpStore
from sceneScript import welfareCoupon

# env='kuaileyouxuan'
# env='preprod'
env='maimai100'
# ten=pickUpStore.pickUpStore(env)
# res=ten.runStoreApi()
ten=welfareCoupon.welfareCoupon(env)
for i in range(10):
    res=ten.takeCoupon()
    print(res)
    time.sleep(4)
