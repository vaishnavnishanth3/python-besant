print(" ")
print("1) type(): ")
print(" ")

#stringarrays
#text type->str
#numeric type->int,float
#sequence type->list,tuple
#set type->dict
#boolean type->bool
#NoneType->None

a=input("Enter the Word: ")
b=int(input("Enter the Integer: "))
c=float(input("Enter the Float: "))
print("")
print(type(a),type(b),type(c))
print("")

print("2) Indexing:")

city=input("Enter the Word: ")

#Indexing
#  k  a  l  l  a  i
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1 

print("")
print(f"The Index [5] gives: {city[5]}")
print(f"The Index [:-2] gives: {city[:-2]}")
print("")

#stringslicing
#variablename[startindex:endindex]

print("# String Slicing: ")
word=input("Enter the word (min 10): ")
print(f"The Index [4:7] gives: {word[4:7]}")
print(f"The Index [8:10] gives: {word[8:10]}")
print("")

#stringmethods

#3)Uppercase():
print("3) Uppercase(): ")
name=input("Enter you Name: ").upper()
print(name.upper())
print("")

if name=="ARUN" or name=="arun":
    print(name," is Allowed")
print("")

#4)Capitalize():
print("4) Capitalize(): ")
print(name.capitalize())

#5)Count the numbers:
print("")
print("5) Count & Find: ")
name1=input("Enter the Name: ")

print("")
print("# Count(): ")
y1=input("Enter the word for the letter to be counted: " ) 
x=name1.count(y1) #to find the no.of.strings present in the word
print(x)
print("")

#6)Find the string:
print("# Find(): ")
y2=input("Enter the letter to be found: ")
z=name1.find(y2) #to find the no.of.repeats of the string 
print(z)
print("")