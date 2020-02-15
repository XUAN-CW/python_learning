#coding=utf-8
'''
程序开发中，有时候我们也需要自己定义异常类。
自定义异常类一般都是运行时异常，通常 继承 Exception 或其子类即可。
命名一般以 Error、Exception 为后缀。
自定义异常由 raise 语句主动抛出
'''

class AgeError(Exception):  #继承 Exception
    def __init__(self,errorInfo):#重写构造器，errorInfo 用来描述错误信息
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):#重写 __str__() ，把想提示的错误信息放到这里
        return str(self.errorInfo)+",年龄错误！应该在1-150之间"


############测试代码################
if __name__ == "__main__":   #如果为True，则模块是作为独立文件运行，可以执行测试代码
    age = int(input("输入一个年龄:"))
    if age<1 or age>150:
        raise AgeError(age)#自定义异常由 raise 语句主动抛出
    else:
        print("正常的年龄：",age)