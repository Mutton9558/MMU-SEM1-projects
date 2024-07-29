# *********************************************************
# Program: RuneOfMinigames.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TC1L/TL2L
# Trimester: 2410
# Name: SHAWN HUANG QI YANG
# ID: 241FC240CK
# Email: SHAWN.HUANG.QI@soffice.mmu.edu.my
# Phone: +60162510502
# *********************************************************

import random # library for random function (randomise numbers)
import numpy # require pip install https://numpy.org/install/
import os # file checking and also to clear terminal, learnt from https://www.w3schools.com/python/module_os.asp
from time import sleep # delay time, learnt time sleep from https://www.geeksforgeeks.org/python-time-module/

# Main function for the maze minigame
def maze():
    applePos = [(random.randint(1,2)), (random.randint(3,4)), (random.randint(5,6)), (random.randint(7,8)), (random.randint(9,10)), (random.randint(11,12)), (random.randint(13,15))] # randomises apple position
    game_end = False # initiate the variable for the loop
    appleCount = 0 # initialise the accumulator
    while not game_end: # loop condition
        if appleCount == 3: # ends the game as user has won
            text = """
You have obtained all 3 apples! Congrats
Using the 3 apples at your disposal, you used that treasure to summon...
The Eight-Handled Key Divergent Sila Divine General Apple

APPLE: Argh! Don't eat me pls I beg!

YOU: I'm not here to eat you bro you probably taste rotten.

APPLE: Ugh rude! Then why are you chasing me?

YOU: I need the key on your back...

APPLE: Oh... I see. You could've just said so.

YOU: bruh

The apple instantly hands you the key and shows you the way out. You then proceeded to walk towards the stairway.
And with that your journey is coming to a close...
"""
            for line in text:
                sleep(0.01)
                print(line, end="", flush=True)
            end()
            game_end = True
            break
        else:
            monsterPos = [(random.randint(1,5)), (random.randint(6,10)), (random.randint(11,15))] # randomises monster position
            orbPos = [(random.randint(1,5)), (random.randint(6,10)), (random.randint(11,15))] # randomises orb position
            print("\n-----------------------------------------------------------")
            print("That apple seems to have used a weird cloning technique. If you find 3 apples in the maze he will appear before you... Go get him!")
            print(f"You have {appleCount} apples")
            print("Choose a direction to go in this maze...\n")
            print("Left") 
            print("Center")
            print("Right")
            print("\n-----------------------------------------------------------")
            userChoice = input("\nWhere shall you go? (Left/Center/Right): \n")
            if userChoice.casefold() == "left": 
                playerPos = random.randint(1,5) # randomises user position if they chose left
                if playerPos in monsterPos: # brings user to game over screen when they encounter a monster
                    print("\nYou encountered a monster and died.")
                    gameOver()
                    game_end = True
                    break
                elif playerPos in orbPos: 
                    if appleCount > 0:
                        print("\nYou encountered a purple orb. Your -1 IQ brain thought it was an Apple and you touch it. You lose an apple.\n")
                        appleCount -= 1 # removes one apple from the accumulator
                    else: # nothing will happen if appleCount = 0
                        print("\nYou encountered a purple orb!")
                        print("You touched the weird orb but nothing happened.\n")
                elif playerPos in applePos: # adds one apple to the accumulator
                    appleCount += 1
            elif userChoice.casefold() == "center":
                playerPos = random.randint(6,10) # randomises user position if they chose center
                if playerPos in monsterPos: # brings user to game over screen when they encounter a monster
                    print("You encountered a monster and died.")
                    gameOver()
                    game_end = True
                    break
                elif playerPos in orbPos: 
                    if appleCount > 0:
                        print("You encountered a purple orb. Your -1 IQ brain thought it was an Apple and you touch it. You lose an apple.")
                        appleCount -= 1 # removes one apple from the accumulator
                    else:
                        print("\nYou encountered a purple orb!")
                        print("You touched the weird orb but nothing happened.") # nothing will happen if appleCount = 0
                elif playerPos in applePos: # adds one apple to the accumulator
                    appleCount += 1
            elif userChoice.casefold() == "right":
                playerPos = random.randint(11,15) # randomises user position if they chose right
                if playerPos in monsterPos: # brings user to game over screen when they encounter a monster
                    print("You encountered a monster and died.")
                    gameOver()
                    game_end = True 
                    break
                elif playerPos in orbPos: 
                    if appleCount > 0:
                        print("You encountered a purple orb. Your -1 IQ brain thought it was an Apple and you touch it. You lose an apple.")
                        appleCount -= 1 # removes one apple from the accumulator
                    else:
                        print("\nYou encountered a purple orb!")
                        print("You touched the weird orb but nothing happened.") # nothing will happen if appleCount = 0
                elif playerPos in applePos:
                    appleCount += 1
            else: # This will happen if a user does not give an expected input 
                print("You stood in place because you're illiterate and dyslexic. After a while, you encountered a monster")
                print("You were eaten alive")
                game_end = True
                gameOver()
                break
    return # ends function

