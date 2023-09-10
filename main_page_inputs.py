## run the main.py first
import user
import admin_inputs
import user_inputs

def mainpage():
    print("")
    print("                        COVID INFORMATION DATABASE")
    print("")
    print("[ User | Admin ]")
    print("")
    print("Input 1 --> [ Admin ]")
    print("Input 2 --> [ User ]")
    print("Input 3 --> [ Close the Application ]")
    print("")

    access_option=int(input(("Enter your option: ")))
    if access_option==1:
        admin_inputs.admin_login()
        admin_inputs.admin_actions()

    elif access_option==2:
        user.user_login()
        user_inputs.user_actions()

    elif access_option==3:
        print ("Thank you for using this application.")

    else:
        print("Invalid Input!!")
        mainpage()