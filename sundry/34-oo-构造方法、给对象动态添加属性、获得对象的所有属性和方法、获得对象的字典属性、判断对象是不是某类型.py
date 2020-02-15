class Student:   #类名一般首字母大写，多个单词采用驼峰原则

    def __init__(self,name,score): #self必须位于第一个参数，这个地方是构造方法
        self.name = name#self 就像 Java 中的 this 
        self.score = score

    def say_score(self):   #self必须位于第一个参数
        print("{0}的分数是：{1}".format(self.name,self.score))



s1 = Student("高淇",18)   #通过类名()调用构造函数
s1.say_score()

#python 可以给对象动态添加属性
s1.age = 32
s1.salary = 3000
print(s1.salary)



s2 = Student("高希希",100)
s2.say_score()
Student.say_score(s2)

print(dir(s2))#获得对象的所有属性和方法

print(s2.__dict__)#获得对象的字典属性

class Man:
    pass

print(isinstance(s2,Man))#判断对象是不是某类型

