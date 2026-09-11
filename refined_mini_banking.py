attempt = 0
max_attempt = 3
balance = 500.00
option = 0
withdraw = 0
isLogin = False

while attempt < max_attempt:
    pin = input("Enter Pin: ")

    if pin == "":
        print("pin cannot be empty")
    elif pin != "1234":
        print("Incorrect pin")
        attempt += 1
    else:
        print("welcome to your account")
        isLogin = True
        break
   
if(attempt == max_attempt):
    print("Too many attempts. Account lock")

while isLogin != False:
    print("=====BANKING MENU=====")  
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("")
    option = input("Enter an option: ")

    if option == "1":
        print(f"Your balance is: ${balance}")

    elif option == "2":
        deposit = float(input("Enter amount to deposit: "))
        if deposit < 100: print("deposit can't be less than 100")
        else:
            balance += deposit
        # balance = balance + deposit
        print("Deposit successful!")
        print(f"Your new balance is: ${balance}")

    elif option == "3":
        amount = float(input("Enter amount to be withdrawn: "))
        if amount > balance:
            print("insufficient funds")
        else:
            balance -= amount
            print("withdrawal successful!")
            print(f"Your new balance is: ${balance}")

    elif option == "4":
        print("logged out, bye!")
        isLogin = False

    else:
        print("Invalid option, try again")