def cupGame(): # function for the cup game
    # opening text
    # no. 1 is a lie
    text = """
MAGICIAN: The game is simple! In one of these 3 cups lies the key. I will tell you two truths and one lie as a clue.
MAGICIAN: Here, let's try a test run.
MAGICIAN: Here it goes!

-----------------------------------------------------------
Magician will tell you two truths and one lie regarding where the key is!
1. Key is on the left
2. Key is on the right
3. The first statement is a lie
-----------------------------------------------------------
"""
    for char in text:
        sleep(0.03)
        print(char, end="", flush=True)
    userChoice = input("\nMAGICIAN: Now where do you think the key is in? (Left/Right/Center): ") # accepts user input
    if userChoice.casefold() == "left":
        print("\nMAGICIAN: Wrong! Luckily this is a demo run.")
    elif userChoice.casefold() == "right":
        print("\nMAGICIAN: Correct!")
    elif userChoice.casefold() == "center":
        print("\nMAGICIAN: Wrong!")
    else:
        print("\nMAGICIAN: PLEASE PICK A CHOICE!") # brings users back if they didn't choose a valid option since it's the demo
        cupGame()
        return
    # no. 3 is a lie
    text = """
MAGICIAN: That is basically how the game is...Easy right? Alright now! Let's start getting serious!

-----------------------------------------------------------
Magician will tell you two truths and one lie regarding where the key is!
1. The key is either on the center or right
2. The key is NOT on the right
3. The key is ON the right
-----------------------------------------------------------
"""

    for char in text:
        sleep(0.03)
        print(char, end="", flush=True)
    userChoice2 = input("\nMAGICIAN: Now where do you think the key is in? (Left/Right/Center): ")
    if userChoice2.casefold() == "left":
        print("\nMAGICIAN: Wrong!")
        print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
        gameOver() # brings users to the game over screen if they chose the wrong option
        return
    elif userChoice2.casefold() == "right":
        print("\nMAGICIAN: Wrong!")
        print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
        gameOver() # brings users to the game over screen if they chose the wrong option
        return
    elif userChoice2.casefold() == "center":
        print("\nMAGICIAN: Correct!")
        # no.1 is a lie
        text = """
MAGICIAN: I lied, I never put the keys in any cup!

YOU: WHAT?! I lost 10000 aura because of that!

MAGICIAN: Haha, fine this time I'll be serious.
MAGICIAN: Ok, let's spice things up a bit!

-----------------------------------------------------------
Magician will tell you two truths and one lie regarding where the key is!
1. The key is NEITHER the left NOR center
2. The key is EITHER the right OR left
3. The key is NOT on the right. It may or may not be on the center
-----------------------------------------------------------
"""

        for char in text:
            sleep(0.03)
            print(char, end="", flush=True)
        userChoice3 = input("\nMAGICIAN: Now where do you think the key is in? (Left/Right/Center): ")
        if userChoice3.casefold() == "left":
            print("\nMAGICIAN: Correct!")
            # no.2 and 3 is a lie
            text = """
As he lifts up the cup, yet again there is no key.

YOU: When are you actually going to give me the key?

MAGICIAN: If you pass my final trial, then I will give you the key but be warned for I am now changing the rules!

YOU: Huh?

MAGICIAN: Instead of 2 truths and 1 lie how about 1 truth and 2 lies!

-----------------------------------------------------------
Uh oh Magician changed the rules, he will tell you 1 truth and 2 lies!
1. Key is NOT on the right
2. The key is NOT on the center
3. Key is on the left
-----------------------------------------------------------
"""
            for char in text:
                sleep(0.03)
                print(char, end="", flush=True)
            userChoice4 = input("\nMAGICIAN: Now where do you think the key is in? (Left/Right/Center): ")
            if userChoice4.casefold() == "left":
                print("\nMAGICIAN: Wrong!")
                print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
                gameOver() # brings users to the game over screen if they chose the wrong option
                return
            elif userChoice4.casefold() == "right":
                print("\nMAGICIAN: Wrong!")
                print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
                gameOver() # brings users to the game over screen if they chose the wrong option
                return
            elif userChoice4.casefold() == "center":
                print("\nMAGICIAN: Correct!")
                text = """
Alas, you have obtained the key to the stairway. Suddenly, the play area disappeared and so did the Magician.

YOU: What a peculiar individual, Giorno Giovanna, I will never forget you for as long as I live.
You head to the stairway and used the key. And just like that, you have beaten level 3. Good job.
Entering level 4...The last level.
-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
                for char in text:
                    sleep(0.03)
                    print(char, end="", flush=True)
                try:
                    userChoice = int(input("Choose a number (1/2): "))
                    if userChoice == 1:
                        fourthLevel() # proceed to next level if they win
                    elif userChoice == 2:
                        print("See you again some day...")
                        return
                    else:
                        print("\nChoose only either 1 or 2! Teleporting you in 3 seconds.")
                        sleep(3)
                        thirdLevel()
                except ValueError:
                    print("\nOnly an integer pls")
                    print("Bringing you back to the third level in 10 seconds")
                    sleep(10.0)
                    thirdLevel()
                except Exception as e:
                    print(f"\nAn error occured {e}")
                    print("Bringing you back to the third level in 10 seconds")
                    sleep(10.0)
                    thirdLevel()
            else:
                print("\nMAGICIAN: PLEASE PICK A CHOICE!")
                print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
                gameOver() # kills user for invalid input
                return
        elif userChoice3.casefold() == "right":
            print("\nMAGICIAN: Wrong!")
            print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
            gameOver() # brings users to the game over screen if they chose the wrong option
            return
        elif userChoice3.casefold() == "center":
            print("\nMAGICIAN: Wrong!")
            print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
            gameOver() # brings users to the game over screen if they chose the wrong option
        else:
            print("\nMAGICIAN: PLEASE PICK A CHOICE!")
            print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
            gameOver() # kills user for invalid input
            return
    else:
        print("\nMAGICIAN: PLEASE PICK A CHOICE!")
        print("MAGICIAN: Looks like the monsters are going to have a nice meal!")
        gameOver() # kills user for invalid input
        return
    return

# The connect 4 game was made following these two tutorials:
# https://www.youtube.com/watch?v=zD-Xuu_Jpe4&list=PLFCB5Dp81iNW19pnwTkOmRxc8CP4BSgr8&index=2
# https://www.youtube.com/watch?v=UYgyRArKDEs&list=PLFCB5Dp81iNW19pnwTkOmRxc8CP4BSgr8&index=1
# A lot of modification was done for example using numpy.full instead of zeros so that the map is not a bunch of 0s
# Function to print the map
def connect4createMap():
    board = numpy.full((6,7), '.')
    return board

# function to drop piece
def dropPiece(board, row, entry, piece):
    board[row][entry] = piece # replace the element at the specified row and column with the specified piece

def isValid(board, entry):
    return board[0][entry] == '.' # checks if the column is completely occupied or not

# it loops the entire column checking if it is empty or not, if it is that it will return the row
def getOpenRow(board, entry):
    for row in range(5, -1, -1):
        if board[row][entry] == '.':
            return row

def winConnect4(board, piece):
    # Checks horizontally for a win
    for i in range(4): # i is for column
        for j in range(6): # j is for row
            if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:
                return True
    # Checks vertically for a win
    for a in range(7): # a is for column
        for b in range(3): # b is for row
            if board[b][a] == piece and board[b+1][a] == piece and board[b+2][a] == piece and board[b+3][a] == piece:
                return True
    # Checks diagonally going down from the left
    for c in range(4): # c is for column
        for d in range(3): # d is for row
            if board[d][c] == piece and board[d+1][c+1] == piece and board[d+2][c+2] == piece and board[d+3][c+3] == piece:
                return True
    # Checks diagonally going down from the right
    for e in range(6, 2, -1): # e is for column
        for f in range(3): # f is for row
            if board[f][e] == piece and board[f+1][e-1] == piece and board[f+2][e-2] == piece and board[f+3][e-3] == piece:
                return True

#  Main connect 4 function
def connect4Main(): 
    print("\nIn The Coffee Code, Connect 4 is played as follows. The challenger, in this case you, plays it normally. Choose a tile and place your piece.")
    print("When 4 pieces line up you win. Easy right?")
    print("However, the challenged player, in this case, Monsieur Catterson, gets to place two pieces per turn.")
    print("And that is why he never loses. Break a leg!")
    board = connect4createMap() # initializes the board
    gameEnd = False # variable for loop
    print(board) # prints board
    while not gameEnd: # loop condition                                                                                                                                 
        userInput = int(input("Make a selection from 1 to 7: "))
        if userInput > 7 or userInput < 1: # if user does not input as expected
            print("\nMONSIEUR CATTERSON: Read the instructions Meow! *scratches you*")
            gameOver()
            return
        else:
            pass
        if isValid(board, userInput-1): # check if the column is filled or not
            row = getOpenRow(board, userInput-1)
            dropPiece(board, row, userInput-1, 'O')
            if winConnect4(board, 'O'): # check if the user got a 4 in a row, if so they win and game ends
                print(board)
                text = """
