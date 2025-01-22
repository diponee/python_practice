password = 1234
balance = 3000000
attempts = 0
max_attempts = 3

while True:
    
    print('Welcome to GoodNews ATM machine')
    pawd = int(input('Enter your password to continue:'))
    
    if pawd == password:
        print("Access Granted")
        
        print("Please choose a option")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Quit")
        option = int(input("Enter option: ")) 
        
        
        if option == 1:
            print(f"Your balance == {balance}")
        if option == 2:
            amt = int(input("Enter Amount: "))
            balance -= amt
            print("Withdraw successful!")
        if option == 3:
            amt = int(input("Enter Amount: "))
            balance += amt
            print("Deposit successful!")
        if option == 4:
            print("Thank you for banking with us.")
            break
            
    else:
        print("Unauthorized User, Try Again")
        max_attempts -= 1
        
        if max_attempts == 0:
            print("Too many attempts. Access Locked.")
            break
        
        

