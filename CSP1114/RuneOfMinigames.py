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

import random
import numpy
import os

isLoggedIn = False

# Function to print the map
def connect4createMap():
    board = numpy.zeros((6,7))
    return board

def connect4Main():
    board = connect4createMap()
    gameOver = False
    
    while not gameOver:
        userInput = int(input("Make a selection from 0 to 6: "))
        botInput = random.randint(0,6)

def gameOver():
    print("Oops, you died.")
    print("Failure is merely the door to success, don't give up.")
    userChoice = input("Continue? (Y/N): ")
    if userChoice.capitalize() == "Y":
        print("It felt like it was just a dream...")
        startMenu()
    elif userChoice.capitalize() == "N":
        print("Goodbye.")
        return
    else:
        print("Please only enter Y or N!")
        gameOver()
    return

def rpsRematch():
    element = ["Papers", "Scissors", "Rock"]
    print("\n-----------------------------------------------------------")
    print("\n COMPUTER demands a REMATCH!")
    print("1. Papers")
    print("2. Scissors")
    print("\n-----------------------------------------------------------")
    botInput = random.randint(1,3)
    userInput = int(input("This seems quite challenging, choose wisely: "))
    if userInput < 1 or userInput > 2:
        print("\nCOMPUTER: Are you illiterate? Nah I'm killing you.")
        gameOver()
        return
    elif userInput == botInput:
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: What?! We drew?! Again! This time I'll beat you!")
        rpsRematch()
        return
    elif (userInput == 1 and botInput == 2) or (userInput == 2 and botInput == 3):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: Hah! I beat you! Ok now die.")
        gameOver()
        return
    elif (userInput == 1 and botInput == 3) or (userInput == 2 and botInput == 1):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nYou're sigma aura is too strong! I admit defeat!")

def rockpapersscissors():
    element = ["Rock", "Paper", "Scissors"]
    print("\n-----------------------------------------------------------")
    print("\n COMPUTER challenges YOU to a Rock Papers Scissors Fight!")
    print("1. Rock")
    print("2. Papers")
    print("3. Scissors")
    print("\n-----------------------------------------------------------")
    botInput = random.randint(1,3)
    userInput = int(input("Choose a number from 1 to 3: "))
    if userInput < 1 or userInput > 3:
        print("\nCOMPUTER: Are you illiterate? Nah I'm killing you.")
        gameOver()
        return
    elif (userInput == 1 and botInput == 2) or (userInput == 2 and botInput == 3) or (userInput == 3 and botInput == 1):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: Hah! I beat you! Ok now die.")
        gameOver()
        return
    elif userInput == botInput:
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: What?! We drew?! Again! This time I'll beat you!")
        rockpapersscissors()
        return
    elif (userInput == 1 and botInput == 3) or (userInput == 2 and botInput == 1) or (userInput == 3 and botInput == 1):
        print(f"You chose {element[userInput-1]}, COMPUTER chose {element[botInput-1]}")
        print("\nCOMPUTER: I...lost? No this can't be!")
        print("\nYOU: Skill issue. Just get better.")
        print("\nCOMPUTER: I refuse! I demand a rematch and this time I'll be making sure you lose.")
        print("COMPUTER: Let's see how you play without being able to choose Rock")
        print("\nYOU: HUH?!")
        rpsRematch()
        return

def register():
    if not os.path.exists("userInfo.txt"):
        f = open("userInfo.txt", "x")
    f = open("userInfo.txt", "r")
    Username = input("Enter a Username: ")
    Password = input("Enter a Password: ")
    confirmPassword = input("Re-enter your password to confirm: ")
    user = []
    userPassword = []
    for i in f:
        a,b = i.split(", ")
        user.append(a)
        userPassword.append(b)
    dict(zip(user, userPassword))

    if confirmPassword != Password:
        print("Password does not match please try again!")
        register()
    else:
        if Username in f:
            print("Username already exists!")
            register()
        elif len(Username) < 1 or len(Password) < 1:
            print("Invalid Username and Password")
            register()
        else:
            f = open("userInfo.txt", "a")
            f.write(f"{Username}, {Password}\n")
            f.close()
            print(f"Succefully created User! Hello {Username}")
            userMenu()

