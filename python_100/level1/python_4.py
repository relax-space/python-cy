# 问题4
# 定义一个至少具有两个方法的类：getString：从控制台输入获取字符串printString：以大写形式输出字符串。还请包括简单的测试功能来测试类方法。

class outputString():
    def __init__(self,str):
        self.str = str

    def getString(self):
        return self.str
    
    def printString(self):
        return self.str.upper()


string = input('input your str:')
foo = outputString(string)
result = foo.printString()
print(result)