#sem6:
print("")
print("Input must be in numbers")
print("O  -- 10")
print("A+ -- 09")
print("A  -- 08")
print("B+ -- 07")
print("B  -- 06")
print("")

print("Sem 7:")
#credits:
cs7p1=3
cs7p2=3
cs7p3=3
cs7p4=3
cs7p5=3
cs7p6=3
cs7p7=2
cs7p8=2
cs7p9=2
print("")

#arrear:

#scores:
s7p1=int(input("Enter Score for Sub 1                     : "))
s7p2=int(input("Enter Score for Sub 2                     : "))
s7p3=int(input("Enter Score for Sub 3                     : "))
s7p4=int(input("Enter Score for Open Elective II          : "))
s7p5=int(input("Enter Score for Professional Elective II  : "))
s7p6=int(input("Enter Score for Professional Elective III : "))
s7p7=int(input("Enter Score for Lab 1                     : "))
s7p8=int(input("Enter Score for Lab 2                     : "))
s7p9=int(input("Enter Score for Naan Mudhalvan            : "))
print("")

#credit*score
css7p1=s7p1*cs7p1
css7p2=s7p2*cs7p2
css7p3=s7p3*cs7p3
css7p4=s7p4*cs7p4
css7p5=s7p5*cs7p5
css7p6=s7p6*cs7p6
css7p7=s7p7*cs7p7
css7p8=s7p8*cs7p8

print("")

print(css7p1,css7p2,css7p3,css7p4,css7p5,css7p6,css7p7,css7p8)
print("")
s7ssum=css7p1+css7p2+css7p4+css7p5+css7p6+css7p7+css7p8
s7csum=cs7p1+cs7p2+cs7p4+cs7p5+cs7p6+cs7p7+cs7p8
gpas7=s7ssum/s7csum
print(f"Score Sum is {s7ssum}")
print("")
print(f"Credit Sum is {s7csum}")
print("")
print(f"GPA for Sem 6 is {gpas7}")
print("")