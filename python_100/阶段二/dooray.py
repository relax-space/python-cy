# 爬取数据：爬取自己账号下的，dooray 担当业务箱的内容


# 明天继续修改

import requests

url = "https://pangpang.dooray.com/v2/wapi/projects/*/posts?order=-createdAt&page=0&projectScope=all&size=30&toMemberIds=2175283010926898096&userWorkflowClass=registered,working"

payload = {}
headers = {
  'Cookie': 'SCOUTER=x38mem9d076sod; SESSION=c6f5bd03-7780-4b64-ac0a-aff8fc59003e'
}

response = requests.request("GET", url, headers=headers, data = payload)

result = response.json()['result']['contents']
for subject in result:
    print(subject['subject'])
