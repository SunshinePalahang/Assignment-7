#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid
while True:
    password = input("Create password: ")
    valid = False
    number = '0123456789'
    capital_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_char = '!@#$%^&*()-_+={[]}|\/:;"<>,.?'
    
    
    if not password in number:
        print("Not valid ! It should contain one letter between [1-9]")
        continue
    elif not password in capital_letter:
        print("Not valid ! It should contain one letter between [A-Z]")
        continue 
    elif not password in special_char:
        print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
        continue 
    else:
        valid=True
        break

if (valid):
    print("Valid")
   
