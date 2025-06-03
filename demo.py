import requests

url_base='https://staging-syapi.kuaileyouxuan.com/'
url_base1='http://api-staging.maimai100.cn/'
api='app-api/member/auth/login'
env='maimai100'
if env=='maimai100':
    head={'Tenant-id':'166'}
    body = {'mobile': '13100000000', 'password': '123456'}
    url=url_base1+api
else:
    head={'Tenant-id':'999170'}
    body={'mobile':'18811117359','password':'123456'}
    url=url_base+api
res=requests.post(url,headers=head,json=body)
print(res.status_code)
print(res.text)