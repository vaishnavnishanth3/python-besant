#python keywords: if, elif, else, for, while, etc....
#while loop:
#syntax:
#while condition:
#   print statement
#   increment
print("")
print("1) i) While:")
a=int(input("Enter the Initial Value: "))
b=int(input("Enter the Higher Limit: "))
c=int(input("Enter the Increment Value: "))
print("")
while a<b:
    print(a)
    a+=c

#while---arrange linewise

#break:
#stops the values at speicied place 
print("")
print("b) Break:") 
d=int(input("Enter the Initial Value: "))
e=int(input("Enter the Higher Limit: "))
f=int(input("Enter the Increment Value: "))
g=int(input("Enter the Break Value: "))
print("")
while d<e:
    print(d)
    if d==g:
        break
    d+=f
print("")

#Continue:
#used to skip the specified value
#initial value will not be displayed
#add the higher limit value to the list 
print("")
print("c) Continue:")
h=int(input("Enter the Initial value: "))
i=int(input("Enter the Higher Limit: "))
j=int(input("Enter the Increment Value: "))
k=int(input("Enter the Skip value: "))
print("")
while h<i:
    h+=j
    if h==k:
        continue
    print(h)
print("") 

#for loop:
print("")
print("2) For: ")
print("a)")
names=["a","b","c","d","e","f"]
print("")
print("Element is the list are:")
print("")

for l in names:
    print(l)
print("")

#for loop:
#break:
print("")
print("2) For: ")
print("a) Break: ")
names=["a","b","c","d","e","f"]
print("")
print(names)
m=input("Enter the Break Value: ")
for n in names:
    print(n)
    if n==m:
        break
print("")

#for loop:
#continue:
print("b) continue:")
print(names)
o=input("Enter the Skip Value: ")
for p in names:
    if p==o:
        continue
    print(p)

#increments in for loop:
#Syntax:
#range(start,end,step)
print("")
print("c) Increments using range:")
for q in range(5): #(0-4)
    print(q)
print("")

r=int(input("Enter the Initial digit (Numerical): "))
s=int(input("Enter the Final digit (Numerical): "))
t=int(input("Enter the Step digit (Numerical): "))
print("")

for u in range(r,s,t):
    print(u)
print("")

#odd or even using for, and, & if:

print("4) Odd or even:")
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

v=[]
w=[]

print("The Numbers in the List are")
print(nums)
print("")

for x in nums:
    print(x)
    if x%2==0:
        w.append(x)
    else:
        v.append(x)

print("")
print(f"Odd:{v}")
print(f"Even:{w}")
print("")