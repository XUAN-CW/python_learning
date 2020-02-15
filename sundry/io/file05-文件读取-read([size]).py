#测试文件读取
'''
文件的读取一般使用如下三个方法：
1. read([size])
从文件中读取 size 个字符，并作为结果返回。如果没有 size 参数，则读取整个文件。
读取到文件末尾，会返回空字符串。
2. readline()
读取一行内容作为结果返回。读取到文件末尾，会返回空字符串。
3. readlines()
文本文件中，每一行作为一个字符串存入列表中，返回该列表

'''
with open(r"e.txt","r",encoding="utf-8") as f:
    str = f.read(3)
    print(str)