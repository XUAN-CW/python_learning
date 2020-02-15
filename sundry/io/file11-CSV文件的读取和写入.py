'''
csv(Comma Separated Values)是逗号分隔符文本格式，常用于数据交换、Excel
文件和数据库数据的导入和导出。与Excel 文件不同，CSV 文件中：
    值没有类型，所有值都是字符串
    不能指定字体颜色等样式
    不能指定单元格的宽高，不能合并单元格
    没有多个工作表
    不能嵌入图像图表
Python标准库的模块 csv提供了读取和写入 csv格式文件的对象。
'''
import csv

with open("dd.csv","r") as f:
    a_csv = csv.reader(f)
#    print(list(a_csv))
    for row in a_csv:
        print(row)

with open("ee.csv","w") as f:
    b_csv = csv.writer(f)
    b_csv.writerow(["ID","姓名","年龄"])
    b_csv.writerow(["1001","高淇","18"])
    c = [["1002","希希","3"],["1003","东东","4"]]
    b_csv.writerows(c)
