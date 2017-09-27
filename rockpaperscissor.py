player1 = input("Enter value at player 1 ")
player2 = input("Enter value at player 2 ")
if player1 == 'rock':
   if player2 == 'rock':
      print("TIE")
   elif player2 == 'paper':
      print("Player 2 wins")
   elif player2 == 'scissor':
      print("Player 1 wins")
elif player1 == 'paper':
   if player2 == 'scissor':
        print("TIE")
   elif player2 == 'rock':
        print("Player 2 wins")
   elif player2 == 'paper':
        print("PLayer 1 wins")
elif player1 == 'scissor':
	if player2 == 'scissor':
		print("TIE")
	elif player2 == 'rock':
		print("Player 2 wins")
	elif player2 == 'paper':
		print("Player 1 wins")
else:
    print("Wrong value entered")