#测试lambda表达式、匿名函数

#定义 lambda 表达式：lambda 参数1,参数2,参数3 ... :<表达式>
#运算结果为表达式的运算结果
f = lambda a,b,c,d:a*b*c*d
#等效与下面的函数 test01()
def test01(a,b,c,d):
    return a*b*c*d
print(f(2,3,4,5))
print(test01(2,3,4,5))

#函数也是对象，可以放在列表中
g = [lambda a:a*2,lambda b:b*3]
print(g[0](6))
h = [test01,test01]    #函数也是对象
print(h[0](3,4,5,6))

