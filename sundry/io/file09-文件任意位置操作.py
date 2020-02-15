with open("e.txt","r",encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())# f.tell() 返回文件指针的当前位置
    print("读取的内容：{0}".format(str(f.readline())))
    print(f.tell())
    '''
    seek(offset [,whence]) 
    把文件指针移动到新的位置， offset 表示相对于 whence 的多少个字节的偏移量；
    offset：
        off 为正往结束方向移动，为负往开始方向移动
    whence 不同的值代表不同含义：
        0: 从文件头开始计算（默认值）
        1：从当前位置开始计算
        2：从文件尾开始计算
    '''
    f.seek(0,0)
    print("读取的内容：{0}".format(str(f.readline())))