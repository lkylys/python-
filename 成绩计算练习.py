score = int(input("Please enter your score:"))

if score < 60 :
    print("不及格")
elif score >= 60 and score < 70 :
    print("等级是D")
elif score >= 70 and score < 80 :
    print("C")
elif score >= 80 and score < 90 :
    print("B")
elif score >= 90 and score <= 100 :
    print("A")