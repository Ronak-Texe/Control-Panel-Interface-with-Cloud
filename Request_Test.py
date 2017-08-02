import requests

a=str(['1','2','3'])


r=requests.post('http://127.0.0.1/upload',data=a)

print(r.status_code,r.reason)
