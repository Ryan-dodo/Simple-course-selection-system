# -*- coding: utf-8 -*-
# @Time    : 2021/12/22
# @File    : run.py
# @Software: Geany
# @Author：Ryan

import sqlite3
# python自带的数据库


# 创建 类 课程
class Course():
    
    def __init__(self,courseName,description,learningTime):
        self.courseName = courseName
        self.description = description
        self.learningTime = learningTime
    
    def addCourse(self):
        pass

# 创建 类 人员
class Staff():
    
    def __init__(self,name,age,gender,idcard,address,tel):
        self.name = name 
        self.age = age 
        self.gender = gender 
        self.idcard = idcard
        self.address = address 
        self.tel = tel
        
# 创建 类 课程详细内容
class openCourse():
    
    def __init__(self,teachingDate,teachingTime,position):
        self.teachingDate = teachingDate
        self.teachingTime = teachingTime
        self.position = position
    
    def addStudent(self):
        pass
        
    def setTeacher(self):
        pass
        
    def isFullStudent(self):
        pass
        
# 创建 类 学生登录        
class StudentRegister():
    
    def __init__(self,semester,courseName):
        self.semester = semester
        self.courseName = courseName
    
    def choseCoure():
        pass
        
    def printCourse():
        pass
    
# 创建 类 课程注册    
class CourseRegister():
 
    def __init__(self,semester,studentName):
        self.semester = semester
        self.studentName = studentName  
    
    def addStudent():
        pass
    
    def printCourse():
        pass
        
        
class CourseCount():
    
    def __init__(self,semester):
        self.semester = semester 
        
    def countByCourse(self):
        pass
        
    def countByStudent(self):
        pass
    
    def printall(self):
        pass

# 管理员登录入口函数
def adminLogin():
    # 功能选择界面
    while True:
        print("---------------------------------------------")
        print()
        print('Hello admin!')
        print('What do you want to do ?')
        print()
        print('1------show all course')
        print('展示所有课程（简略版）')
        print()
        print('2------show all openCourse in detail')
        print('展示所有课程（有具体的学生信息）')
        print()
        print('3------show all  users')
        print('展示所有师生名单')
        print()
        print('4------show course by select a student')
        print('搜索某个学生的选课')
        print()
        print('5------show course by select a course')
        print('展示某个课程的选课情况')
        print()
        print('else------Get back')
        print('返回主界面')
    
        i2 = input('Please press a number, and enter')   
        if i2 == '2':
            print("---------------------------------------------")
            print()
            print('There are all openCourse')
            for row in cur.execute('SELECT * FROM openCourses '):
                print(row)            
            
                
        elif i2 == '1':
            print("---------------------------------------------")
            print()     
            print('courseName  description  learningTime teacherName teachingDate  teachingTime  position ')
            for row in cur.execute('SELECT * FROM courses'):
                print(row)
 
        elif i2 == '3':
            print("---------------------------------------------")
            print()     
            print('Name text, managementNumber text, position text')
            for row in cur.execute('SELECT * FROM staff'):
                print(row)
        
        elif i2 == '4':
            i = input('Please enter a studentIDcard')
            j = (i,)
            for row in cur.execute('SELECT * FROM openCourses where idcard = (?)',j):
                print(row)
        
        elif i2 == '5':
            i = input('Please enter a courese name')
            j = (i,)
            for row in cur.execute('SELECT * FROM openCourses where courseName = (?)',j):
                print(row)
            
             
            
        else:
            break
    main()
    
