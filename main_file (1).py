import mysql.connector as a

# connect to database
con=a.connect(host='localhost',user='chhavi', database='test',passwd='lakshya')


def AddSt():
    n=input("Student name: ")
    r=input("Roll no:")
    cl=input("Class:")
    a=input("Address:")
    ph=input("Phone: ")
    sql=f"insert into test.student (name, roll, class, address, phone) values ('{n}','{r}','{cl}','{a}','{ph}')"
    c=con.cursor()
    c.execute(sql)
    con.commit()
    print("Data entered successfully")
    print("")
    main()


def RemoveSt():
    name=input("Name of student: ")
    r=input("Roll no of student: ")
    cl=input("class of student: ")
    sql=f"Delete from student where name = '{name}' and class = '{cl}' and roll = '{r}'"
    c=con.cursor()
    c.execute(sql)
    con.commit()
    print ("Data deleted successfully")
    print("")
    main()


def DisplaySt():
    cl=input("Class:")
    sql=f"select * from test.student where class='{cl}'"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    print("--------------------------------------------------")
    print("Name, Class, Roll No, Address, Phone")
    for i in d:
        print(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}")
    print("--------------------------------------------------")
    main()


def UpdateFees():
    cl=input("Enter Class: ")
    fees=input("Enter the new Fees: ")
    sql=f"update test.FEE_STRUCTURE set amount = '{fees}' where class = '{cl}'"
    c=con.cursor()
    c.execute(sql)
    con.commit()
    print("Data updated successfully")
    print("")
    main()


def DisplayFees():
    sql=f"select * from test.FEE_STRUCTURE;"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    print("------------------------------------------")
    print("Class    Fees")
    for i in d:
        print(f" {i[0]}  : {i[1]} ")
    print("------------------------------------------")
    main()


def main():
    ch='y'
    while ch in ['y', 'Y']:
        print("########################################################")
        print("# LUCKNOW PUBLIC SCHOOL DATABASE MANAGEMENT SYSTEM     #")
        print("# Table Number | Table Name                            #")
        print("#  1           |  Student                              #")
        print("#  2           |  Fee_Structure                        #")
        print("#  Press 3 to quite application                        #")
        print("########################################################\n")
        table=int(input ("Enter table Number to operate:  "))
        print("")

        # Student Table condition
        if table==1:
            op='y'
            while op in ['y', 'Y']:
                print(".------------------------------------------------------.")
                print("| Task Number  |  Operations                           |")
                print("| 1            |  Add student                          |")
                print("| 2            |  Remove student                       |")
                print("| 3            |  Display St detail                    |")
                print(".------------------------------------------------------.")
                task=int (input ("Enter task no to operate:  "))
                if task==1:
                    AddSt()
                elif task==2:
                    RemoveSt()
                elif task==3:
                    DisplaySt()
                else:
                    print("Please enter a valid choice!!")
                op=input("Continue in this table(y/n):")

        # Fee Structure condition
        elif table==2:
            op='y'
            while op in ['y', 'Y']:
                print(".------------------------------------------------------.")
                print("| Task Number  |  Operations                           |")
                print("| 1            |  Update Fees                          |")
                print("| 2            |  Display Fees                         |")
                print(".------------------------------------------------------.")
                task=int (input ("Enter task no to operate:  "))
                if task==1:
                    UpdateFees()
                elif task==2:
                    DisplayFees()
                else:
                    print ("Enter Valid Choice!!")
                op=input("Continue in this table (y/n) :")

        # Quite application
        elif table==3:
            break

        # Invalid choice provided by the user
        else:
            print("ENTER VALID CHOICE!!!")
        ch=input("Do you want to continue (y/n): ")

if __name__ == '__main__':
    print("CLASS 12th Project on Student Management System made by-")
    print("CHHAVI SAXENA")
    print("AGREEMA SRIVASTAVA")
    print("AROOSH DATTA\n")
    main()
