# python function:
# def function_name():
#     print statement
# function_name()

print("")
def stdata():
    print("Called")
stdata() # simple function creation code
print("")

#argument pass into the function:

print("Argument Passing into def():")
def createnewaccount(username,password): #email,passoword are parameters/arguments
    if username=="ranjithshivn" and password=="Shiv@python":
        print ("Succesfull")
    else:
        print("pls check")

username=input("Username: ")
password=input("Password: ")

createnewaccount(username,password)
print("")

def oddoreven(num):
    if num%2==0:
        print("Even Num")
    else:
        print("Odd Num")

num=int(input("Enter the Number: "))
oddoreven(num)

def oddoreven():
    x=10
    y=20
    c=x+y
    return c

def data():
    print(5+oddoreven())
data() 
print("")

#Calling the function using conditional statement
print("Bee Techs: ")
print("1 - tea")
print("2 - coffee")
print("3 - Juice")
print("")
user=int(input("Enter your option: "))
print("")
def tea():
    print("You've selected tea")
    
def coffee():
    print("You've selected coffee")

def juice():
    print("You've selected Juice")

if user==1:
    tea()
elif user==2:    
    coffee()
elif user==3:
    juice()
print("")