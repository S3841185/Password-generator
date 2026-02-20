import random
import string

def password_generator(pwd_len):

    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    special_chars = string.punctuation
    pwd = ""

    while len(pwd) < pwd_len:
        pwd += random.choice(upper_chars)
        pwd += random.choice(lower_chars)
        pwd += random.choice(special_chars)
        

    return pwd


def main():
    while True:
        print("\n================================")
        print("====== PASSWORD GENERATOR ======")
        print("================================")
        
        minimum_length = input("Enter the password length, minimum length is 12 : ")


        if minimum_length.isdigit() == False:
            print("Invalid Input, Try again.")
            continue


        length = int(minimum_length)


        if length >= 12:
            password = password_generator(length)
            print(f"Your generated password is: {password}\n")           
        
        if int(length) < 12:
            print("Password length is too low, try again.\n")               
            continue
    
        
main()


