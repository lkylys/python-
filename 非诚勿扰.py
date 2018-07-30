n = 0
m = 0
man = []
woman = []
list = ["age" , "height" , "weight" , "money"]
ManLimit1 = [20 , 160 , 40 , 2000]
ManLimit2 = [28 , 175 , 60 , 5000]
WomanLimint1 = [25 , 170 , 60 , 5000]
WomanLimint2 = [35 , 180 , 80 , 10000]
print("请依次输入男生的年龄，身高，体重，收入")
for i in range(4) :
    a = int(input())
    man.append(a)
print("请依次输入男生的年龄，身高，体重，收入")
for j in range(4) :
    b = int(input())
    woman.append(b)
for i in range(4) :
    if woman[i] < ManLimit1[i] or woman[i] > ManLimit2[i] :
        print("女生不符合男生要求")
        break
    else :
        m += 1
        if m == 4 :
            print("女生符合男生要求")
for j in range(4) :
    if man[j] < WomanLimint1[j] or man[j] > WomanLimint2[j] :
        print("男生不符合女生要求")
        break
    else :
        n += 1
        if n == 4 :
            print("男生符合女生要求")
if m == 4 and n == 4 :
    print("配对成功")
else :
    print("配对不成功")