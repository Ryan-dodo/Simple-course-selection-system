package com.ryan.test;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * @Author : Ryan
 * @Email : ryan1057@163.com
 * @File :
 * @Software: IDEA
 * @Time :
 * @Github : https://github.com/Ryan-dodo
 * @using :
 */
public class StudentManeger {
    ArrayList<Student> students = new ArrayList<>();
    int studentsNum = 0;

    public StudentManeger() {
    }

    public StudentManeger(ArrayList<Student> students) {
        this.students = students;
    }

    public void add() {
        // 增
        Student student = new Student();
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入学生id");
        String sId = sc.next();
        // 检查id
        if (this.checkId(Integer.parseInt(sId))) {
            System.out.println("学生id重复请检查，添加失败");
            return;
        }
        student.setId(Integer.parseInt(sId));
        System.out.println("请输入学生姓名");
        String sName = sc.next();
        student.setName(sName);
        System.out.println("请输入学生年龄");
        int sAge = sc.nextInt();
        student.setAge(sAge);
        System.out.println("请输入学生地址");
        String sAddress = sc.next();
        student.setAddress(sAddress);
        this.students.add(student);
        studentsNum++;
    }

    public void del() {
        // 删
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入要删除的学生的id");
        String sId = sc.next();
        if (this.checkId(Integer.parseInt(sId))) {
            int id = this.getId(Integer.parseInt(sId));
            this.students.remove(id);
            studentsNum--;
        } else {
            System.out.println("id对应学生不存在");
        }
    }

    public Boolean checkId(int id) {
        // 查验id存在？
        for (int i = 0; i < studentsNum; i++) {
            if (students.get(i).getId() == id) {
                return true;
            }
        }
        return false;
    }

    public int getId(int id) {
        // 根据id获取索引
        for (int i = 0; i < studentsNum; i++) {
            if (students.get(i).getId() == id) {
                return i;
            }
        }
        return -1;
    }

    public void setData() {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入要修改学生的id");
        int id = sc.nextInt();
        for (int i = 0; i < studentsNum; i++) {
            if (students.get(i).getId() == id) {
                System.out.println("请输入要修改的姓名,输入0跳过修改");
                String sName = sc.next();
                if (sName.equals("0")) ;
                else {
                    students.get(i).setName(sName);
                }
                System.out.println("请输入要修改的年龄,输入0跳过修改");
                String sAge = sc.next();
                if (sAge.equals("0")) ;
                else {
                    students.get(i).setAge(Integer.parseInt(sAge));
                }
                System.out.println("请输入要修改的地址,输入0跳过修改");
                String sAddress = sc.next();
                if (sAddress.equals("0")) ;
                else {
                    students.get(i).setAddress(sAddress);
                }
                return;
            }
        }
        System.out.println("查无此人");
    }

    public int selectFromId() {
        // 查
        // 打印id对应学生信息
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入要查询学生的id");
        int id = Integer.parseInt(sc.next());
        for (int i = 0; i < studentsNum; i++) {
            if (students.get(i).getId() == id) {
                printStudent(i);
                return i;
            }
        }
        System.out.println("查无此人");
        return -1;
    }

    public void printBasicData() {
        System.out.println("id              姓名               年龄                 地址");
    }

    public void printStudent(int index) {
        System.out.println(students.get(index).getId() + "       " + students.get(index).getName() + "       " +
                students.get(index).getAge() + "       " + students.get(index).getAddress());
    }

    public void printAll() {
        printBasicData();
        for (int i = 0; i < studentsNum; i++) {
            printStudent(i);
        }
    }

    public void quickAdd() {
        Student student1 = new Student(001, "ryan", 12, "flea");
        Student student2 = new Student(002, "xn3", 213, "fle5646456a");
        Student student3 = new Student(003, "x342n", 2163563, "flegdfgdfa");
        Student student4 = new Student(004, "x55n", 266513, "fsrgslea");
        Student student5 = new Student(005, "xn23", 21633, "fhhqqqqqlea");
        students.add(student1);
        students.add(student2);
        students.add(student3);
        students.add(student4);
        students.add(student5);
        studentsNum = 5;
    }
}

