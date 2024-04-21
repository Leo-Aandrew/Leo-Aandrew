import random
import string
def random_password(length, name):
   
    if length < 8:
        length = 8
    
 
    password = name
    
 
    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
 
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

name = input("Enter your preferred character/number/symbol to be in the password: ")
password_length = int(input("Enter the minimum length of the password (minimum 8 characters): "))

print("Your random password based on your input is:", random_password(password_length, name))
