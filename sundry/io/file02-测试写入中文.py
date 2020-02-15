#测试写入中文
f = open(r"b.txt","w",encoding="utf-8")#若出现中文乱码，请使用 字符集 utf-8
f.write("尚学堂\n百战程序员\n")
f.close()