MONSIEUR CATTERSON: You beat me? Wow. That was unexpected, meow.
MONSIEUR CATTERSON: Fine meow, I'll let you go and head over to level 3. After all, it's been a long time since I was defeated.
MONSIEUR CATTERSON: Needless to say, I could feel your determination, meow.
MONSIEUR CATTERSON: But be careful, from here on out, I can't help you, meow.

YOU: Hah, don't you worry. I'm sure it will be fine. After all, throughout the dungeons and the bar, I alone am the honored one.

The cat, no longer able to stand the nonsense leaving your mouth, kicks you down the stairs.
Congratulations, you have passed Level 2. You are now entering Level 3...
-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
                for char in text:
                    sleep(0.01)
                    print(char, end="", flush=True)
                try:
                    userChoice = int(input("Choose a number (1/2): "))
                    if userChoice == 1:
                        thirdLevel() # proceed to level 3 if you win
                        gameEnd = True
                        break
                    elif userChoice == 2:
                        print("See you again some day...")
                        return
                    else:
                        print("\nChoose only either 1 or 2! Teleporting you in 3 seconds.")
                        sleep(3)
                        secondLevel()
                except ValueError:
                    print("\nOnly an integer pls")
                    print("Bringing you back to the second level in 10 seconds")
                    sleep(10.0)
                    secondLevel()
                except Exception as e:
                    print(f"\nAn error occured {e}")
                    print("Bringing you back to the second level in 10 seconds")
                    sleep(10.0)
                    secondLevel()
            botInput = random.randint(0,6) # randomises bot move
            if isValid(board, botInput): # check if column is occupied, if not
                row = getOpenRow(board, botInput) # designates the row
                dropPiece(board, row, botInput, 'X') # replaces the '.' at the row and column with X
            else: # if column is occupied
                while isValid(board, botInput) == False:
                    botInput = random.randint(0,6) # continuously randomises the bot input until it chooses a column not occupied
                    isValid(board, botInput) # calls function to return a boolean value, if still False the loop will continue
                row = getOpenRow(board, botInput)
                dropPiece(board, row, botInput, 'X') 
            botInput2 = random.randint(0,6) # bot has two moves, this is it's second move
            if isValid(board, botInput2): # check if column is occupied, if not
                row = getOpenRow(board, botInput2) # designates the row
                dropPiece(board, row, botInput2, 'X') # replaces the '.' at the row and column with X
            else: # if column is occupied
                while isValid(board, botInput2) == False:
                    botInput2 = random.randint(0,6) # continuously randomises the bot input until it chooses a column not occupied
                    isValid(board, botInput2) # calls function to return a boolean value, if still False the loop will continue
                row = getOpenRow(board, botInput2)
                dropPiece(board, row, botInput2, 'X') # replaces the '.' at the row and column with X
            if winConnect4(board, 'X'): # check if bot wins
                print(board)
                print("\nMONSIEUR CATTERSON: HAH Monsieur Catterson mantains his 20 year win streak yet again! Hey wait! Are you ok? Meow?")
                print("MONSIEUR CATTERSON: Don't tell me you died by losing in Connect 4? Lame meow.")
                gameOver()
                break
        else:
            print("\nColumn is occupied!")
        print(board)

def gameOver(): # what happens when a user dies
    print("Oops, you died.")
    print("Failure is merely the door to success, don't give up.")
    userChoice = input("Continue? (Y/N): ")
    if userChoice.capitalize() == "Y": # if user wishes to continue
        os.system('cls' if os.name == 'nt' else 'clear')
        startMenu()
        return
    elif userChoice.capitalize() == "N": # otherwise
        print("Goodbye.")
    else:
        print("Please only enter Y or N!")
        gameOver()
        return

