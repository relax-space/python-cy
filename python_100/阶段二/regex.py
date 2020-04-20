# 正则匹配：从这个地址中取出fruits,地址可能是 /v1/fruits?name=1，或者/v1/fruits/1,或者/v1/fruits
import re
regex = r'fruits'

addrs = ['/v1/fruits?name=1','/fruits/1','/v1/fruits']

for addr in addrs:
    res = re.findall(regex,addr)
    print(res)