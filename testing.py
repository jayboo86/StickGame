from this import d
import time,os,sys

# function to delay text on screen for output to player
def typingPrint(text):
    for char in text:
        time.sleep(0.05)
        print(char, end = '')

# function to delay text on screen when asking for input from player
def typingInput(text):
    for char in text:
        time.sleep(.05)
        print(char, end = '')
    value = input()
    return value

# function to clear the screen
def clearScreen():
    os.system("cls")

# Intro to the game
def introGame(typingPrint, clearScreen):
    clearScreen()
    typingPrint('HELLO WORLD!\n')
    time.sleep(1)
    typingPrint('.........\n')
    time.sleep(1)
    typingPrint('.........\n')
    time.sleep(1)
    print('')
    print('')
    time.sleep(1)
    typingPrint('Brought to you by........ Your Dad!\n')
    time.sleep(1)
    input('Press Enter to continue.')

# Return the players name
def nameReturn(typingPrint, clearScreen, username):
    typingPrint("Oh my! ")
    typingPrint(username) 
    typingPrint("! You say?\n")
    typingPrint("What a fantastic name!\n")
    time.sleep(3)
    typingPrint("...")
    clearScreen()

# Return the day of the week
def dayReturn(typingPrint, dOfWeek):
    if dOfWeek.lower() == ('sunday'):
        typingPrint("Oh good! I am glad to know it is only ")
        typingPrint(dOfWeek)
        typingPrint(". I still have time!!")

    elif dOfWeek.lower() == ('monday'):
        typingPrint("Well, I can handle it being ")
        typingPrint(dOfWeek)
        typingPrint(". I can still make it.")
    
    elif dOfWeek.lower() == ('tuesday'):
        typingPrint("Hmmm.. That is not leaving me much time..")

    elif dOfWeek.lower() == ('wednesday'):
        typingPrint(dOfWeek)
        typingPrint("Well... ")

    elif dOfWeek.lower() == ('thursday'):
        typingPrint(dOfWeek)

    elif dOfWeek.lower() == ('friday'):
        typingPrint(dOfWeek)

    elif dOfWeek.lower() == ('saturday'):
        typingPrint(dOfWeek)

    
    # typingPrint("No way! It is ")
    # typingPrint(dOfWeek)
    # typingPrint(" already?!")





introGame(typingPrint, clearScreen)
clearScreen()

typingPrint('Oh! Hello, I did not see you there. \n')
time.sleep(1)

# Ask the player their name 
username = typingInput("My name is Stick. What is your name?\n")
nameReturn(typingPrint, clearScreen, username)

# Ask the player what day it is
dOfWeek = typingInput("Say, would you happen to know what day of the week it is?\nI seem to have had some memory loss.\n")
print('\n')
print("1. Sunday\n")
print("2. Monday\n")
print("3. Tuesday\n")
print("4. Wednesday\n")
print("5. Thursday\n")


clearScreen()
dayReturn(typingPrint, dOfWeek)




