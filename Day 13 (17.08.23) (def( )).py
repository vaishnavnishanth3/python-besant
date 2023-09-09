print("")
print("Calculator Application:")

def calculator():
    print("")
    operand=input("Choose [ + | - | * | / | % | e | log | antilog | powers | roots ] (further operations will be added soon)\nEnter the Operation: ")
    print("")
    ops=["+","-","*","/","e","log","antilog","powers","roots"]

    if operand not in ops:
        print("")
        print('Invalid operation')
        
    elif operand=="e":
        coefficient=int(input("Enter the Coefficient Value: "))
        power=int(input("Enter the Power Value: "))
        operation=coefficient*(10**power)
        operation_string_e=str(coefficient)+"e"+str(power)
        print("")
        print(operation_string_e+" "+"=",operation)

    elif operand=="log":
        coefficient=int(input('Enter the Co-effieicent Value: '))
        base=int(input("Enter the Base Value: "))
        start=1
        end=coefficient*10
        for log in range(start,end):
            if base**log==coefficient:
                break
        
        operation_string_log="log"+"("+str(base)+")"+str(coefficient)
        if base**log==coefficient:
            print(operation_string_log,"=",log)

    elif operand=="antilog":
        base=int(input("Enter the Base value: "))
        power=int(input("Enter the Power value: "))
        antilog=base**power
        operation_string_antilog="Antilog("+str(base)+")"+str(power)
        print(operation_string_antilog+"=",antilog)

    elif operand=="roots":
        base=int(input("Enter the base value: "))
        root=int(input("Enter the nthroot value: "))
        operation=base**(1/root)
        operation_string_root=str(base)+"**"+"1/"+str(root)
        print(operation_string_root," ","="," ",operation)

    elif operand=="powers":
        base=int(input("Enter the base value:"))
        power=int(input("Enter the power value:"))
        operation=base**power 
        operation_string_powers=str(base)+"**"+str(power)
        print(operation_string_powers," ","=",operation)
                 
    else:
        first_num=float(input("Enter the First Number: "))
        print("")

        second_num=float(input("Enter the Second Number: "))
        operation_string=str(first_num)+" "+'('+operand+')'+" "+str(second_num)

        if operand=="+":
            operation=first_num+second_num
            print("")
            print(operation_string+" "+"=",operation)

        elif operand=="-":
            operation=first_num-second_num
            print("")
            print(operation_string+" "+"=",operation)

        elif operand=="*":
            operation=first_num*second_num
            print("")
            print(operation_string+" "+"=",operation)

        elif operand=="/":
            operation=first_num/second_num
            print("")
            print(operation_string+" "+"=",operation)

        elif operand=="%":
            operation=first_num%second_num
            print("")
            print(operation_string+" "+"=",operation)

    print("")
    print("Choose: [Continue|Exit]")
    print("On Option, type Continue to use the calculator again & type Exit to exit the application")
    print("")

    option=input("Enter your option: ")
    if option=="Continue" or option =="continue":
        print("")
        print("Values reset.")
        print("Continue!!!")
        calculator()
    elif option=="Exit" or option=="exit":
        print("")
        print("Thanks for using this Application!!!")
    else:
        print("")
        print("Invalid option (Auto Exiting>>>)")
calculator()
