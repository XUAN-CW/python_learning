#测试循环中的else语句

salarySum= 0
salarys = []
for i in range(4):
    s = input("请输入一共4名员工的薪资（按Q或q中途结束）")

    if s.upper()=='Q':
        print("录入完成，退出")
        break
    if float(s)<0:
        continue

    salarys.append(float(s))
    salarySum += float(s)

else:#循环正常结束，else 执行，循环 break ,else 执行
    print("您已经全部录入4名员工的薪资")

print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/4))
