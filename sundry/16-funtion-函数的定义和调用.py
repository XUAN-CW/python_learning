#测试函数的定义和调用

#定义 
def  test01():
    print("*"*10)
    print("@"*10)


print(id(test01))#函数也有id
print(type(test01))#类型为 function
print(test01)#打印函数地址


#调用
for i in range(10):
    test01()