def rpsRematch(): # second phase of the rock paper scissors game
    element = ["Papers", "Scissors", "Rock"] # array to store possible options
    print("\n-----------------------------------------------------------")
    print("\n COMPUTER demands a REMATCH!")
    print("1. Papers")
    print("2. Scissors")
    print("\n-----------------------------------------------------------")
    botInput = random.randint(1,3) # randomises bot's choice
    userInput = int(input("This seems quite challenging, choose wisely (1/2): "))
    if userInput < 1 or userInput > 2:
        print("\nCOMPUTER: Are you illiterate? Nah I'm killing you.")
        gameOver() # kills user for invalid input
        return
    elif userInput == botInput:
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: What?! We drew?! Again! This time I'll beat you!")
        rpsRematch() # restarts if you drew
        return
    elif (userInput == 1 and botInput == 2) or (userInput == 2 and botInput == 3):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: Hah! I beat you! Ok now die.")
        gameOver() # kills you if you lost
        return
    elif (userInput == 1 and botInput == 3) or (userInput == 2 and botInput == 1):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        text = """
COMPUTER: Your sigma aura is too strong! I admit defeat!

COMPUTER: Fine, I'll tell you. The way out... is to traverse all 4 levels of this dungeon.

COMPUTER: Right now you're at the first level, there are still three more to go. Head downwards to the next... but be warned.

COMPUTER: There exists monsters far more dangerous than I am there.

YOU: Do not worry, my aura is too strong for any monster! After all, I have 10 million power in Rise of Kingdoms.

COMPUTER: What nonsense are you spouting?! Leave now, I wish to be alone.
-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
        for char in text:
            sleep(0.01)
            print(char, end="", flush=True)
        try:
            userChoice = int(input("Choose a number (1/2): "))
            if userChoice == 1:
                secondLevel() # proceed to level 2 if you win
            elif userChoice == 2:
                print("See you again some day...")
                return
            else:
                print("\nChoose only either 1 or 2! Teleporting you in 3 seconds.")
                sleep(3)
                firstLevel()
        except ValueError:
            print("\nOnly an integer pls")
            print("Bringing you back to the first level in 10 seconds")
            sleep(10.0)
            firstLevel()
        except Exception as e:
            print(f"\nAn error occured {e}")
            print("Bringing you back to the first level in 10 seconds")
            sleep(10.0)
            firstLevel()
    return

def rockpapersscissors(): # first phase of rock papers scissors game
    element = ["Rock", "Paper", "Scissors"] # list containing possible choices
    print("\n-----------------------------------------------------------")
    print("\n COMPUTER challenges YOU to a Rock Papers Scissors Fight!")
    print("1. Rock")
    print("2. Papers")
    print("3. Scissors")
    print("\n-----------------------------------------------------------")
    botInput = random.randint(1,3) # randomises bot choice
    userInput = int(input("Choose a number from 1 to 3: "))
    if userInput < 1 or userInput > 3:
        print("\nCOMPUTER: Are you illiterate? Nah I'm killing you.")
        gameOver() # kills user for invalid input
        return
    elif (userInput == 1 and botInput == 2) or (userInput == 2 and botInput == 3) or (userInput == 3 and botInput == 1):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: Hah! I beat you! Ok now die.")
        gameOver() # kills user if they lose
        return
    elif userInput == botInput:
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: What?! We drew?! Again! This time I'll beat you!")
        rockpapersscissors() # restarts the game if user draws
        return
    elif (userInput == 1 and botInput == 3) or (userInput == 2 and botInput == 1) or (userInput == 3 and botInput == 1):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: I...lost? No this can't be!")
        print("\nYOU: Skill issue. Just get better.")
        print("\nCOMPUTER: I refuse! I demand a rematch and this time I'll be making sure you lose.")
        print("COMPUTER: Let's see how you play without being able to choose Rock")
        print("\nYOU: HUH?!")
        rpsRematch() # calls rematch function to go to phase 2
        return

# function to register new user
def register():
    if not os.path.exists("userInfo.txt"): # check if path does not exist
        with open("userInfo.txt", "x"):
            pass # creates new file if it does not exist
    with open("userInfo.txt", "r") as file: # opens the file "userInfo.txt" with read function only as variable file
        Username = input("Enter a Username: ")
        Password = input("Enter a Password: ")
        confirmPassword = input("Re-enter your password to confirm: ")
        user = []
        for i in file:
            i = i.split(", ") # splits each line into substrings
            user.append(i[0]) # appends the user data into array user (user data is the 0 index)

        if confirmPassword != Password: # checks if confirm password matches password
            print("Password does not match please try again!")
            register()
        else:
            if Username in user: # check if username already taken
                print("Username already exists!")
                register()
            elif len(Username) < 1 or len(Password) < 1: # check if there was input
                print("Invalid Username and Password")
                register()
            else:
                with open("userInfo.txt", "a") as file:
                    file.write(f"{Username}, {Password}\n") # appends the username and password into the text file
                    print(f"Successfully created User! Hello {Username}")
                userMenu()

# login function
def login():
    global Username
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    if not os.path.exists("userInfo.txt"): # checks if the file exists
        with open("userInfo.txt", "x"):
            pass # creates file if it doesn't exist
    with open("userInfo.txt", "r") as file: # opens userInfo.txt as a read-only file
        user = []
        userPassword = []
        for i in file:
            name,psword = i.split(", ") # splits each line into substring and stores them in name and psword
            user.append(name) # appends name into user list
            userPassword.append(psword) # appends psword into userPassword list
        data = dict(zip(user, userPassword)) # make them into values for a dictionary name data
        try:
            if data[Username]: # checks if there is a key with the Username in data
                try:
                    if Password in data[Username]: # check if the value of that key is the password
                        print("Login Success")
                        print(f"Welcome {Username}")
                        startMenu()
                        return
                    else:
                        print("Incorrect Password")
                        print("Try again")
                        login()
                except:
                    print("Incorrect Username or Password")
                    login()
            else:
                print("Username doesn't exist")
                userMenu()
        except:
            print("Username or Password does not exist")
            userMenu()

# menu for users to login or register account, the first screen they see
def userMenu():
    try:
        text = """
-----------------------------------------------------------

Welcome fallen warrior to Rune of Minigames!
1. Register new user
2. Log in into an existing account
3. Quit

