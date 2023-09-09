import mysql.connector

assignment_db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="12345",
    database="assignment_db"
)

cursor = assignment_db.cursor()

def create_table():
    sql_create_table="create table user_info (S_no int, Name varchar(255),Age varchar(255),Number varchar(255),Email varchar(255))"
    cursor.execute(sql_create_table)
    assignment_db.commit()
    print("Table created !!")

def insert_data():
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    number=input("Enter the Mobile: ")
    email=input("Enter the email: ")
    
    sql_insert="insert into user_info (Name,Age,Number,Email) values (%s,%s,%s,%s)"
    val=(name,age,number,email)
    cursor.execute(sql_insert,val)
    assignment_db.commit()
    
    print("")
    print("Data Inserted!!")
    print("")


def view_data():
    name=input("Enter your Name: ")
    print("")
    sql_view_individual_medical_data="SELECT * FROM user_info where Name = %s;"
    cursor.execute(sql_view_individual_medical_data,(name,))
    data = cursor.fetchall()
    print(data)
    assignment_db.commit()
    print("")



    
def update_name():
    change_data=input("Modified Name: ")
    reference_value=input("Enter the Email: ")
    sql_update_result="update user_info set Name = %s where Email = %s"
    val=(change_data,reference_value)
    cursor.execute(sql_update_result,val)
    assignment_db.commit()
    print("")
    print("Updated!!")

def update_age():
    change_data=input("Modified Age: ")
    reference_value=input("Enter the Name: ")
    sql_update_result="update user_info set Age = %s where Name = %s"
    val=(change_data,reference_value)
    cursor.execute(sql_update_result,val)
    assignment_db.commit()
    print("")
    print("Updated!!")   

def update_number():
    change_data=input("Modified Number: ")
    reference_value=input("Enter the Name: ")
    sql_update_result="update user_info set Number = %s where Name = %s"
    val=(change_data,reference_value)
    cursor.execute(sql_update_result,val)
    assignment_db.commit()
    print("")
    print("Updated!!")  

def update_email():
    change_data=input("Modified Email: ")
    reference_value=input("Enter the Name: ")
    sql_update_result="update user_info set Email = %s where Name = %s"
    val=(change_data,reference_value)
    cursor.execute(sql_update_result,val)
    assignment_db.commit()
    print("")
    print("Updated!!")     

def main2():
    print("Enter 1 -- > Change Name")
    print("Enter 2 --> Change Age")
    print("Enter 3 ---> Change Mobile")
    print("Enter 4 --> Change Email")
    print("Enter 5 --> Exit")
    print("")
    option2=int(input("Enter your option: "))

    if option2==1:
        update_name()
        main2()
    elif option2==2:
        update_age()
        main2()
    elif option2==3:
        update_number()
        main2()
    elif option2==4:
        update_email()
        main2()
    elif option2==5:
        print("Exiting...Done")

def main():
    print("[ View | Insert | Update ]")
    print("Enter 1 --> [Create Table]")
    print("Enter 2 --> [Insert Data]")
    print("Enter 3 --> [View Data]")
    print("Enter 4 --> [Update Data]")
    print("Enter 5 --> Exit")
    print("")
    option=int(input("Enter your Option: "))


    if option==1:
        create_table()
        main()

    elif option==2:
        insert_data()
        main()

    elif option==3:
        view_data()
        main()

    elif option==4:
        main2()
    
    elif option==5:
        print("Exiting...Done")

    else:
        print("Invalid input!!!")
main()