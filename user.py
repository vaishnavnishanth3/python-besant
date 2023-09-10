## run the main.py first
import mysql.connector
import main_page_inputs
import user_login_and_signup

covid_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid_data"
) 

cursor=covid_db.cursor()
def user_login():
    print("")
    print("[ Login | Sign Up ]")
    print("")
    print("Input 1 --> [ Sign-Up ]")
    print("Input 2 --> [ Login ]")
    print("")

    signin_option=int(input("Enter your option: "))

    if signin_option==1:
        print("")
        user_login_and_signup.sign_up()
        print("")
        main_page_inputs.mainpage()

    elif signin_option==2:
        print("")
        user_login_and_signup.log_in()
        print("")

    else:
        print("Invalid input!")
        user_login()

def view_individual_medical_data():
    name=input("Enter your Name: ")
    print("")
    sql_view_individual_medical_data="SELECT * FROM medical_database where Name = %s;"
    cursor.execute(sql_view_individual_medical_data,(name,))
    data = cursor.fetchall()
    print(data)
    covid_db.commit()
    print("")

def view_login_data():
    username=input("Enter your Username: ")
    print("")
    sql_view_individual_login_data="SELECT * FROM login_database where Username = %s;"
    cursor.execute(sql_view_individual_login_data,(username,))
    data = cursor.fetchall()
    print(data)
    covid_db.commit()
    print("")

def registration_data():
    print("")
    name=input("Enter your Name: ")
    reason=input("Enter your Reason for Appointment: ")
    appointment_datetime=input("Enter the appointment data & time: ")
    fee=input("Enter the Consultancy Fee: ")
    update=input("Enter the update in time (if available): ")

    sql_registaration_data="insert into appointment_registration (S_no,Name,`Reason for Appointment`,`Appointment Date and Time`,`Consultancy Fee`,`Update in time (if any)`) values (%s,%s,%s,%s,%s,%s)"
    val=(1,name,reason,appointment_datetime,fee,update)
    cursor.execute(sql_registaration_data,val)
    covid_db.commit()
    print("")
    print("Registration successfull")

def appointment_registration():
    print("")
    print("*********WELCOME TO COVID SPREAD MANAGEMENT SERVICE************")
    print("")
    print("Appointment Registration: ")    
    print("")
    print("Input 1 --> Register for appointment")
    print("Input 2 --> Exit to user Home page")
    access_option4=int(input("Enter your option: "))
    if access_option4==2:
        user_actions()

    elif access_option4==1:
        registration_data()

    else:
        appointment_registration()

def nextops_user():
    print("[ Continue | Logout ]")
    print("")
    print("Input 1 --> Continue")
    print("Input 2 --> Logout")

    option1=int(input("Enter your input: "))
    if option1==1:
        user_actions()
    if option1==2:
        main_page_inputs.mainpage()
    else:
        nextops_user()

def user_actions():
    print("")
    print("[ View medical data with test results | View login data | Register for appointment]")
    print("")
    print("Input 1 --> View medical data with test results")
    print("Input 2 --> View login data")
    print("Input 3 --> Register for appointment")
    print("")

    access_option3=int(input("Enter your Option: "))

    if access_option3==1:
        print("")
        view_individual_medical_data()
        print("")
        nextops_user()
    
    elif access_option3==2:
        print("")
        view_login_data()
        print("")
        nextops_user()

    elif access_option3==3:
        print("")
        appointment_registration()
        print("")
        nextops_user()

    else:
        print ("Invalid input!")
        user_actions()
