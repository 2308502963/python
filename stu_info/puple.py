# _*_ coding: utf-8 _*_
# @Time : 2019/11/21 14:49
# @Author : moran office
# File : puple.py
# Software : PyChram

import sys
# 录入用户的信息
def adduserinfo():
    info_list = []
    print("*"*50+"开始录入用户信息"+"*"*50)
    # 录入用户信息
    id = input("输入唯一标识符学号：")
    name = input("输入姓名：")
    chinese = input("输入语文:")
    math = input("输入数学:")
    english = input("输入英语:")
    user_info = {
        "id": id,
        "name": name,
        "chinese": chinese,
        "math": math,
        "english": english
    }
    info_list.append(user_info)
    saveuserinfo(info_list)
    print("*" * 150)
    print("*" * 150)
    print("保存成功!是否继续？".center(116, " "))
    choice = input("1继续录入小学生信息，0返回主页面".center(116, " "))
    if eval(choice) == 1:
        adduserinfo()
    elif eval(choice) == 0:
        menu()
    else:
        print("没工夫跟你耗，再见")
        sys.exit()
#显示所有用户信息
def findall():
    list = []     #用于存放返回的列表
    flag = 0
    with open("stu_info.txt", "r+", encoding="utf-8") as fp:
        try:
            while not flag:
                info_list = fp.readline()
                if info_list != "":
                    info_list = eval(info_list)
                    list.append(info_list)
                else:
                    flag = 1
        except Exception as e:
            print("findall()：读取时错误:", e)
    return list
def viewAll():
    list = findall()
    for name in["ID", "NAME", "CHINESE", "MATH", "ENGLISH"]:
        print(name, end="\t\t\t")
    print("")
    print("="*150)
    for x in range(len(list)):
        seconddict = list[x]
        for i in range(len(seconddict)):
            li = seconddict[i]
            print("%s\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s" % (li["id"]
                                              , li["name"]
                                              , li["chinese"]
                                              , li["math"]
                                              , li["english"]))
    menu()
# 搜索用户的信息
def searchuserinfo(id):
    list = findall()
    for firstlist in list:
        # firstlist:存储每一行数据的列表，其中可能还包括列表
        # seconddict:列表中的字典
        for seconddict in firstlist:
            if seconddict["id"] == id:
                print("为你找到%s的相关信息"%seconddict["name"])
                for name in ["ID", "NAME", "CHINESE", "MATH", "ENGLISH"]:
                    print(name, end="\t\t\t")
                print("")
                print("=" * 150)
                print("%s\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s" % (seconddict["id"]
                                                        , seconddict["name"]
                                                        , seconddict["chinese"]
                                                        , seconddict["math"]
                                                        , seconddict["english"]))
                print("=" * 150)
                print("你可以执行的操作有:")
                print("1.修改")
                print("2.删除")
                print("0.返回主页面")
                choice = input("请选择:")
                if eval(choice) == 0:
                    menu()
                elif eval(choice) == 1:
                    updateuserinfo(id)
                elif eval(choice) == 2:
                    deluserinfo(id)
                else:
                    print("大傻子，再见")
                    sys.exit()
    else:
        print("没有该小学生的信息")
        print("="*200)
        menu()
# 修改用户的信息
def updateuserinfo(id):
    list = findall()
    list1 = []
    for firstlist in list:
        # firstlist:存储每一行数据的列表，其中可能还包括列表
        # seconddict:列表中的字典
        for seconddict in firstlist:
            if seconddict["id"] == id:  # 找到相应的记录，修改
                seconddict["id"] = input("你要修改的学号：")
                seconddict["name"] = input("你要修改的姓名：")
                seconddict["chinese"] = input("你要修改的语文成绩：")
                seconddict["math"] = input("修改的数学成绩:")
                seconddict["english"] = input("修改的英语成绩:")
                list1.append(seconddict)
            else:
                list1.append(seconddict)
    saveuserinfo1(list1)
    viewAll()
# 删除用户的信息
def deluserinfo(id):
    list = findall()
    list1 = []
    for firstlist in list:
        # firstlist:存储每一行数据的列表，其中可能还包括列表
        # seconddict:列表中的字典
        for seconddict in firstlist:
            if seconddict["id"] != id:#找到相应的记录，删除
                list1.append(seconddict)
    saveuserinfo1(list1)
    viewAll()
#保存
def saveuserinfo1(text):
    text = str(text)
    try:
        # 保存数据到文件
        with open("stu_info.txt", 'w+', encoding="utf-8") as fp:
            fp.write(text)
            fp.write("\n")
    except Exception as e:
        print('保存失败', e)
# 用于保存用户的信息,基于文件的操作
def saveuserinfo(text):
    text = str(text)
    try:
        # 保存数据到文件
        with open("stu_info.txt", 'a+', encoding="utf-8") as fp:
            fp.write(text)
            fp.write("\n")
    except Exception as e:
        print('保存失败', e)
# 用户显示主页面
def menu():
    print("*"*50+"欢迎进入小学生成绩管理系统"+"*"*50)
    print("1:显示所有小学生信息".center(116, "*"))
    print("2:录入小学生信息".center(116, "*"))
    print("3:搜索小学生信息".center(116, "*"))
    print("0:退出系统".center(116, "*"))
    # 判断用户的选择，只有在0~4之间才通过
    user_choice = -1
    while user_choice < 0 or user_choice > 4:
        user_choice = eval(input("你的选择是:"))
    # 判断用户的选择
    if user_choice == 0:  # 选择的是0，退出系统（结束程序）
        print("期待您的再次使用")
        sys.exit()
    elif user_choice == 1:  # 选择的是1， 显示所有用户信息
        viewAll()
    elif user_choice == 2:  # 选择的是2，录入用户信息
        adduserinfo()
    elif user_choice == 3:  # 选择的是3，搜索用户的信息
        id = input("你要查询的小学生的学号是：")
        searchuserinfo(id)
if __name__ == '__main__':
    menu()
