#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

password = input("Create password: ")

number = '0123456789'
capital_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_char = '!@#$%^&*()-_+={[]}|\/:;"<>,.?'

for i in range(len(password)):
    if i in number:
        x=1
    