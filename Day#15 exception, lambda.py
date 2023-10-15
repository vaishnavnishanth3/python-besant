#try:
#   actual code
#except:
#   error message
#finally:
#   message

print("")
print("Exceptionals:")
try:
    age=int(input("Enter your age:"))
    print(age)
except:
    print("input:'number';inputerror")
finally:
    print("your code is always checked")

#except Exception as kumar:
#print(str(kumar)):

print("")
try:
    age1=int(input("Enter your age: "))
    print(age)
except Exception as kumar:
    print(str(kumar))
finally:
    print("Wrong")

print("")
print("Multiple Exceptions: ")
#handling multiple exceptions:
try:
    age3=int(input("Enter your age: "))
    print(f"age is {age}")

except ValueError:
    print("This is value error")

except NameError:
    print("This is name error")

except Exception as e:
    print(str(e))

#normal functions:
print("")
print("Normal Functions: ")
a=int(input("Enter your age:"))
b=int(input("Enter your age:"))
c=int(input("Enter your age:"))
x=a+b+c
print(x)
print("")

#Lambda Function:
print("Lambda Functions:")
y=lambda a,b,c:a+b+c
print(y(1,2,3))