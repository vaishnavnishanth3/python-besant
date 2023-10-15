#python operators

# 1)arithmetic (+,-,*,/,%) and GST calculations. Total = Original + GST. GST = (Original x GST%)/100

print("")
print("1) Arithmetic Operators: ")
print("a) Fundamentals: ")
print("")

a=int(input("Enter the First number: "))
b=int(input("Enter the Second number: "))

c=a+b
d=a-b
e=a*b
f=a/b
g=a%b

print("")
print(f" First Number={a}, \n Second Number={b}, \n  \n Addition={c}, \n Subtraction={d}, \n Multiplication={e}, \n Division={f}, \n Modulus={g}")
print("")
print("b) GST: ")

op=int(input("Enter The Original Price: "))
gstpercent=int(input("Enter The GST%: "))
totp=op+((op*gstpercent)/100)

print("")
print(f"The Total Price is {totp}")

# 2) Assignment Operators (=, += , -= , *= , /=).

print("")
print("2) Assignment Operators: ")

i=int(input("Enter the Intial Value: "))
j=int(input("Enter the Increment Value: "))

h=i #h1
h+=j #h1 #h2=h1+5

print("")
print(h)

#type(): To identify the type.

print("")
print("# Type(): (From:[int,str,float])")
print("")

k=12
l="value"
m=7.79

print("")
print(f"The Inputs are: \n {k} \n {l} \n {m}")
print("")
print(f"The type of the input: \n {k} is {type(k)}, \n {l} is {type(l)}, & \n {m} is {type(m)}")

#3) Comparison Operators (==,<=,>=,>,<,!=).

print("")
print("3) Comparion Operators: ")
print("")

n=int(input("Enter the First number: "))
o=int(input("Enter the Second number: "))

print("")
print(f"The two values are {n},{o}")
print("a) Are they Equal?")
print(n==o) 
print("b) Is the first value greater than or equal to the second?")
print(n>=o)
print("c) Is the first value lesser than or equal to the second?")
print(n<=o)
print("d) Is the first value lesser than the second?")
print(n<o)
print("e) Is the first value greater than the second?")
print(n>o)
print("")

#4) Logical Operators (AND, OR, NOT):
#AND: If both the condtions are true, return true.
#OR: If any one the conditions in true, return true.
#NOT: Reverse the Result.

print("4) Logical Operators: ")
print("a)")

p=10
q=15

print("")
print(f"The Values are {p},{q}")
print("")
print(f"If P=10 & Q=20: {p==10 and q==20}")
print(f"If P=10 | Q=20: {p==10 or q==20}")
print(f"Not p, Not q : {not(p==10),not(q==10)}")
print("")

dept=input("Enter your department [From BCA, MCA, CSE, IT only]: ")
print(f'Eligiblity: {dept=="BCA" or dept=="MCA" or dept=="CSE" or dept=="IT" or dept=="bca" or dept=="mca" or dept=="cse" or dept=="it"}')

if dept=="BCA" or dept=="MCA" or dept=="CSE" or dept=="IT" or dept=="bca" or dept=="mca" or dept=="cse" or dept=="it":
    print("You're Allowed")
else:
    print("Go Out")

#Identity Operator:

print("")
print("# Identity Operator: ")
print("")

a=int(input("Enter the First Value: "))
b=a

print("Second Value = First Value")
print("")
print(f"The second value is not equal to the first value?: {b is not a}")

#5) Membership Operator (in, not in)

print("")
print("5) Membership Operator: ")
print("")

fruits=["Banana", "Grapes", "Apple"]
print(f"Available Fruits are {fruits}")
print("")

fruit=input("Enter the your fruit: ").capitalize
print (f"Availability: {fruit().capitalize in fruits}")