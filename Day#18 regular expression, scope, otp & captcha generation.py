#re--> regular expression:
print("")
def hotel():
    try:
        import re
        txt="hi guys i am suffering from fever"
        print("")

        word=input('Enter the Word: ')
        y=re.search(word,txt)

#print(y) #re.Match==True# 

        if y:
            print(f"{word} is available")
        else:
            print(f"Not available")
        print("")

        f=open("Day18module.txt","r")
        txt1=f.read()
        f.close() #close after read
        print(f"menus->{txt1}")
        print("")
        food=input("Enter your food: ")
        x=re.search(food,txt1)
        z=re.findall(food,txt1)
        print(len(x))

        if x:
            print("Available")
        else:
            print("Not Available")
        print("") #if file not found (File not found error)

    except:
        print("File is not present")

#python-scope:
#local scope:
    def localscope():
        hername="Hello"
        print(x)

    def chennai():
        ponnuname="Malar"
        print(f"ponnu name is {ponnuname}")

    def kumbakonam():
        ponnuname="Malar"
        print(f"ponnu name is {ponnuname}")

    def trichy():
        ponnuname="Malar"
        print(f"ponnu name is {ponnuname}")

#globalscope:
ponnuname="Malar"

def chenai():
    global ponnuname
    print(f"ponnu name is {ponnuname}")

def thiruchi():
    global ponnuname
    print(f"ponnu name is {ponnuname}")
    
hotel()
print("")

#OTP Generation:
print("OTP Generation: ")
import random
otp=random.randint(0000,9999)
print(f"Your OTP is {otp}")
print("")

#Captcha Generation:
print("OTP Generation: ")
import string
import random
captcha=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=5))
print(f"Your Captcha is --> {captcha}")
print("")