from random import randint

# setup game board
myBoard = []
AIBoard = []

def createBoard(n, arr):
	for i in range(n):
		arr.append(["*"] * n)
	return arr

# print game board
def printBoard(board):
	for r in board:
		print " ".join(r)

# get random row
def randRow(board):
	return randint(0, len(board) - 1)

# get random column
def randCol(board):
	return randint(0, len(board[0]) - 1)

# create ship locations
#def createShips:
	# 2 ship


# place ships on board

# check if guess is a hit or miss

# update guess on board

# start and play game

# enter n input
while(True):
	n = raw_input("Enter the value for n (where the game board dimenstions are  n x n: ")
	if n.isdigit():
		n = int(n)
		break
	else:
		print "Invalid input. Please only enter an integer"

#create and print boards
myBoard = createBoard(int(n), myBoard)
AIBoard = createBoard(int(n), AIBoard)
print("my board is this: \n")
printBoard(myBoard)
print("\n")
print("AI board is this: \n")
printBoard(AIBoard)

# check if game is won or lost