-----------------------------------------------------------
"""
        print(text)
        userChoice = int(input("Enter a number to select your choice (1/2/3): "))
        if userChoice == 1:
            register()
        elif userChoice == 2:
            login()
        elif userChoice == 3:
            print("Quitting program...")
            return  # Exit the function to avoid further processing
        else:
            print("Enter 1,2 or 3 only!")
            userMenu()

    except:
        print("Please follow instructions.")
        userMenu()

# users can choose to load a level they have saved
def loadGame(Username):
    os.system('cls' if os.name == 'nt' else 'clear') # clears terminal
    if not os.path.exists("level.txt"): # check if level.txt exists or not
        print("You have not yet saved any level.") # output if the file does not exist
        startMenu()
        return

    user_data = {}
    with open("level.txt", "r") as file: # opens file
        for line in file:
            user, level = line.strip().split(", ") # splits each line into substring and stores them in user and level
            user_data[user] = level # assigns the value of user key as level

    try:
        if Username in user_data:
            user_level = user_data[Username] # assign user_level as the level saved by the user with username in Username variable
            if user_level == "intro":
                print("\nLoading intro level...")
                print("\n-----------------------------------------------------------")
                intro()
            elif user_level == "1":
                print("\nLoading level 1...")
                print("\n-----------------------------------------------------------")
                firstLevel()
            elif user_level == "2":
                print("\nLoading level 2...")
                print("\n-----------------------------------------------------------")
                secondLevel()
            elif user_level == "3":
                print("\nLoading level 3...")
                print("\n-----------------------------------------------------------")
                thirdLevel()
            elif user_level == "4":
                print("\nLoading level 4...")
                print("\n-----------------------------------------------------------")
                fourthLevel()
            else:
                print("No levels saved for this user.")
                startMenu()
        else:
            print("No levels saved for this user.")
            startMenu()
    except Exception as e:
        print(f"An error occurred: {e}")
        startMenu()

# save progress function that accepts level and Username as parameters
def save_progress(level, Username):
    if not os.path.exists("level.txt"):
        with open("level.txt", "x"):
            pass  # Create the file if it doesn't exist

    # Read existing data from the file
    user_level_data = []
    with open("level.txt", "r") as file:
        for line in file:
            user, user_level = line.strip().split(", ") # strips each line into two substrings and store their values in user and user_level
            user_level_data.append((user, user_level)) # append them as a tuple in user_level_data

    # Remove existing user data if it exists. List comprehension
    user_level_data = [(user, user_level) for user, user_level in user_level_data if user != Username]

    # Add the new user data
    user_level_data.append((Username, level))

    # Write the updated data back to the file
    with open("level.txt", "w") as file:
        for user, user_level in user_level_data:
            file.write(f"{user}, {user_level}\n")

    print("Successfully saved progress!")

# the end of the game
def end():
    sentence1 = "THE END"
    sentence2 = "Also I'm removing your safe progress now"
    print("You walk downwards anticipating a grand exit... to your disappointment, it was just an elevator going up."
      " To be fair, the way back to the surface is up so... it's pretty logical I guess."
      " As you exit, you can feel the fresh air against your frail body, adrenaline coursing through your veins."
      " Finally, you're free. Therefore, this journey has now come to an end. You finally bought your milk and returned home safely.\n")
    sleep(25.0)
    for char1 in sentence1:
        sleep(1.0)
        print(char1, end="", flush=True)
    print("\n")
    for char2 in sentence2:
        sleep(0.05)
        print(char2, end="", flush=True)
    if not os.path.exists("level.txt"):
        with open("level.txt", "x"):
            pass  # Create the file if it doesn't exist
    
    # This should delete user's current save file
    # Read existing data from the file
    user_level_data = []
    with open("level.txt", "r") as file:
        for line in file:
            user, user_level = line.strip().split(", ")
            user_level_data.append((user, user_level))

    # Remove existing user data if it exists. List comprehension
    user_level_data = [(user, user_level) for user, user_level in user_level_data if user != Username]

    # Write the updated data back to the file
    with open("level.txt", "w") as file:
        for user, user_level in user_level_data:
            file.write(f"{user}, {user_level}\n")
    print("Bringing you back to the start menu in 5 seconds!")
    sleep(5)
    startMenu()
    return

# function for the fourth level
def fourthLevel():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = """
-----------------------------------------------------------

1. Save Progress
2. Continue
3. Quit

-----------------------------------------------------------
"""
    print(text)
    userChoice = int(input("Choose an option wisely (1/2/3): "))
    try:
        if userChoice == 1: # when user chose 1
            save_progress("4", Username) # call the functions with these parameters
            text = """
-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
            print(text)
            userChoice2 = int(input("Choose a choice (1/2): "))
            try:
                if userChoice2 == 1: # when user chose 1
                    text = """
You can feel your heart beating with joy, the adrenaline rushes to your head knowing you are reaching the end.
As you step foot on the fourth level, a bright ray of light shines upon you.
You look around your surroundings, amazed. The environment is much different than the others.
While the others were dark and mossy, the walls of this level are shiny and clean, showing no signs of being abandoned whatsoever.

YOU: Did I die? Am I in Heaven?

My guy, heaven is in the clouds, not 10 feet under.
You walk across the shiny hallway until you hear a voice...

APPLE: Ahh! A giant!

You look down to see an apple screaming at you.

YOU: I've seen many weird things here, but a talking apple? Now that's TOO far-fetched!

APPLE: Don't eat me PLEASE!

YOU: I'm not going to eat you...

APPLE: You are, aren't you! They all do!

The apple starts running into what seems like a bush maze.
You then notice that there is a key stuck behind the apple. You quickly chase after the apple as fast as you can. But it is too late.
The apple is already in the maze...
"""
                    for char in text:
                        sleep(0.01)
                        print(char, end="", flush=True)
                    maze()
                    return
                elif userChoice2 == 2: # when user chose 2, quit
                    print("Quitting...")
                    return
                else:
                    print("1 or 2 Only! Bringing you back to the start in 5 seconds...")
                    sleep(5)
                    fourthLevel()
                    return
            except ValueError:
                print("Invalid input! Please enter an integer")
                sleep(3)
                fourthLevel()
                return
            except Exception as e:
                print(f"An error occurred: {e}.")
                sleep(3)
                fourthLevel()
                return
        elif userChoice == 2: # what happens when a user chose 2
            text = """
You can feel your heart beating with joy, the adrenaline rushes to your head knowing you are reaching the end.
As you step foot on the fourth level, a bright ray of light shines upon you.
You look around your surroundings, amazed. The environment is much different than the others.
While the others were dark and mossy, the walls of this level are shiny and clean, showing no signs of being abandoned whatsoever.

YOU: Did I die? Am I in Heaven?

My guy, heaven is in the clouds, not 10 feet under.
You walk across the shiny hallway until you hear a voice...

APPLE: Ahh! A giant!

You look down to see an apple screaming at you.

YOU: I've seen many weird things here, but a talking apple? Now that's TOO far-fetched!

APPLE: Don't eat me PLEASE!

YOU: I'm not going to eat you...

APPLE: You are, aren't you! They all do!

The apple starts running into what seems like a bush maze.
You then notice that there is a key stuck behind the apple. You quickly chase after the apple as fast as you can. But it is too late.
The apple is already in the maze...
"""
            for char in text:
                sleep(0.01)
                print(char, end="", flush=True)
            maze()
            return
        elif userChoice == 3: # stops the game when user chooses 3
            print("Your journey has stopped, but it has not yet end...")
            return
        else:
            print("1, 2 or 3 Only! Bringing you back to the start in 5 seconds...")
            sleep(5)
            fourthLevel()
            return
    except ValueError:
        print("Invalid input! Please enter an integer.")
        sleep(3)
        fourthLevel()
        return
    except Exception as e:
        print(f"An error occurred: {e}.")
        sleep(3)
        fourthLevel()
        return

