import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="Localhost", user="root", password="", database="EMPLY_DB")

if con:
    print("DB CONNECTED...")

else:
    print("NOT CONNECTED")

def insert(EmpName, City, Age, Gender):
    res = con.cursor()
    sql = "insert into EM_DB (Empname, City, Age, Gender) values (%s,%s,%s,%s)"
    user = (EmpName, City, Age, Gender)
    res.execute(sql, user)
    con.commit()

def update(id, EmpName, City, Age, Gender):
    res=con.cursor()
    sql="update EM_DB set EmpName=%s, City=%s, Age=%s, Gender=%s where id =%s"
    user=(id, EmpName, City, Age, Gender)
    res.execute(sql, user)
    con.commit()

def select():
    res=con.cursor()
    sql="SELECT *from EM_DB"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result, headers=["id", "EmpName", "City", "Age", "Gender"],tablefmt="grid"))

def delete(id):
    res=con.cursor()
    sql="delete from EM_DB where id=%s"
    user=(id,)
    res.execute(sql, user)
    con.commit()


while True:
    print("1.DATA INSERT")
    print("2.DATA UPDATE")
    print("3.DATA SELECT")
    print("4.DATA DELETE")
    print("5.EXIT")

    choice = int(input("ENTER YOUR CHOICE.."))

    if choice == 1:
        EmpName = input("ENTER YOUR EMPLOYEE NAME : ")
        City = input("ENTER YOUR EMPLOYEE CITY : ")
        Age = input("ENTER YOUR EMPLOYEE AGE : ")
        Gender = input("ENTER YOUR EMPLOYEE GENDER : ")
        insert(EmpName, City, Age, Gender)
        print("DATA INSERTED!!!")

    elif choice==2:
        id=input("ENTER YOUR EMPLOYEE ID TO UPDATE : ")
        EmpName = input("ENTER YOUR EMPLOYEE NAME : ")
        City = input("ENTER YOUR EMPLOYEE CITY : ")
        Age = input("ENTER YOUR EMPLOYEE AGE : ")
        Gender = input("ENTER YOUR EMPLOYEE GENDER : ")
        update(EmpName, City, Age, Gender,id)
        print("DATA UPDATED!!!")

    elif choice==3:
        select()

    elif choice==4:
        id=input("ENTER YOUR EMPLOYEE ID TO DELETE : ")
        delete(id)
        print("DATA DELETED...")
    
    elif choice==5:
        exit("SUCCESSFULLY EXITED !!!")

    else:
        print("SOMETHING WENT WRONG.........")

