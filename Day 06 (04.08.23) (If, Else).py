print("")
name=input('Enter student name: ')
reg_nos=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110]
print("")

if type(name)==str:
    print("Proceed to next step")
    reg_no=int(input('Enter registration number: '))
    print("")
    
    if type(reg_no)==int and reg_no in reg_nos:
        print(f"Your name is {name}, and your reg no is {reg_no}")
    
    else:
        print("Check your input (Either [InputError] or [register number not found])")

else:
    print("Enter string only")