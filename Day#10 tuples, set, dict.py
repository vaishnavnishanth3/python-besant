#1) Tuples:
print("")
print("1) Tuples: ")
nums=("integers","real","decimal","imaginery")
print(type(nums)) #multipleitems/values,ordered,allow duplicates,unchangable
print(nums)

#2) Sets:
print("")
print("2) Sets: ")
set1={"Takes","Fandom","Brains","Fork","Fork"}
print(type(set1))
print(set1) #multiplevalues/items,unordered,noduplicates,unchangable

#set constructor:
print("")
print("Set Constrctor: ")
set2=set(("Takes","Fandom","Brains","Fork","Fork"))
print(type(set2))
print(set2)

#Remove Dupliactes from list 
print("")
print("Remove Duplicates: ")
list1=[21,25,65,21,59,25,21,26,59]
nodups=[*set(list1)]
print(nodups)

#3) Dictionaries:
print("")
print("3) Dictionaries: ")
data={"int":55.58,"real":56,"dec":25.56,"flt":36.9,"flt":26.9}
print(type(data))
print(data)

#Key Value Change:
print("")
print("Key Value change: ")
data["flt"]=46.9
print(data)

#Display Keys & Values:
print("")
print("Keys() & Values(): ")
x=data.keys()
y=data.values()
print(x,y)

#4) Logical:
print("")
print("4) Logical: ")
opr=input("Type of Arithmetic Operation (in words/symbols): ")
if opr=="ADD" or opr=="add" or opr=="Add" or opr=="+" or opr=="SUBTRACT" or opr=="subtract" or opr=="Subtract" or opr=="-" or opr=="MULTIPLY" or opr=="Multiply" or opr=="multiply" or opr == "*" or opr=="x" or opr=="X" or opr=="Divide" or opr=="DIVIDE" or opr=="divide" or opr=="/":
    print(f"{opr}:")
    g=int(input("Enter the First Value: "))
    h=int(input("Enter the Second value: "))
    add=g+h
    subtract=g-h
    multiply=g*h
    divide=g/h
    if opr=="add" or opr=="ADD" or opr=="Add"or opr=="+":
        print(add)
    elif opr=="subtract" or opr=="SUBTRACT" or opr=="Subtract" or opr=="-":
        print(subtract)
    elif opr=="multiply" or opr=="Multiply" or opr=="Multiply" or opr=="x" or opr=="X" or opr=="*":
        print(multiply)
    elif opr=="divide" or opr=="DIVIDE" or opr=="Divide" or opr=="/":
        print(divide)

else:
    print("Invalid Operation")    
print("")

#5) Boolean(Bool):
print("5) Boolean: ")
r=True
s=False

if r:
    print("The Statement is true")
else:
    print("The Statement is False")
print(type(r))
print(r,s)

#6)None Type:
print("")
print("6) None Type: ")
z=None
print(type(z))
print(z)
print("")

#7) Type Conversion:
f=open("newdoc.txt","r")
data=f.read()
x=data.split(",")
print(x)
print("")