import random

# get random card number
cardDraw = random.randrange(1,101)
# print(cardDraw) # only for testing purposes
# get random dice number
diceRoll = random.randrange(1,7)
# print(cardDraw)
# print(diceRoll)
# ask to input player's name
userName = str(input("What is your name?: "))
i = diceRoll
attempt = 0
num = 0
# start guessing
while i > 0:
    attempt += 1
    try:
        # get users guess
        num = int(input("Guess a number from 1 to 100. You have " + str(i) + " guess(es): "))
    except ValueError:
        # if input non-numerical, give player a message and go to next turn
        print("Your input is not a number!")
        i -= 1
        continue
    # if input is out of range, give player a message and go to next turn
    if num > 100 or num < 1:
        print("Your number is out of range!")
    # if input equals card number, give player a message and stop the game
    if num == cardDraw:
        print("Your guess is correct!")
        break
    # if input less than card number, give player a message and go to next turn
    elif num < cardDraw:
        print("Too low!")
    # if input higher than card number, give player a message and go to next turn
    elif num > cardDraw:
        print("Too high!")
    i -= 1

status = ""
# if last guess is not correct, give a message
if num != cardDraw:
    print("Sorry! You do not have any more guesses.")
    status = "lost"
# if last guess is correct, give a message
elif num == cardDraw:
    print("Congratulations!")
    status = "win"
# give message about how many guesses the player took
print("You have taken " + str(attempt) + " guess(es) and " + status + "!")

# prepare info to be written to the statistics.txt file
info = userName + " | " + status + " | " + str(attempt) + "\n"
# open statistics.txt file, whire the info about the last game, close the file
f = open("statistics.txt", "a")
f.write(info)
f.close()

with open("statistics.txt", "r") as fr:
    nameChar = 0
    statChar = 0
    # list all the previous players
    playerList = fr.read().splitlines()
    # get max number of characters in 1st and 2nd columns for better presentation
    for player in playerList:
        playerInfo = player.split(sep=" | ")
        if len(playerInfo[0]) > nameChar: nameChar = len(playerInfo[0])
        if len(playerInfo[1]) > statChar: statChar = len(playerInfo[1])
    # display information from statistics.txt file
    for player in playerList:
        playerInfo = player.split(sep=" | ")
        strOne = ""
        strTwo = ""
        i = nameChar - len(playerInfo[0])
        while i >0:
            strOne = strOne+" "
            i -=1
        i = statChar - len(playerInfo[1])
        while i >0:
            strTwo= strTwo+" "
            i -=1
        print(str(playerInfo[0])+strOne+" | "+str(playerInfo[1])+strTwo+" |  "+str(playerInfo[2]))
#the end


