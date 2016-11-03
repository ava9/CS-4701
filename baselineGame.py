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
n = 0
while(True):
	n = raw_input("Enter the value for 5 <= n <= 15 (where the game board dimenstions are  n x n): ")
	if n.isdigit() and (int(n) >= 5) and (int(n) <= 15):
		n = int(n)
		break
	else:
		print "Invalid input. Please only enter an integer n where 5 <= n <= 15"

#create and print boards
myBoard = createBoard(int(n), myBoard)
AIBoard = createBoard(int(n), AIBoard)
print("my board is this: \n")
printBoard(myBoard)
print("\n")
print("AI board is this: \n")
printBoard(AIBoard)

# user places 2 ship
print("You will now be prompted to enter the starting row, column, and direction of your 2 ship: \n")
twoShipRow = 0
while(True):
	twoShipRow = raw_input("Enter the starting row for your 2 ship (between 1 and "+str(n)+"): ")
	if twoShipRow.isdigit() and (int(twoShipRow) >= 1) and (int(twoShipRow) <= n):
		twoShipRow = int(twoShipRow)
		break
	else:
		print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": "
twoShipCol = 0
while(True):
	twoShipCol = raw_input("Enter the starting column for your 2 ship (between 1 and "+str(n)+"): ")
	if twoShipCol.isdigit() and (int(twoShipCol) >= 1) and (int(twoShipCol) <= n):
		twoShipCol = int(twoShipCol)
		break
	else:
		print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": "
twoShipDir = "u"
while(True):
	twoShipDir = raw_input("Enter the direction for your 2 ship to face from your starting square (u, d, l, r - which represent up, down, left, right): ")
	if twoShipDir == "u" or twoShipDir == "d" or twoShipDir == "l" or twoShipDir == "r":
		break
	else:
		print "Invalid input. Please only enter an direction (u, d, l, r) which represent up, down, left, right: "


# check if game is won or lost