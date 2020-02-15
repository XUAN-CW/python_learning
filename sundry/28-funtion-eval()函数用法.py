# eval() 函数可以执行传递给它的语句，使代码更加灵活

s = "print('abcde')"
eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

dict1 = dict(a=100,b=200)

#eval() 传参
d = eval("a+b")
print(d)
e = eval("a+b",dict1)
print(e)

