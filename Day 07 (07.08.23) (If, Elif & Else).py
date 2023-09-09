def vault1():
    secret_code=input("Enter the passcode: ")
    if secret_code=="4568":
        print("\n\tWelcome to Vault 1.0 \n")
        print("Now enter your vault number: ")
        print("Use 1--> to access vault items")
        print("Use 2--> to add items to vault")
        input_vault1=int(input("Enter your input: "))
        if input_vault1==1:
            print("Now open, you can now access the items.")
        elif input_vault1==2:
            number_of_items=int(input("Enter the number of items to be added: "))
            confirmation=int(input("Enter '1' to add or '2' to decline: "))
            if confirmation==1:
                print(f"Your {number_of_items} items has been added successfully")
            else:
                print("Addition request declined successfully")
    else:
        print("Invalid passcode")

def vault2():
    secret_code=input("Enter the passcode: ")
    if secret_code==9856:
        print("Now enter your vault number: ")
        print("This Vault has been locked due to security reasons. Contact admin to address the issue.")

vault_number=int(input("Enter your Vault number [1-2]: "))

if vault_number==1:
    print("Welcome to my bank account, have a nice day!")
    vault1()

elif vault_number==2:
    print("Welcome to my bank account, have a nice day!")
    vault2()