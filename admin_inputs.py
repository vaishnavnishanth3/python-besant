# run the main.py first
import mysql.connector
import main_page_inputs
import random

covid_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid_data"
) 

cursor=covid_db.cursor()

def admin_login():

    admin_id=input("Enter your ID: ")
    admin_password=input("Enter your Password: ")

    try:
        sql_login = "SELECT `Admin Password` FROM admin_database WHERE `Admin ID` = %s"
        cursor.execute(sql_login, (admin_id,))
        result = cursor.fetchone()

        if result is not None and result [0] == admin_password :
            print("")
            print("Admin Login Successfull")
            print("")

        else:
            print("The Username / Password is invalid")
            print("")
            admin_login()

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        print("")
        admin_login()

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and covid_db.is_connected():
            covid_db.close()

def view_active():

    sql_view_active="SELECT * FROM medical_database where `Test Result` = 'POSITIVE' ;"
    cursor.execute(sql_view_active,)
    for data in cursor.fetchall():
        print(data)
    covid_db.commit()
    print("")

def appointment_schedule():
    
    sql_view_login_db="SELECT * FROM appointment_registration;"
    cursor.execute(sql_view_login_db,)
    for data in cursor.fetchall():
        print(data)
    covid_db.commit()
    print("")

def view_login_data():

    sql_view_login_db="SELECT * FROM login_database;"
    cursor.execute(sql_view_login_db,)
    for data in cursor.fetchall():
        print(data)
    covid_db.commit()
    print("")

def view_medical_data():

    sql_view_medical_data="SELECT * FROM medical_database;"
    cursor.execute(sql_view_medical_data,)
    for data in cursor.fetchall():
        print(data)
    covid_db.commit()
    print("")

def email_sending():

    login_maidid=input("Enter the Login Mail ID: ")
    login_mailid_password=input("Enter the login Mail Password: ")
    reciever_mailid=input("Enter the Reciever Id: ")
    message = input("Enter the Message to be sent: ")

    import smtplib
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(login_maidid, login_mailid_password)
    s.sendmail(login_maidid, reciever_mailid , message)
    s.quit()
    print("")
    print("Email Sent Successfully!!")
    print("")

def insert_data():

    s_no=random.randint(0000,9999)
    name=input("Enter Patient Name: ")
    age=input("Enter Patient Age: ")
    testtype=input("Enter the Test type: ")
    testdate=input("Enter the Date of test: ")
    doneby=input("Test Done by: ")
    result=input("Test Result: ").upper()
    amount=input("Enter the Amount paid: Rs.")

    sql_insert="insert into medical_database (S_no,Name,Age,`Test Type`,`Test Date`,`Test Done by`,`Test Result`,`Amount paid for Test`) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(s_no,name,age,testtype,testdate,doneby,result,amount)
    cursor.execute(sql_insert,val)
    covid_db.commit()
    
    print("")
    print("Data Inserted!!")
    print("")

def update_result_data():

    reference_value=input("Enter the Name: ")
    change_data=input("Modified Data: ")

    sql_update_result="update medical_database set `Test Result` = %s where Name = %s"
    val=(change_data,reference_value)
    cursor.execute(sql_update_result,val)
    covid_db.commit()
    print("")
    print("Updated!!")

def admin_actions():
    print("")
    print("[ View Medical Data | View Login Data | Send Email ]")
    print("")
    print("Input 1 --> View Medical Data")
    print("Input 2 --> View Login Data")
    print("Input 3 --> Insert Data")
    print("Input 4 --> Update Test Result Data")
    print("Input 5 --> View Active Cases")
    print("Input 6 --> View Appointment Schedule")
    print("Input 7 --> Send Email")
    print("Input 8 --> Log-out")
    print("")
    
    access_option_2=int(input("Enter the input: "))

    if access_option_2==1:
        print("")
        view_medical_data()
        print("")
        nextops()

    elif access_option_2==2:
        print("")
        view_login_data()
        print("")
        nextops()

    elif access_option_2==3:
        print("")
        insert_data()
        print("")
        nextops()

    elif access_option_2==4:
        print("")
        update_result_data()
        print("")
        nextops()

    elif access_option_2==5:
        print("")
        view_active()
        print("")
        nextops()

    elif access_option_2==6:
        print("")
        appointment_schedule()
        print("")
        nextops()

    elif access_option_2==7:
        print("")
        email_sending()
        print("")
        nextops()

    elif access_option_2==8:
        print("Logged Out")
        main_page_inputs.mainpage()

    else:
        print("Invalid inputs")
        print("")
        admin_actions()

def nextops():

    print("[ Continue | Logout ]")
    print("")
    print("Input 1 --> Continue")
    print("Input 2 --> Logout")

    option1=int(input("Enter your input: "))
    if option1==1:
        admin_actions()
    if option1==2:
        main_page_inputs.mainpage()
    else:
        nextops()