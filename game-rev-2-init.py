# -*- coding: utf-8 -*-
##Currently this does not test for a duplicate score for the players.  Needs added.


# import the randint to generate random integers
from random import randint
# import a counter to test for a draw
from collections import Counter
# import for sys.exit()
import sys
 
# defining the function game()
def game():
    # set the dealer's random value
    dealer = randint(0, 10)
    # reset beginning count
    count = 0
    # we will call player outside of this function
    global player
    # testing for the numeric input
    while True:
        try:
            player = int(input("Please enter an integer between 0 and 10: \n"))
        except ValueError:
            print("\nYou must type a valid integer!  Try again.\n")
        else:
            break
    # this is where the player guesses
    while dealer != player:
        count += 1
        print(playerassignment+": "+str(player)+" \nby the way, this is try #"+str(count))
        if player < dealer:
            player = int(input("\nTry a greater number.\n")) 
        elif player > dealer:
            player = int(input("\nTry a smaller number.\n"))
    # when dealer=player, we continue
    finalcount = count + 1
    # print result
    print("That's right! "+playerassignment+"'s # of tries: "+str(finalcount))
    #we return the final value
    return finalcount


# we define the number of players and start calling the function game()

# let's test for a valid input
while True:
    try:
        players_amt = int(input("How many players will there be? \n"))
        if players_amt > 0:
            break
    except ValueError:
        print("\nYou must type a valid integer!  Try again.\n")
    else: 
        print("\nYou must have at least 1 player for this game.  Game Over!")
        sys.exit()   
# we will define our dictionary
# we are retaining name and score
dict = {}
# let's iterate through the number of players
for i in range(players_amt):
    global keyglobal 
    global playerassignment
    # we take names here
    playerassignment = input("\nWhat is your first name?\n")
    # testing for a valid alpha character string
    while playerassignment.isalpha() == False:
           print("\nYou must type a valid alpha character string!  Try again.\n")
           playerassignment = input("What is your first name?\n")
    # we define the key for the dict() to be the player's name
    key = playerassignment
    dict[key] = game()
    print("\n")
    # printing the player's name and score values to make it clear on the console
    print("\nPlayer and score - "+str(key)+" : "+str(dict.get(key)))
print("\n")
# to determine the winner, we simply take the minimum and declare through an 'if' test
min_score = min(dict.values())
min_player = min(dict, key=dict.get)
if min_score == 1:
    print("For the winner! Here is your name and score - "+str(min_player)+", with "+str(min_score)+" try!\n")
else:
    print("For the winner! Here is your name and score - "+str(min_player)+", with "+str(min_score)+" tries!\n")

# print each data item in the dictionary as a final output
for key, value in dict.items():
    print("Name: "+str(key), '   ' , "Score: "+str(value))
