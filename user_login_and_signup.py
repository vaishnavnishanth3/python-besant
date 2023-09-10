## run the main.py first
import mysql.connector
import random
import user

covid_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid_data"
) 

cursor=covid_db.cursor()

def sign_up():

    s_no=random.randint(0000,9999)
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    gender=input("Enter your gender [M/F/Others]: ")
    mobile=int(input("Enter your Mobile: "))
    email=input("Enter your Email: ")
    username=input("Enter your Username: ")
    password=input("Enter your password: ")

    sql_insert_data="insert into login_database (S_No, Username, Password, Name, Age, Gender, Mobile, Email) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(s_no,username,password,name,age,gender,mobile,email)
    cursor.execute(sql_insert_data,val)
    covid_db.commit()
    print("")
    print("Sign Up Successfully")
    user.user_login()

def log_in():

    login_username=input("Enter your username: ")
    login_password=input("Enter your password: ")

    try:
        sql_login = "SELECT Password FROM login_database WHERE Username = %s"
        cursor.execute(sql_login, (login_username,))
        result = cursor.fetchone()

        if result is not None and result [0] == login_password :
            print("")
            print("Login Successfull")
        else:
            print("The Username / Password is invalid")
            log_in()
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        log_in()
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and covid_db.is_connected():
            covid_db.close()