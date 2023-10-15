def extractdata():
#to create a new file:
    print("")
    print("1) New File Creation:")
    print("")
    f=open("Day16module.txt","x") #add x--> to create a new files
    print("Debug Information: File Created Successfully")
    print("")

#read:
    print("2) Read:")
    f=open("Day16module.txt","r") #r--> to read the file 
    data1=f.read()  
    print(data1)
    print(type(data1))
    print("")

#Type conversion: (to list)
    print("3) Type Conversion:")
    print("To List:")
    x=data1.split(",")
    print(x)
    print("")

    print("a) Length:")
    y=len(x)
    print(y)
    print("")

    print("b) Extract Count:")
    z=x.count("paid")
    print(z)
    print("")
 
    paid=[]
    unpaid=[]
    for i in x:
        if i=="paid" or i==" paid" or i=="paid " or i==" paid ":
            paid.append(i)
        elif i=="unpaid" or i==" unpaid" or i=="unpaid " or i==" unpaid ":
            unpaid.append(i)
    print(f"paid--> {len(paid)}")
    print(f"unpaid--> {len(unpaid)}")

extractdata()

#Chatgpt Reduced:
#def extractdata():
#    with open("aug22.txt", "r") as f:
#        data1 = f.read()
#    
#    x = [i.strip() for i in data1.split(",")]
#    
#    paid = [i for i in x if i.strip() == "paid"]
#    unpaid = [i for i in x if i.strip() == "unpaid"]
#    
#    print(f"paid --> {len(paid)}")
#    print(f"unpaid --> {len(unpaid)}")

#extractdata()

#append a file:
print("")
print("Append a file:")
f=open("Day16module.txt","a") #add a
f.write(", unpaid")
print("Data Added Successfully")
print("")

#overwrite a file:
print("")
print("Overwrite a file:")
f=open("Day16module.txt","w") #add w
f.write("bye bro")
print("Data Added Successfully")
print("")

#to remove the file from the device
print("Delete a file:")
import os
os.remove("C:/Vaishnav/Courses/Python/Codes/Day16module.txt")
print("Deleted Successfully")