def Txtmoney ():
    km = int(input("Please enter your km :"))
    if km <= 0:
        print("请输入正确的公里数进行计算，程序结束")
    else :
        a = 8
        if km <= 2 :
            print("收费：%d" %a)
            Txtmoney()
        elif km <= 12 :
            b = a + (km - 2) * 1.2
            print("收费：%d" %b)
            Txtmoney()
        else :
            c = a + 12 + (km - 12) * 1.5
            print("收费：%d" %c)
            Txtmoney()
Txtmoney()