def login():
    global isLoggedIn
    global Username
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    if not os.path.exists("userInfo.txt"):
        f = open("userInfo.txt", "x")
    f = open("userInfo.txt", "r")
    user = []
    userPassword = []
    for i in f:
        a,b = i.split(", ")
        user.append(a)
        userPassword.append(b)
    data = dict(zip(user, userPassword))
    try:
        if data[Username]:
            try:
                if Password in data[Username]:
                    print("Login Success")
                    print(f"Welcome {Username}")
                    isLoggedIn = True
                    return isLoggedIn
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

def userMenu():
    try:
        print("\n-----------------------------------------------------------")
        print("\n Welcome Fallen Warrior to Rune of Minigames!")
        print("\n1. Register new user")
        print("2. Log in into an existing account")
        print("3. Quit")
        print("\n-----------------------------------------------------------")
        userChoice = int(input("Enter a number to select your choice: "))
        if userChoice == 1:
            register()
        elif userChoice == 2:
            login()
        elif userChoice == 3:
            print("Quitting program...")
            return  # Exit the function to avoid further processing
        else:
            print("Enter 1,2 or 3 only!")

    except:
        print("Please follow instructions.")

def loadGame():
    pass

def save_progress(level, Username):
    if not os.path.exists("level.txt"):
        with open("level.txt", "x"):
            pass  # Create the file if it doesn't exist

    # Read existing data from the file
    user_level_data = []
    with open("level.txt", "r") as f:
        for line in f:
            user, user_level = line.strip().split(", ")
            user_level_data.append((user, user_level))

    # Remove existing user data if it exists. List comprehension
    user_level_data = [(user, user_level) for user, user_level in user_level_data if user != Username]

    # Add the new user data
    user_level_data.append((Username, level))

    # Write the updated data back to the file
    with open("level.txt", "w") as f:
        for user, user_level in user_level_data:
            f.write(f"{user}, {user_level}\n")

    print("Successfully saved progress!")

def firstLevel():
    print("All you could see was darkness as your body has been falling for who knows how long.")
    print("\nYOU: How long have I been falling for? I can quite literally watch the entire Mat Kilau movie on Netflix with how long I have been falling.")
    print("SPLASH")
    print("It seems that you have finally finished falling.")
    print("\nYOU: Ouch! Ugh...I'm wet all over. Like literally wet. And these are new designer clothes too")
    print("\nYOU: Oh no my Yeezy's bruh.")
    print("After you had finished sulking like a little baby, you decided to explore the abyss in front of you.")
    print("\n-----------------------------------------------------------")
    print("\n1. Save Progress")
    print("2. Continue")
    print("3. Quit")
    print("\n-----------------------------------------------------------")
    userChoice = int(input("Enter a choice: ")) 

    if userChoice == 1:
        save_progress("1", Username)
        print("\n-----------------------------------------------------------")
        print("\n1. Continue?")
        print("2. Quit")
        print("\n-----------------------------------------------------------")
        try:
            userChoice2 = int(input("What will thy decide?: "))
            if userChoice2 == 1:
                print("As you continued walking, you could hear the creaks of the floor beneath you, water droplets falling from the ceiling.")
                print("Suddenly you have seemed to have bumped into a huge object that feels like metal in front of you.")
                print("\nYOU: Ouch!")
                print("\nCOMPUTER: Hmm? Who dares disturb me beep boop!")
                print("\nYOU: I'm sorry! I was just trying to find a way out.")
                print("\nCOMPUTER: Well I know the way out but since you rudely bumped into me I won't tell you!")
                print("\nYOU: Please! I'd do anything! *whimpers and cries compulsively or whatever*")
                print("\nCOMPUTER: Really? Then challenge me into a rock paper scissors game and then I'd tell you!")
                print("\nYOU: Really? Rock papers scissors?")
                print("\nCOMPUTER: Yeah, I've never played it before and I always wanted to so come on...let's fight!")
                print("\nCOMPUTER: But I will warn you, as the apex of all digital systems, there's no way I'm going down!")
                rockpapersscissors()
            elif userChoice2 == 2:
                print("Quitting...")
                return
            else:
                print("Invalid choice.")
        except:
            print("Invalid choice.")
    elif userChoice == 3:
        print("Quitting...")
        return
    elif userChoice > 3:
        print("Enter 1, 2, or 3 only!")
        return
    elif userChoice == 2:
        print("As you continued walking, you could hear the creaks of the floor beneath you, water droplets falling from the ceiling.")
        print("Suddenly you have seemed to have bumped into a huge object that feels like metal in front of you.")
        print("\nYOU: Ouch!")
        print("\nCOMPUTER: Hmm? Who dares disturb me beep boop!")
        print("\nYOU: I'm sorry! I was just trying to find a way out.")
        print("\nCOMPUTER: Well I know the way out but since you rudely bumped into me I won't tell you!")
        print("\nYOU: Please! I'd do anything! *whimpers and cries compulsively or whatever*")
        print("\nCOMPUTER: Really? Then challenge me into a rock paper scissors game and then I'd tell you!")
        print("\nYOU: Really? Rock papers scissors?")
        print("\nCOMPUTER: Yeah, I've never played it before and I always wanted to so come on...let's fight!")
        print("\nCOMPUTER: But I will warn you, as the apex of all digital systems, there's no way I'm going down!")
        rockpapersscissors()