# function of the third level
def thirdLevel():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = """
-----------------------------------------------------------

1. Save Progress
2. Continue
3. Quit

-----------------------------------------------------------
"""
    print(text)
    userChoice = int(input("Choose an option wisely (1/2/3): "))
    try:
        if userChoice == 1:
            save_progress("3", Username) # call the save_progress function with parameters 3 and user's username
            text = """
-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
            print(text)
            userChoice2 = int(input("Choose a choice (1/2): "))
            try:
                if userChoice2 == 1:
                    text = """
It seems the cat may have kicked you a little bit too hard as you fell straight down landing head first.

YOU: Ouch! Rude cat. Wears a suit but has no proper etiquette!
You continue walking. The environment has completely changed; it is full of concrete walls that are a little bit cracked.
Suddenly, you hear a sound behind you.

YOU: MONSTERRRRRRRRRRRRRRRRRRRRRRRRRR!!!
You start running as fast as you can.
You keep on running, not even paying attention to the mossy walls all around you.
CRASH!

YOU: AH!

MAGICIAN: Alakazam Alakazoo Wam wam with this treasure I summon, my hat!
And just like that, the monsters chasing you have disappeared...

YOU: Woah thank you, who are you?

MAGICIAN: My name is Giorno Giovanna but you can call me Magician.

YOU: Cool. Alright, I'll be heading off now.

MAGICIAN: Hey, wait a moment! Aren't you forgetting to repay me?

YOU: I got no cash sorry sir.
As you try walking away, the magician teleports you to a little play area.

YOU: Great, another minigame now, right?

MAGICIAN: You're right, hidden within these cups is the key to the stairs. If you can beat my little game here, I'll let you walk free.
However, if you lose, I'll just feed you back to the monsters.

YOU: Nothing comes free here huh?

MAGICIAN: Welcome to the True Man's World.
"""
                    for char in text:
                        sleep(0.01)
                        print(char, end="", flush=True)
                    cupGame()
                    return
                elif userChoice2 == 2:
                    print("Quitting...")
                    return
                else:
                    print("1 or 2 only! Restarting level 3 in 5 seconds")
                    sleep(5)
                    thirdLevel()
                    return
            except ValueError:
                print("Invalid input! Please enter a number.")
                sleep(3)
                thirdLevel()
                return
            except Exception as e:
                print(f"An error occurred: {e}.")
                sleep(3)
                thirdLevel()
                return
        elif userChoice == 2:
            text = """
It seems the cat may have kicked you a little bit too hard as you fell straight down landing head first.

YOU: Ouch! Rude cat. Wears a suit but has no proper etiquette!
You continue walking. The environment has completely changed; it is full of concrete walls that are a little bit cracked.
Suddenly, you hear a sound behind you.

YOU: MONSTERRRRRRRRRRRRRRRRRRRRRRRRRR!!!
You start running as fast as you can.
You keep on running, not even paying attention to the mossy walls all around you.
CRASH!

YOU: AH!

MAGICIAN: Alakazam Alakazoo Wam wam with this treasure I summon, my hat!
And just like that, the monsters chasing you have disappeared...

YOU: Woah thank you, who are you?

MAGICIAN: My name is Giorno Giovanna but you can call me Magician.

YOU: Cool. Alright, I'll be heading off now.

MAGICIAN: Hey, wait a moment! Aren't you forgetting to repay me?

YOU: I got no cash sorry sir.
As you try walking away, the magician teleports you to a little play area.

YOU: Great, another minigame now, right?

MAGICIAN: You're right, hidden within these cups is the key to the stairs. If you can beat my little game here, I'll let you walk free.
However, if you lose, I'll just feed you back to the monsters.

YOU: Nothing comes free here huh?

MAGICIAN: Welcome to the True Man's World.
"""
            for char in text:
                sleep(0.01)
                print(char, end="", flush=True)
            cupGame()
            return
        elif userChoice == 3:
            print("Your journey has stopped, but it has not yet end...")
            return
        else:
            print("1, 2 or 3 only! Restarting level 3 in 5 seconds")
            sleep(5)
            thirdLevel()
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        sleep(3)
        thirdLevel()
        return
    except Exception as e:
        print(f"An error occurred: {e}.")
        sleep(3)
        thirdLevel()
        return

def secondLevel():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = """
-----------------------------------------------------------

1. Save Progress
2. Continue
3. Quit

-----------------------------------------------------------
"""
    print(text)
    userChoice = int(input("Choose an option wisely (1/2/3): "))
    try:
        if userChoice == 1:
            save_progress("2", Username) # call the save_progress function with parameters 2 and user's username
            text = """
