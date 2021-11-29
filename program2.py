#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

import re

while True:
    password = input("Create password: ")
    validity = False
    if (len(password)<15 or len(password)> 30):
        print("Have at least 15 letters")
        continue
    elif not re.search("[A_Z]",password):
        print("Have at least one capital letter")
        continue
    elif not re.search("[0-9]",password):
        print("Have at least one number")
   
