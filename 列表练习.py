def students():
    print('--'*20)
    print('欢迎来到网络172班学生管理系统')
    print('1，查询学生信息')
    print('2，添加学生信息')
    print('3，删除学生信息')
    print('4，查询全体学生信息')
    print('5，退出学生管理系统')
    print('--'*20)
def Continue():
    print('1，查询学生信息')
    print('2，添加学生信息')
    print('3，删除学生信息')
    print('4，查询全体学生信息')
    print('5，退出学生管理系统')
    print('请继续您的操作：\n')
    change()
def change():
    n = int(input())
    if n == 1:
        name = input('请输入查询学生姓名：\n')
        stu = m[name]
        print(stu)
        print('\n')
        Continue()
    elif n == 2:
        print('请输入要添加学生信息：\n')
        add = input()
        addinformation = input()
        m[add] = addinformation
        print(m)
        print('\n')
        Continue()
    elif n == 3:
        print('请输入要删除学生姓名：\n')
        Yname = input()
        del m[Yname]
        print(m)
        Continue()
    elif n == 4:
        print(m)
        print('\n')
        Continue()
    elif n == 5:
        print('感谢您的使用，欢迎下次再见')
m = {}
students()
print('请输入您的选项:\n')
change()