-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
            print(text)
            userChoice2 = int(input("Choose a choice (1/2): "))
            try:
                if userChoice2 == 1:
                    text = """
You mustered all your courage and headed down the long concrete and dark stairway, nervous of what lies ahead.
After what felt like an eternity, you finally stepped foot on Level 2. Be proud of yourself.
A long hallway awaits. It reeks of dead fish, which makes you choke for a moment.
As you continue walking, you stumble upon an area that looks like a bar.

YOU: Why would there be a bar here?

You asked that out loud as if I'd know either.
You enter the strange-looking bar and the strong smell of coffee hits your senses.
A refreshing new smell that you very much enjoy, after painstakingly enduring the fishy smell outside.
You take a deep breath after a long day.

MONSIEUR CATTERSON: Uh... are you just going to stand there? Meow.

You look beneath you only to see a cat in a suit.

YOU: A talking cat?!

MONSIEUR CATTERSON: What? Is it that surprising? Stop standing there; you're blocking the way. Come sit by the counter, Meow.

You and the cat sit by the counter and have a chat. You tell it why you're here and your encounter with the Computer.

MONSIEUR CATTERSON: That piece of metal junk isn't totally wrong, you know, Meow.
MONSIEUR CATTERSON: This bar was opened as a safe haven against the evil monsters outside, Meow.
MONSIEUR CATTERSON: Usually, I'd ask for a handsome payment to show you the way down to the next level, but you don't really have money now, do you Meow?
MONSIEUR CATTERSON: How about this? Beat me in Connect 4, and then we'll negotiate, Meow.

YOU: Connect 4? Piece of cake!

MONSIEUR CATTERSON: Don't be too overconfident. Connect 4 is played differently around these parts. I never lose Meow.

YOU: Huh??
"""
                    for char in text:
                        sleep(0.01)
                        print(char, end="", flush=True)
                    connect4Main()
                    return

                elif userChoice2 == 2:
                    print("Quitting...")
                    return
                else:
                    print("1 or 2 Only! Returning in 5 seconds")
                    sleep(5)
                    secondLevel()
                    return
            except ValueError:
                print("Invalid input! Please enter an integer...")
                sleep(3)
                secondLevel()
                return
            except Exception as e:
                print(f"An error occurred: {e}.")
                sleep(3)
                secondLevel()
                return
        elif userChoice == 2:
            text = """
You mustered all your courage and headed down the long concrete and dark stairway, nervous of what lies ahead.
After what felt like an eternity, you finally stepped foot on Level 2. Be proud of yourself.
A long hallway awaits. It reeks of dead fish, which makes you choke for a moment.
As you continue walking, you stumble upon an area that looks like a bar.

YOU: Why would there be a bar here?

You asked that out loud as if I'd know either.
You enter the strange-looking bar and the strong smell of coffee hits your senses.
A refreshing new smell that you very much enjoy, after painstakingly enduring the fishy smell outside.
You take a deep breath after a long day.

MONSIEUR CATTERSON: Uh... are you just going to stand there? Meow.

You look beneath you only to see a cat in a suit.

YOU: A talking cat?!

MONSIEUR CATTERSON: What? Is it that surprising? Stop standing there; you're blocking the way. Come sit by the counter, Meow.

You and the cat sit by the counter and have a chat. You tell it why you're here and your encounter with the Computer.

MONSIEUR CATTERSON: That piece of metal junk isn't totally wrong, you know, Meow.
MONSIEUR CATTERSON: This bar was opened as a safe haven against the evil monsters outside, Meow.
MONSIEUR CATTERSON: Usually, I'd ask for a handsome payment to show you the way down to the next level, but you don't really have money now, do you Meow?
MONSIEUR CATTERSON: How about this? Beat me in Connect 4, and then we'll negotiate, Meow.

YOU: Connect 4? Piece of cake!

MONSIEUR CATTERSON: Don't be too overconfident. Connect 4 is played differently around these parts. I never lose Meow.

YOU: Huh??
"""
            for char in text:
                sleep(0.01)
                print(char, end="", flush=True)
            connect4Main()
            return
        elif userChoice == 3:
            print("See you again one day...")
            return
        else:
            print("1, 2 or 3 Only! Returning in 5 seconds")
            sleep(5)
            secondLevel()
            return
    except ValueError:
        print("Invalid input! Please enter an integer...")
        sleep(3)
        secondLevel()
        return
    except Exception as e:
        print(f"An error occurred: {e}.")
        sleep(3)
        secondLevel()
        return

def firstLevel():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = """
All you could see was darkness as your body has been falling for who knows how long.

YOU: How long have I been falling for? I can quite literally watch the entire Mat Kilau movie on Netflix with how long I have been falling.

SPLASH
It seems that you have finally finished falling.

YOU: Ouch! Ugh... I'm wet all over. Like literally wet. And these are new designer clothes too.

YOU: Oh no, my Yeezy's bruh.

After you had finished sulking like a little baby, you decided to explore the abyss in front of you.

-----------------------------------------------------------

1. Save Progress
2. Continue
3. Quit

-----------------------------------------------------------
"""
    for char in text:
        sleep(0.01)
        print(char, end="", flush=True)
    userChoice = int(input("Enter a choice (1/2/3): ")) 
    try:
        if userChoice == 1:
            save_progress("1", Username) # call the save_progress function with parameters 1 and user's username
            text = """
-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
            print(text)
            try:
                userChoice2 = int(input("What will thy decide? (1/2): "))
                if userChoice2 == 1:
                    dialogue = """
As you continue walking, you hear the creaks of the floorboards beneath you and the steady drop of water falling from the ceiling. 
Suddenly, you bump into a large, metal object in front of you with a loud thud.

YOU: Ouch!

COMPUTER: Hmm? Who dares disturb me? Beep boop!

YOU: I'm sorry! I was just trying to find a way out.

COMPUTER: I know the way out, but since you rudely bumped into me, I won't tell you!

YOU: Please! I'd do anything! *whimpers and cries*

COMPUTER: Really? Then challenge me to a game of rock-paper-scissors and I'll tell you!

YOU: Really? Rock-paper-scissors?

