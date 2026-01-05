# password checker

# password must contain 8 characters
# password must be hashed

import hashlib

def check_password(password):
    if len(password) < 8:
        raise Exception("Password must contain 8 characters")
    
    has_capital = False
    has_number = False
    has_special = False
    
    for ch in password:
        if ch.isupper():
            has_capital = True
        elif ch.isdigit():
            has_number = True
        elif not  ch.isalnum():
            has_special = True
        
    if  not (has_capital and has_number and has_special):
            raise Exception("Password must contain special, number and capital") 
        
        
    return True
    
    
def verify_password(password):
    while True:
        renter = input("Re-Enter the password: ")
        if password == renter:
            return "Password matched"
        else:
            print("Please enter in correctly")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    

password = input("Enter the password: ")

try:
    check_password(password)
    verify_password(password)
    hashed_password = hash_password(password)
    print("Password set Successfull !")
    print("Hashed password", hashed_password)
except Exception as e:
    print(f"Error : {e}")
    
    
       
    
    