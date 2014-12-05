#!/usr/bin/env python

board = {}
winner = False
playeroneturn = True

for i in range(1,11):
    board[i]=i

def printdict(board):
   s = ""
   for i in range(1,10):
       s += str(board[i]) + "|"
       if i%3 == 0:
           s+="\n"
   print s

def printturn(playeroneturn):
    if playeroneturn == True:
        print ("Player One, it's your turn.")
    else:
        print ("Player Two, it's your turn.")

printdict(board)
playerone = True
playeronetype = raw_input("You are player 1, would you like to be X or 0? ")
print playeronetype
while playeronetype not in('X', '0'):
    playeronetype = raw_input("Please try again, would you like to be X or 0? ")
if playeronetype == "X":
    playertwotype ="0"
    print "Player 2 is 0"
else:
    playertwotype = "X"
    print "Player 2 is X"
while winner == False:
    printdict(board)
    printturn(playeroneturn)
    choice = raw_input("Please make a move: ")
    choice = int(choice)
    if playeroneturn == True: 
        board[choice] = playeronetype
    else:
        board[choice] = playertwotype
    playeroneturn= not playeroneturn


