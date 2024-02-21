
import string
import random
 
# Getting password length
length = int(input("Enter password length: "))
 
print('''Choose alphabets set for password from these : 
         1. Numbers
         2. Letters
         3. Symbols
         4. Exit''')
 
alphabetsList = ""
 
# Getting alphabets set for password    
while(True):
    option = int(input("Pick a number "))
    if(option == 1):
         
        # Adding letters to possible alphabets
        alphabetsList += string.ascii_letters
    elif(option == 2):
         
        # Adding Numbers to possible alphabets
        alphabetsList += string.digits
    elif(option == 3):
         
        # Adding symbols to possible
        # alphabets
        alphabetsList += string.punctuation
    elif(option == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    # Picking a random alphabets from our 
    # alphabets list
    randomchar = random.choice(alphabetsList)
     
    # appending a random alphabets to password
    password.append(randomchar)
 
# printing password as a string
print("The random password is " + "".join(password))
