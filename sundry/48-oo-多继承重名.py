#测试mro()方法解析顺序
#多继承时父类中的属性或方法重名，继承者将会按“从左到右”的方式寻找，继承第一个出现的属性或方法
class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say AAA!")

class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB!")
class C(B,A):#B、A中都有方法 say() ,继承者应继承 B 中的 say()，因为 B 中的 say() 先出现
    def cc(self):
        print("cc")

c = C()
print(C.mro())          #打印类的层次结构
c.say()                 #解释器寻找方法是“从左到右”的方式寻找，此时会执行B类中的say()