# 学生入口函数
def studentLogin():
    print("---------------------------------------------")
    print()
    # 输入学生基本信息
    print('Welcome! ')
    print('Please enter the name, age, gender, management number, address, and telephone in order, separated by spaces.')
    i = input().split()
    try:
        teacher1 = Staff(i[0],int(i[1]),i[2],int(i[3]),i[4],i[5])
        j = (i[0],i[3],'student')
        cur = con.cursor()
        cur.execute("INSERT INTO staff VALUES (?,?,?)",j)
        con.commit()
    except:
        print('Wrong input, please retry')
        teacherLogin()
        
    while True:
        print("---------------------------------------------")
        print()
        print('What do you want to do ?')
        print()
        print('1------show all course')
        print('展示所有课程（简略版）')
        print()
        print('2------choose a course')
        print('选课')
        print()
        print('3------my course')
        print('展示我的课程')
        print()
        print('else------Get back')
        print('返回主界面')
    
        i2 = input('Please press a number, and enter')   
        if i2 == '2':
            print('Please enter the courseName teacherName teachingDate teachingTime position and semester  separated by spaces')
            i2 = input().split()
            try:
                j = (i2[0],i2[1],i2[2],i2[3],i2[4],i[0],i2[5],i[3])
                cur = con.cursor()
                cur.execute("INSERT INTO openCourses VALUES (?,?,?,?,?,?,?,?)",j)
                con.commit()
            except:
                print('Wrong input!')
                
        elif i2 == '1':
            print("---------------------------------------------")
            print()     
            print('courseName  description  learningTime teacherName teachingDate  teachingTime  position ')
            for row in cur.execute('SELECT * FROM courses'):
                print(row)
 
        elif i2 == '3':
            print("---------------------------------------------")
            print()
            print('There are your course')
            j = (i[3],)
            for row in cur.execute('SELECT * FROM openCourses where idcard = (?)',j):
                print(row)
        else:
            break
    main()


# 教师端入口
def teacherLogin():
    print("---------------------------------------------")
    print()
    print('Welcome, teacher! ')
    print('Please enter the name, age, gender, management number, address, and telephone in order, separated by spaces.')
    i = input().split()
    try:
        teacher1 = Staff(i[0],int(i[1]),i[2],int(i[3]),i[4],i[5])
        j = (i[0],i[3],'teacher',)
        cur = con.cursor()
        cur.execute("INSERT INTO staff VALUES (?,?,?)",j)
        con.commit()
    except:
        print('Wrong input, please retry')
        teacherLogin()
        
    while True:
        print("---------------------------------------------")
        print()
        print('What do you want to do ?')
        print()
        print('1------New a course')
        print('新建课程')
        print()
        print('2------show course')
        print('展示所有课程（简略版）')
        print()
        print('3------show all')
        print('展示课程选课情况')
        print()
        print('else------Get back')
        print('返回主界面')
    
        i = input('Please press a number, and enter')   
        if i == '1':
            print('Please enter the course name description class hours teachingDate, teachingTime and position in order, separated by spaces')
            i = input().split()
            try:
                course1 = Course(i[0],i[1],i[2])
                j = (course1.courseName,course1.description,course1.learningTime,teacher1.name,i[3],i[4],i[5])
                cur = con.cursor()
                cur.execute("INSERT INTO courses VALUES (?,?,?,?,?,?,?)",j)
                con.commit()
            except:
                print('Wrong input! Please retry!')
        elif i == '2':
            print('courseName  description  learningTime teacherName teachingDate  teachingTime  position ')
            for row in cur.execute('SELECT * FROM courses'):
                print(row)
        elif i == '3':
            print('courseName teacherName teachingDate  teachingTime  position studentName semester idcard ')
            for row in cur.execute('SELECT * FROM openCourses'):
                print(row)
        else:
            break
    main()


        
    
def main():
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print()
    print('Welcome! This is a course selection system. ')
    print('这是一个简单的选课系统，数据库可能空空如也，要选课请先从教师入口创建课程')
    print()
    print('What is your position ?')
    print('选择你的身份，输入数字回车')
    print()
    print('1------admin')
    print()
    print('2------student')
    print()
    print('3------teacher')
    print()
    i = input('Please press a number, and enter')    
    if i == '1':
        adminLogin() 
    elif i == '2':
        studentLogin()
    elif i == '3':
        teacherLogin()
    else :
        print('wrong input , please retry!')
        print()
        main()
    
if __name__ == '__main__':
    # 链接数据库
    con = sqlite3.connect('csu.db') 
    # 设置游标
    cur = con.cursor
    cur = con.cursor()
    # 创建表格 因为可能重复创建而出错 用try语句包裹
    try:
        # 建立了三个表格
        cur.execute('''CREATE TABLE courses
                       (courseName text, description text, learningTime text,teacherName text,teachingDate text, teachingTime text, position text)''')
        cur.execute('''CREATE TABLE openCourses
                       (courseName text,teacherName text,teachingDate text, teachingTime text, position text,studentName text,semester text,idcard text)''')
        cur.execute('''CREATE TABLE staff
                       (Name text, managementNumber text, position text)''')                                      
        con.commit()
        con.close()
    except:
        pass
    # 进入主函数
    main()
    


        
    
    
