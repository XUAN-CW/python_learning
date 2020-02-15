#coding=utf-8
'''
finally 块由于是否发生异常都会执行，通常我们放释放资源的代码。
其实，我们可以通 过 with 上下文管理，更方便的实现释放资源的操作。
with 上下文管理的语法结构如下：

with context_expr[as var]：
    语句块

context_expr 是一个表达式，返回的是一个对象，var用来保存context表达式返回的对象。
with 上下文管理可以自动管理资源，在 with 代码块执行完毕后自动还原进入该代码之前的现场或上下文。
不论何种原因跳出 with 块，不论是否有异常，总能保证资源正常释放,
极大的简化了工作，在文件操作、网络通信相关的场合非常常用
'''

with open("d:/a.txt","r") as f:
    content = f.readline()
    print(content)

print("程序执行结束！")