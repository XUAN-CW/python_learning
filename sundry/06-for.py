#测试for循环

for x in (10,20,30):
    print(x)
print("- - - - - - - - - - - - ")
for y in "abcdef":
    print(y)
print("########################")

d = {"name":"高淇","age":18,"job":"程序员"}
for x in d:
    print(x)
print("- - - - - - - - - - - - ")
for x in d.keys():
    print(x)
print("- - - - - - - - - - - - ")
for x in d.values():
    print(x)
print("- - - - - - - - - - - - ")
for x in d.items():
    print(x)
print("- - - - - - - - - - - - ")
for x in range(5):
    print(x)
print("########################")

sum_all = 0
sum_odd = 0  #100以内的奇数和
sum_even = 0  #100以内的偶数和
for x in range(101):
    sum_all += x
    if x%2==1:
        sum_odd += x
    else:
        sum_even += x

print("1-100累加总和{0},奇数和{1},偶数和{2}".format(sum_all,sum_odd,sum_even))

