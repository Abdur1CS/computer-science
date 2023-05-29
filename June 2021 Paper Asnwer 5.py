


def displayMenu():
     # Completed subprogram that displays the menu
    
    print("                  Menu                    ")
    print("------------------------------------------")
    print("[1] Add player name")
    print("[2] Play guess the capital city")
    print("[3] End game")
    print("------------------------------------------")

def getMenuChoice():
    # Completed subprogram that gets and validates the menu choice
    choices = [1,2,3]
    mChoice = 0
    # Menu choice is validated
    while mChoice not in choices:
        mChoice = int(input("Input your menu choice: "))

    # Valid menu option returned to the main menu
    return mChoice
     
def addPlayerName():
    global playerName
    # Add your code to:
    #   ensure a player name is input
    #   return the player name to the main menu
    playerName = str(input("enter ur name: "))
    
    return playerName




def guessCapital():
    global score
    
    # Partially completed subprogram to:
    #   display questions
    #   check guesses
    #   return final score
    
    # Arrays holding question numbers, countries and their capital cities
    questions = [1,2,3,4,5,6,7,8,9]
    countries = ["England","France","Spain","Italy","Germany","Scotland","Wales","United Arab Emirates","China"]
    capitals = ["London","Paris","Madrid","Rome","Berlin","Edinburgh","Cardiff","Abu Dhabi","Beijing"]
    numberDoneList = []

    questionCount = 1
    questionScore = 0

    # Add your code here
    for x in range(5):
        print(numberDoneList)
        askQ  = int(input("what question number do u want to do 1-9:  "))
        while askQ in numberDoneList:
            askQ  = int(input("do not repeat,  what question number do u want to do 1-9:  "))
        numberDoneList.append(askQ)
        print(countries[askQ-1])
        asnwer = str(input("what is the capital of this country:  "))
        if asnwer ==  capitals[askQ-1]:
            print("you got it right Good job +1 score")
            score = score + 1
        else:
            print(f"you got it wrong, the answer {capitals[askQ-1]}")     










    
    return 

menuChoice = 0
score = 0
playerName = ""

while menuChoice != 3:
    displayMenu()
    menuChoice = getMenuChoice()
    if  menuChoice == 1:
        print("1")
        addPlayerName()
    elif  menuChoice == 2:
        print("2")
        guessCapital()    
    else:
        print(f"{playerName} has gotten {score}")    
    # Add your code to:
    #   call the relevant subprogram if the menu choice is 1 or 2
    #   display the player name and the score if the menu choice is 3


