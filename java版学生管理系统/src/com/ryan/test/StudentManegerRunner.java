package com.ryan.test;

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
public class StudentManegerRunner {
    public static void main(String[] args){
        System.out.println("------欢迎进入Ryan的学生管理系统------");
        System.out.println("输入1：增加学生");
        System.out.println("输入2：删除学生");
        System.out.println("输入3：更改学生");
        System.out.println("输入4：查询学生");
        System.out.println("输入5：退出");
        StudentManeger studentManeger = new StudentManeger();
        studentManeger.quickAdd();
        studentManeger.printAll();
        Scanner scanner = new Scanner(System.in);
        while (true){
            System.out.println("下面请输入指令:1：增加学生2：删除学生3：更改学生4：查询学生5：退出");

            int instruction = scanner.nextInt();
            switch (instruction){
                case 1: studentManeger.add();
                    break;
                case 2: studentManeger.del();
                    break;
                case 3: studentManeger.setData();
                    break;
                case 4: studentManeger.selectFromId();
                    break;
                case 5: return;
            }
        }
    }
}
