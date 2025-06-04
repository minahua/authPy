from sceneScript import pickUpStore

# env='kuaileyouxuan'
# env='preprod'
env='maimai100'
ten=pickUpStore.pickUpStore(env)
# res=ten.creatStore()
res=ten.getStore('AAA')
# res=ten.deleteStore(49)
# res=ten.updateStore(31)
print(res)
