#assigning your variables
#using f string to avoid closing the strings & \n, \t to jump the context to next line and a tab space

firstname=input("Enter the firstname: ")
lastname=input("Enter the lastname: ")
age=int(input("Enter the age: "))
height=float(input("Enter your height: "))

print(" ")
print(f"My firstname is {firstname}, my lastname is {lastname} & \nmy height is {height} - Ranjith Shivn")
print(" ")
print(f"My firstname is {firstname}, my lastname is {lastname} & my height is {height} \t- Ranjith Shivn")
print("")