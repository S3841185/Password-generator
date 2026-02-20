import random
import string


###### Creating the password generation function
def password_generator(pwd_len):

    ###### gets the characters to put in the password, see line 2, import string
    
    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    special_chars = string.punctuation
    
    pwd_chars = upper_chars + lower_chars + special_chars
    ###### empty password as the start, this is just a placeholder
    pwd = ""

    ###### generating the password itself, generating from a list of words in pwd_chars(line 14)
    while len(pwd) < pwd_len:
        pwd += random.choice(pwd_chars)

        
    ###### returns the password generated
    return pwd

###### Saving password to a file
def save_password(password_to_save):
   with open("Passwords.txt", "a+") as file_to_append:
    file_to_append.write(f"{password_to_save}, ")
    file_to_append.close()



###### the main program
def main():
    while True:
        print("\n================================")
        print("====== PASSWORD GENERATOR ======")
        print("================================")
        
        ###### asks the user to define the length of their password
        ###### good practice principles are employed here
        minimum_length = input("Enter the password length, minimum length is 12 : ")

        ###### input validataion, will only continue if the user input is an integer over 12 (see line 46-48)
        if minimum_length.isdigit() == False:
            print("Invalid Input, Try again.")
            continue

        length = int(minimum_length)

        ###### calls the pasword generator function if the user input is int 12 or over
        if length >= 12:
            password = password_generator(length)
            print(f"Your generated password is: {password}\n")
            
            save_password_choice = input("Would you like to save this password? (y/n) ").lower()
            
            while True:
                if save_password_choice == "y":
                    save_password(password)
                    break
                elif save_password_choice == "n":
                    print("Password Not Saved, Returning to menu")
                    break
                else:
                    print("Invalid Input, Try Again...")
                    save_password_choice = input("Would you like to save this password? (y/n) ").lower()
                

        ###### conditional statement, if the password length is under 12 characters, the program will ask the user to input another value
        if int(length) < 12:
            print("Password length is too low, try again.\n")               
            continue
    
        
main()


