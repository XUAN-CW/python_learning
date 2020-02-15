#测试类方法
class Student:
    company = "尚学堂"  # 类属性

    @classmethod#类方法用 @classmethod
    def printCompany(cls):#第一个参数必须写，一般为 cls ，有形参就放在后面
        print(id(cls))
        print(cls.company)


Student.printCompany()

print(id(Student))