def intro():
    print("\nIn a land far far away...lived one humble guy in a cottage.")
    print("\nYOU: What a sunny day today...perhaps I should go out for a stroll.")
    print("\n-----------------------------------------------------------")
    print("\n1. Save Progress")
    print("2. Continue")
    print("3. Quit")
    print("\n-----------------------------------------------------------")
    userChoice = int(input("Enter a choice: "))

    if userChoice == 1:
        save_progress("intro", Username)
        print("\n-----------------------------------------------------------")
        print("\n1. Continue?")
        print("2. Quit")
        print("\n-----------------------------------------------------------")
        try:
            userChoice2 = int(input("Pick one quick: "))
            if userChoice2 == 1:
                print("You walk outside your humble abode and decided that today...you will buy milk.")
                print("\nYOU: Ugh...life is so boring. Perhaps I should take another route to spice things up a bit.")
                print("Normally, you would take the established and more common route, but today you decided to go off-course through uncharted areas.")
                print("Along the way, you stumbled across a strange looking well.")
                print("\nYOU: Huh? What a strange looking well...Perhaps I should see how deep it goes.")
                print("Unfortunately for you, the wind was rather strong and since your BMI was severely underweight...you fell into the well.")
                print("\nYOU: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                print("And thus began your journey...")
                print("\n-----------------------------------------------------------")
                print("\n1. Continue?")
                print("2. Quit")
                print("\n-----------------------------------------------------------")
                userChoice2 = int(input("Enter a choice: "))
                if userChoice2 == 1:
                    firstLevel()
                    return
                elif userChoice2 == 2:
                    print("Bye bye")
                    return
                else:
                    print('Enter 1 or 2 only!!!')
                    return
            elif userChoice2 == 2:
                print("Quitting...")
                return
            else:
                print("Invalid choice.")
        except:
            print("Invalid choice.")
    elif userChoice == 3:
        print("Quitting...")
        return
    elif userChoice > 3:
        print("Enter 1, 2, or 3 only!")
        return
    else:
        print("You walk outside your humble abode and decided that today...you will buy milk.")
        print("\nYOU: Ugh...life is so boring. Perhaps I should take another route to spice things up a bit.")
        print("Normally, you would take the established and more common route, but today you decided to go off-course through uncharted areas.")
        print("Along the way, you stumbled across a strange looking well.")
        print("\nYOU: Huh? What a strange looking well...Perhaps I should see how deep it goes.")
        print("Unfortunately for you, the wind was rather strong and since your BMI was severely underweight...you fell into the well.")
        print("\nYOU: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        print("And thus began your journey...")
        print("\n-----------------------------------------------------------")
        print("\n1. Continue?")
        print("2. Quit")
        print("\n-----------------------------------------------------------")
        userChoice3 = int(input("Enter a choice: "))
        if userChoice3 == 1:
            firstLevel()
            return
        elif userChoice3 == 2:
            print("Bye bye")
            return
        else:
            print('Enter 1 or 2 only!!!')
            return

def startMenu():
    global isLoggedIn
    print("\n-----------------------------------------------------------")
    print("\n Begin your journey now!")
    print("\n1. New Game")
    print("2. Load an existing game.")
    print("3. Return")
    print("\n-----------------------------------------------------------")
    userChoice = int(input("Enter a number to select your choice: "))
    if userChoice == 1:
        intro()
    elif userChoice == 2:
        loadGame()
    elif userChoice == 3:
        isLoggedIn = False
        userMenu()
    else:
        print("Enter 1,2 or 3 only!")

# Main function
def main():
    userMenu()
    if isLoggedIn:
        startMenu()

# Run the main function
if __name__ == "__main__":
    main()
