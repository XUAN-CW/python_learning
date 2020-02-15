#coding=utf-8
print("step0")
''' 异常的基本结构
try:
    被监控的可能引发异常的语句块
except BaseException [as e]:
    异常处理语句块
'''
try:
    print("step1")
    a = 3/0#在这里产生异常，跳过 step2
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
    print(type(e))
print("end!!!!")