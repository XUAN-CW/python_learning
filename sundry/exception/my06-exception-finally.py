#coding=utf-8
#测试try...except...else...finally结构
'''
try...except...finally 结构中，finally 块无论是否发生异常都会被执行；
通常用来释放 try 块中 申请的资源。
'''
try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
except BaseException as  e:
    print(e)
else:
    print(c)
finally:
    print("我是finally中的语句，无论发生异常与否，都执行！")
print("程序结束！")