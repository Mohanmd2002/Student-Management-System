import pymysql
a=pymysql.connect(
    host="localhost",
    user="root",
    password="Mohan2002@",
    database="student_management_2"
    )
#to create data base:
##mycursor=a.cursor()
##mycursor.execute("CREATE DATABASE student_management_2")

#to create table:
mycursor=a.cursor()
mycursor.execute("CREATE TABLE student_register(first_name VARCHAR(50),last_name VARCHAR(50),course VARCHAR(50),course_package VARCHAR(50),date VARCHAR(50),age INT,gender VARCHAR(50),birth VARCHAR(50),contact VARCHAR(50),email VARCHAR(50),current_course VARCHAR(50),pending_course VARCHAR(50),completed_course VARCHAR(50),Total_fees VARCHAR(50),paid_fees VARCHAR(50),balance_fees VARCHAR(50))")
