password = "fight club"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    
    login = str(input("Enter your password: ")).casefold()
    print(login)
    if login == password:
        print("Access Granted")
        break 
        
    else:
        print("Access Denied, Try Again")
        attempts += 1
        if attempts == max_attempts:
            print("Too many attempts. Access Locked.")  
