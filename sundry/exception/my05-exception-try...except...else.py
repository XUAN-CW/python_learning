#coding=utf-8
#测试try...except...else结构
'''
try...except...else 结构增加了“else 块”。
如果 try 块中没有抛出异常，则执行 else 块。
如果 try 块中抛出异常，则执行 except 块，不执行 else 块。
'''
try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
except BaseException as  e:
    print(e)
else:
    print(c)
print("程序结束！")