#if,elif,nestedif,else
age=int(input('Age: '))

if age>=18:
    print("You're ELIGIBLE to enter this club😊")
else:
    print("GET OUT😆")

#odd/even using if:
print("")
age2=int(input("Enter your age: "))

if age2%2==0:
    print("EVEN")
if age2%2!=0:
    print("ODD")
    
#login checking using if: 
print("")
username=input("Username: ")
password=input("Password: ")

dbusername="ranjithshivn"
dbpassword="Shiv@python"

if username==dbusername and password==dbpassword:
    print("Login SUCCESSFUL")
else:
    print("INVALID username and password")

#palindrom (refer) (same from both from front and back) (Problem Solving)

print("")
word=input('Enter the word: ')
print(f"normal word-> {word} ")
print(f"after reverse-> {word[::-1]}")

if word==word[::1]:
    print("It's a PALINDROME")
else:
    print("It's NOT a PALINDROME")

print("")
dept=input("Enter your department: ")
if dept=="IT" or dept=="it" or dept=="CSE" or dept=="cse" or dept=="BCE" or dept=="bca" or dept=="MCA" or dept=="mca" or dept=="AIDS" or dept=="aids":
   print("You're ELEGIBLE")
else:
    print("You're not eligible")