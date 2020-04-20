import json
fruitDictList = [{
    "name":"apple",
    "price":6.5,
},{
    "name":"pear",
    "price":3.6,
}]

class FruitDto:
    def __init__(self):
        self.name =""
        self.price=0.0

    @classmethod
    def toDict(self,obj):
        dict = obj.__dict__
        return dict

    @classmethod
    def fromDict(self,dict):
        obj = FruitDto()
        obj.__dict__.update(dict)
        return obj

print("dict 和 对象之间的转化：")
fruitStr = json.dumps(fruitDictList)
fruitDtoList = json.loads(fruitStr,object_hook=FruitDto.fromDict)
fruitDto = fruitDtoList[0]
print(f"fruitDto[0]===>type:{type(fruitDto)},value:{fruitDto.__dict__},name:{fruitDto.name}")

newFruitStr = json.dumps(fruitDtoList,default=FruitDto.toDict)
print(f"newFruitStr===>type:{type(newFruitStr)},value:{newFruitStr}")