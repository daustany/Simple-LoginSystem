import hashlib


class textColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def signup():
    print(textColors.OKBLUE + "\n\nNew user registration" + textColors.ENDC)
    firstName = input("Enter your First Name: ")
    lastName = input("Enter your Last Name: ")
    emailAddress = input("Enter your Email Address: ").lower()

    if (checkDuplication(emailAddress)):

        password = input("Enter your Password: ")
        confirm_password = input("Confirm your Password: ")

        if confirm_password == password:

            encoded_password = confirm_password.encode()
            hashed_password = hashlib.md5(encoded_password).hexdigest()

            with open("credentials.txt", "a") as credentialsFile:
                 credentialsFile.write(firstName + "|")
                 credentialsFile.write(lastName + "|")
                 credentialsFile.write(emailAddress + "|")
                 credentialsFile.write(hashed_password)
                 credentialsFile.write("\n")

            credentialsFile.close()

            print(textColors.OKGREEN + "\nYou have registered successfully!" + textColors.ENDC)

        else:
            print("Password is not same as above! \n")



def login():
    print(textColors.OKBLUE + "\n\nAuthentication" + textColors.ENDC)
    emailAddress = input("Enter your Email Address: ").lower()
    password = input("Enter your Password: ")

    encodedPassword = password.encode()
    password_hash = hashlib.md5(encodedPassword).hexdigest()

    with open("credentials.txt", "r") as credentialsFile:
        credentialsFile.seek(0)
        credentialsList = credentialsFile.read().split("\n")
    credentialsFile.close()
    

    for item in credentialsList:
        if(item != ""):
            user = item.split("|")

            if(user[2] == emailAddress and user[3] == password_hash):
                print(textColors.OKGREEN + "\nHello, " + user[0] + " " + user[1] + 
                                           " you have successfully logged in" + textColors.ENDC)
                break
            else:
                print(textColors.FAIL + "\nEntered username/password is incorrect!" + textColors.ENDC)
                break


def checkDuplication(emailAddress):
    with open("credentials.txt", "r") as credentialsFile:
        credentialsFile.seek(0)
        credentialsList = credentialsFile.read().split("\n")
    credentialsFile.close()
    

    for item in credentialsList:
        if(item != ""):
            user = item.split("|")

            if(user[2] == emailAddress):
                print(textColors.WARNING + "\n[" + user[2] + "] has taken, try another Email Address." + textColors.ENDC)
                return False
            else:
                return True



def clearDatabase():
    with open("credentials.txt", "w") as credentialsFile:
         credentialsFile.write("")
    credentialsFile.close()

    print(textColors.OKGREEN + "\nDatabase deleted successfully." + textColors.ENDC)



def showMenu():
    print(textColors.WARNING + 
          "\n------------------- Login System -------------------\n"
          "(1) Signup\n"
          "(2) Login\n"
          "(3) Clear Database !\n"
          "(4) Exit\n"
          "----------------------------------------------------"
           + textColors.ENDC)


print(textColors.UNDERLINE + "\nDefault User: m.daustany@gmail.com | password: 123" + textColors.ENDC)

while 1:
    showMenu()

    action = input("\nEnter your choice: ")

    if not action.isnumeric():
        print(textColors.FAIL + "\nI don't know how to do that!" + textColors.ENDC)
        continue

    if action == "1":
        signup()
    elif action == "2":
        login()
    elif action == "3":
        clearDatabase()
    elif action == "4":
        break
    else:
        print(textColors.FAIL + "\nWrong Choice!" + textColors.ENDC)


#Written by (Mehdi Daustany) at the request of the University of the Netherlands
#https://github.com/daustany/Simple-LoginSystem.git