import unittest
from pickUpStore.storeManage import TestStoreFunc
from pickUpStore.userMange import TestUserFunc

def runTest(env,runType,testName=None,fileName=None):
    """
    执行测试集
    :param env: 执行环境
    :param runType: 执行方式 1：指定测试集的具体test 2、执行测试集所有的test
    :param testName: 具体testName
    :param fileName: 测试集名称
    :return:
    """
    for filename in fileName:
        filename.params = {"env": env}
        if runType==1:
            suite = unittest.TestSuite()
            suite.addTests([filename(testName)])
        else:
            loader=unittest.TestLoader()
            suite=loader.loadTestsFromTestCase(filename)
        unittest.TextTestRunner().run(suite)

# env='kuaileyouxuan'
# env='preprod'
env='maimai100'
fileName=[TestStoreFunc]
# fileName=[TestStoreFunc,TestUserFunc]
testName='test_getStore'
runType=1
runTest(env,runType,fileName=fileName,testName=testName)
