#If:
print("")
print("a) If:")

dept1=input("Enter your dept: ")
if dept1=="MCA":
    print("You're Allowed")
if dept1!="MCA":
    print("You're not Allowed")

#Elif:
print("")
print("b) Elif:")

dept=input("Enter your department: ")
if dept=="MCA" or dept=="mca" or dept=="BCA" or dept=="bca":
    print("Your're Allowed")
elif dept=="Staff" or dept=="HOD":
    print("ID need to be verified")
else:
    print("You're not Allowed")

print("")
print("")
print("WELCOME TO SHIV HOTEL")
print("")
print("Menu:")
print("1) Dosa(20),")
print("2) Idli(5)")
print("3) Poori(15). ")
print("")

d=20 #dosa
i=5 #idli
p=15 #poori

menu=["Dosa","dosa","idli","Idli","poori","Poori"]
yourorder=input("Enter your Order: ")

if yourorder in menu:
    print(f"Your Order, {yourorder} is available.")
    print(" ")

    num_order=int(input("Enter No.of.Orders: ")) 
    totd=num_order*d
    toti=num_order*i
    totp=num_order*p
    distotd=(90*totd)
    distoti=(90*toti)
    distotp=(90*totp)
    if yourorder=="Dosa" or yourorder=="dosa":
        print(f"Your bill is Rs.{totd}")
        if totd>=1000:
            print("")
            print("It is above Rs.1000 and eligible for discount of 5%")
            print(f"Total Discount price is {distotd}")
    elif yourorder=="Idli" or yourorder=="idli":
        print(f"Your bill is Rs.{toti}")
        if toti>=1000:
            print("")
            print("It is above Rs.1000 and eligible for discount of 5%")
            print(f"Total Discount price is {distoti}")
    elif yourorder=="Poori" or yourorder=="poori":
        print(f"Your bill is Rs.{totp}")
        if totp>=1000:
            print("")
            print("It is above Rs.1000 and eligible for discount of 5%")
            print(f"Total Discount price is {distotp}")
else:
    print(f"Your Order {yourorder} is not available")