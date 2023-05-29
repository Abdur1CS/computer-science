# Q02a

# Initialise variables
password = "nX2934?"
username = "bard423"

# Print prompts, take and check input from user
while True:
    print("enter the username and password")
    ansPass = str(input("Password:"))
    ansUsr =  str(input("username:"))

    if ansPass == password and ansUsr  == username:
        print("WELCOME!!!")
        break 
    else:
        print("ERROR WRONG  PASSWORD AND USERNAME")


