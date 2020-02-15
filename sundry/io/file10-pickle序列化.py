'''
Python中，一切皆对象，对象本质上就是一个“存储数据的内存块”。有时候，我们
需要将“内存块的数据”保存到硬盘上，或者通过网络传输到其他的计算机上。这时候，就
需要“对象的序列化和反序列化”。 对象的序列化机制广泛的应用在分布式、并行系统上。
序列化指的是：将对象转化成“串行化”数据形式，存储到硬盘或通过网络传输到其他
地方。反序列化是指相反的过程，将读取到的“串行化数据”转化成对象。
我们可以使用 pickle 模块中的函数，实现序列化和反序列操作。

pickle.dump(obj, file) obj 就是要被序列化的对象，file 指的是存储的文件
pickle.load(file) 从file 读取数据，反序列化成对象

'''

import pickle

a1 = "高淇"
a2 = 234
a3 = [10,20,30,40]

#序列化
with open("data.dat","wb") as f:
    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)

#反序列化
with open("data.dat","rb") as f:
    b1 = pickle.load(f);
    b2 = pickle.load(f);
    b3 = pickle.load(f)
    print(b1);print(b2);print(b3)

    print(id(a1));print(id(b1))
