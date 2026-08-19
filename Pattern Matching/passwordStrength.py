import re


passFlag = False

while(passFlag == False):
    print("A strong password contains at least 8 characters, both uppercase and lowercase characters, and at least one digit.\n")
    password = input("Enter your password: ")
    print("Testing password strength...")

    lowercaseMatch = re.compile(r'[a-z]')
    uppercaseMatch = re.compile(r'[A-Z]')
    digitMatch = re.compile(r'\d')

    lowercaseLetters = lowercaseMatch.findall(password)
    uppercaseLetters = uppercaseMatch.findall(password)
    digit = digitMatch.search(password)

    lengthCheck = len(password)
    lowCheck = (len(lowercaseLetters) > 0)
    upCheck = (len(uppercaseLetters) > 0)
    digitCheck = (digit != None)

    if (lengthCheck & lowCheck & upCheck & digitCheck):
        print("Password accepted")
        passFlag = True
    else:
        print("Password too weak, please try again")



