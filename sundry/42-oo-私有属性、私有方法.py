#测试私有属性、私有方法

class Employee:

    __company = "百战程序员"

    def __init__(self,name,age):
        self.name = name
        self.__age = age        #私有属性，在名字前加 __ 就是私有

    def __work(self):           #私有方法，在名字前加 __ 就是私有
        print("好好工作，赚钱娶媳妇！")
        print("年龄：{0}".format(self.__age))
        print(Employee.__company)



e = Employee("高淇",18)

print(e.name)
#print(e.__age)
print(e._Employee__age)#访问私有属性 _类名__属性名
print(dir(e))
e._Employee__work()
print(Employee._Employee__company)