#测试while循环

num = 0
while num<=10:
    print(num,end="\t")
    num += 1
print("**********************************")

#计算1-100之间数字的累加和
num2 = 0
sum_all = 0

while num2<=100:
    sum_all = sum_all + num2
    num2 +=1
print("1-100所有书的累加和：",sum_all)
print("**********************************")

while num>0:
    print(num)
    num -=1
