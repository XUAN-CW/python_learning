#嵌套函数（内部函数）：在哪产生就在那里使用，就像函数内定义的局部变量一样

def outer():
    print("outer running")

    def inner01():
        print("inner01 running")

    inner01()

outer()

def printChineseName(name,familyName):
    print("{0} {1}".format(familyName,name))

def printEnglishName(name,familyName):
    print("{0} {1}".format(name, familyName))

def printName(isChinese,name,familyName):
    def inner_print(a,b):
        print("{0} {1}".format(a,b))

    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)

printName(True,"小七","高")
printName(False,"Ivanka","Trump")
