from string import ascii_letters, digits
from random import shuffle, choice


## characters to generate password from
characters = list(ascii_letters + digits + "!@#$%^&*()")

def get_pass():
	## length of password from the user
	length = int(input("Enter password length: "))

	## shuffling the characters
	shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(choice(characters))

	## shuffling the resultant password
	shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))




while True:
        get_pass()
        inp = input("do you want try again?(y/n)")
        if  inp == 'n' or inp == "N":
                break
        
