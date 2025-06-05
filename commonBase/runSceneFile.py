from sceneScript import pickUpStore
from sceneScript import welfareCoupon

# env='kuaileyouxuan'
# env='preprod'
env='maimai100'
# ten=pickUpStore.pickUpStore(env)
# res=ten.runStoreApi()
ten=welfareCoupon.welfareCoupon(env)
res=ten.takeCoupon()
print(res)
