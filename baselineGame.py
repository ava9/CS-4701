from random import randint

# setup game board
myBoard = []
AIBoard = []

def createBoard(n, arr):
	for i in range(n):
		arr.append(["0"] * n)
	return arr

# print game board
def printBoard(board):
	for r in board:
		print " ".join(r)

# get random row

# get random column

# create ship location

# place ships on board

# check if guess is a hit or miss

# update guess on board

# start and play game
n = raw_input("Enter the value for n (where the game board dimenstions are  n x n: ")
myBoard = createBoard(int(n), myBoard)
AIBoard = createBoard(int(n), AIBoard)
print("my board is this: \n")
printBoard(myBoard)
print("\n")
print("AI board is this: \n")
printBoard(AIBoard)

# check if game is won or lost