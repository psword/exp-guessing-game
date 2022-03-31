from random import randint

# This game will only process two players.

def game():
    dealer = randint(0, 10)
    count = 0
    global playerassignment
    playerassignment = input("What is your first name?\n")
    global player
    player = int(input("Please enter an integer between 0 and 10: \n"))
    while dealer != player:
        count += 1
        print("Player 1: "+str(player)+" \nby the way, this is try #"+str(count))
        if player < dealer:
            player = int(input("\nTry a greater number.\n")) 
        elif player > dealer:
            player = int(input("\nTry a smaller number.\n"))
    finalcount = count + 1
    print("That's right! "+playerassignment+"'s # of tries: "+str(finalcount))
    return finalcount

#For Player 1
Player1=game()
player1name = str(playerassignment)
player1score = str(Player1)

print("\n")

#For Player 2
Player2=game()
player2name = str(playerassignment)
player2score = str(Player2)

print("\n")

if Player1 > Player2:
    print(str(player2name)+", you are the winner!")
elif Player2 > Player1:
    print(str(player1name)+", you are the winner!")
else: 
    print("The game is a draw! \nTry again!")
