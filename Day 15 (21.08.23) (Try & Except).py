def name():
    try:
        y=input("Enter your name: ")
        print(f"Your Name is {y}")
    except ValueError:
        print("Enter Correct input [Text only]")
        name()

def number():
    try:
        x = int(input("Enter your mobile number: "))
        print(f"Your Mobile number is {x}")
    except ValueError:
        print("Enter Correct input [numbers only]")
        number()

def email():
    try:
        z=input("Enter your email id: ")
        print(f"Your Email is {z}")
    except ValueError:
        print("Enter correct Email ID")
        email()

name()
number()
email()