COMPUTER: Yeah, I've never played it before and I always wanted to, so come on...let's fight! But I will warn you, as the apex of all digital systems, there's no way I'm going down!
"""
                    for char in dialogue:
                        sleep(0.01)
                        print(char, end="", flush=True)
                    rockpapersscissors()
                elif userChoice2 == 2:
                    print("Quitting...")
                    return
                else:
                    print("1 or 2 only! Going back to start...")
                    sleep(5)
                    firstLevel()
            except ValueError:
                print("Invalid input! Please enter an integer...")
                sleep(3)
                firstLevel()
                return
            except Exception as e:
                print(f"An error occurred: {e}.")
                sleep(3)
                firstLevel()
                return
        elif userChoice == 3:
            print("Quitting...")
            return
        elif userChoice == 2:
            dialogue = """
As you continue walking, you hear the creaks of the floorboards beneath you and the steady drop of water falling from the ceiling. 
Suddenly, you bump into a large, metal object in front of you with a loud thud.

YOU: Ouch!

COMPUTER: Hmm? Who dares disturb me? Beep boop!

YOU: I'm sorry! I was just trying to find a way out.

COMPUTER: I know the way out, but since you rudely bumped into me, I won't tell you!

YOU: Please! I'd do anything! *whimpers and cries*

COMPUTER: Really? Then challenge me to a game of rock-paper-scissors, if you win I'll tell you!

YOU: Really? Rock-paper-scissors?

COMPUTER: Yeah, I've never played it before and I always wanted to, so come on...let's fight! But I will warn you, as the apex of all digital systems, there's no way I'm going down!
"""
            for char in dialogue:
                sleep(0.01)
                print(char, end="", flush=True)
            rockpapersscissors()
        else:
            print("Enter 1, 2, or 3 only! Commencing return in 5 seconds")
            sleep(5)
            firstLevel()
            return
        return
    except ValueError:
        print("Invalid input! Please enter an integer...")
        sleep(3)
        firstLevel()
        return
    except Exception as e:
        print(f"An error occurred: {e}.")
        sleep(3)
        firstLevel()
        return

def intro():
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal
    text = """
In a land far, far away... lived one humble guy in a cottage.

YOU: What a sunny day today... perhaps I should go out for a stroll.

-----------------------------------------------------------

1. Save Progress
2. Continue
3. Quit

-----------------------------------------------------------
"""
    print(text)
    userChoice = int(input("Enter a choice (1/2/3): "))

    if userChoice == 1:
        save_progress("intro", Username) # call the save_progress function with parameters intro and user's username
        print("\n-----------------------------------------------------------")
        print("\n1. Continue?")
        print("2. Quit")
        print("\n-----------------------------------------------------------")
        try:
            userChoice2 = int(input("Pick one quick: "))
            if userChoice2 == 1:
                text = """
You walk outside your humble abode and decide that today... you will buy milk.

YOU: Ugh... life is so boring. Perhaps I should take another route to spice things up a bit.

Normally, you would take the established and more common route, but today you decide to go off-course through uncharted areas. Along the way, you stumble across a strange looking well.

YOU: Huh? What a strange looking well... Perhaps I should see how deep it goes.

Unfortunately for you, the wind was rather strong and since your BMI was severely underweight... you fell into the well.

YOU: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

And thus began your journey...

-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
                for char in text:
                    sleep(0.01)
                    print(char, end="", flush=True)
                userChoice2 = int(input("Enter a choice (1/2): "))
                if userChoice2 == 1:
                    firstLevel()
                    return
                elif userChoice2 == 2:
                    print("Bye bye")
                    return
                else:
                    print('Enter 1 or 2 only!!! Awaiting return...')
                    sleep(3)
                    intro()
                    return
            elif userChoice2 == 2:
                print("Quitting...")
                return
            else:
                print("Invalid choice. Awaiting return...")
                sleep(3)
                intro()
        except:
            print("Invalid choice. Awaiting return...")
            sleep(3)
            intro()
    elif userChoice == 3:
        print("Quitting...")
        return
    elif userChoice == 2:
        text = """
You walk outside your humble abode and decide that today... you will buy milk.

YOU: Ugh... life is so boring. Perhaps I should take another route to spice things up a bit.

Normally, you would take the established and more common route, but today you decide to go off-course through uncharted areas. Along the way, you stumble across a strange looking well.

YOU: Huh? What a strange looking well... Perhaps I should see how deep it goes.

Unfortunately for you, the wind was rather strong and since your BMI was severely underweight... you fell into the well.

YOU: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

And thus began your journey...

-----------------------------------------------------------

1. Continue?
2. Quit

-----------------------------------------------------------
"""
        for char in text:
            sleep(0.01)
            print(char, end="", flush=True)
        userChoice3 = int(input("Enter a choice (1/2):"))
        if userChoice3 == 1:
            firstLevel()
            return
        elif userChoice3 == 2:
            print("Bye bye")
            return
        else:
            print('Enter 1 or 2 only!!! Awaiting return...')
            sleep(3)
            intro()
            return
    else:
        print("Enter 1, 2, or 3 only! Awaiting return...")
        sleep(3)
        intro()
        return

# function for the menu after user menu
def startMenu():
    global Username
    text = """
-----------------------------------------------------------

Begin your journey now!
1. New Game
2. Load an existing game.
3. Log Out

-----------------------------------------------------------
"""
    print(text)
    userChoice = int(input("Enter a number to select your choice (1/2/3): "))
    try:
        if userChoice == 1:
            if not os.path.exists("level.txt"):
                with open("level.txt", "x"):
                    pass  # Create the file if it doesn't exist
            
            # clear any existing save file with the same username as current user if they chose for new game
            # Read existing data from the file
            user_level_data = []
            with open("level.txt", "r") as file:
                for line in file:
                    user, level = line.strip().split(", ")
                    user_level_data.append((user, level))
                    
            user_level_data = [(user, level) for user, level in user_level_data if user != Username]

                # Add the new user data
            with open("level.txt", "w") as file:
                for user, user_level in user_level_data:
                    file.write(f"{user}, {user_level}\n")   
            intro()
        elif userChoice == 2:
            loadGame(Username)
        elif userChoice == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            userMenu()
        else:
            print("Enter 1,2 or 3 only! Bringing you back to the start in 10 seconds")
            sleep(10)
            startMenu()
    except:
        print("Invalid input. Returning in 10 seconds")
        sleep(10)
        startMenu()

# Main function
def main():
    userMenu()

# Run the main function
if __name__ == "__main__":
    main()
