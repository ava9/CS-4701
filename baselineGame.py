from random import randint

myBoard = []
AIBoard = []

# setup game board
def createBoard(n, arr):
	for i in range(n):
		arr.append(["*"] * n)
	return arr

# print game board
def printBoard(board):
	for r in board:
		print " ".join(r)

# update game board
def updateBoard(board, (row, col), charac):
	board[row - 1][col - 1] = charac
	return board

# get game board character/square
def getBoardChar(board, (row, col)):
	return board[row - 1][col - 1]

# get random row
def randRow(board):
	return randint(0, len(board) - 1)

# get random column
def randCol(board):
	return randint(0, len(board[0]) - 1)

# is valid ship location
def isValidShip(row, col, direc, n, shipType):
	# add duplicate ship check
	if direc == "u":
		if row - (shipType - 1) >= 1:
			return True
		else:
			return False
	elif direc == "d":
		if row + (shipType - 1) <= n:
			return True
		else:
			return False
	elif direc == "l":
		if col - (shipType - 1) >= 1:
			return True
		else:
			return False
	elif direc == "r":
		if col + (shipType - 1) <= n:
			return True
		else:
			return False
	else:
		return False
	return False

# get ship coordinates
def getShipCoord(row, col, direc, n, shipType):
	if shipType == 2:
		if direc == "u":
			return [(row, col), (row - 1, col)]
		elif direc == "d":
			return [(row, col), (row + 1, col)]
		elif direc == "l":
			return [(row, col), (row, col - 1)]
		elif direc == "r":
			return [(row, col), (row, col + 1)]
		else:
			return []
	elif shipType == 3:
		if direc == "u":
			return [(row, col), (row - 1, col), (row - 2, col)]
		elif direc == "d":
			return [(row, col), (row + 1, col), (row + 2, col)]
		elif direc == "l":
			return [(row, col), (row, col - 1), (row, col - 2)]
		elif direc == "r":
			return [(row, col), (row, col + 1), (row, col + 2)]
		else:
			return []
	elif shipType == 4:
		if direc == "u":
			return [(row, col), (row - 1, col), (row - 2, col), (row - 3, col)]
		elif direc == "d":
			return [(row, col), (row + 1, col), (row + 2, col), (row + 3, col)]
		elif direc == "l":
			return [(row, col), (row, col - 1), (row, col - 2), (row, col - 3)]
		elif direc == "r":
			return [(row, col), (row, col + 1), (row, col + 2), (row, col + 3)]
		else:
			return []
	elif shipType == 5:
		if direc == "u":
			return [(row, col), (row - 1, col), (row - 2, col), (row - 3, col), (row - 4, col)]
		elif direc == "d":
			return [(row, col), (row + 1, col), (row + 2, col), (row + 3, col), (row + 4, col)]
		elif direc == "l":
			return [(row, col), (row, col - 1), (row, col - 2), (row, col - 3), (row, col - 4)]
		elif direc == "r":
			return [(row, col), (row, col + 1), (row, col + 2), (row, col + 3), (row, col + 4)]
		else:
			return []
	else:
		return []
	return []

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
	n = raw_input("Enter the value for 5 <= n <= 15 (where the game board dimenstions are  n x n):  \n")
	if n.isdigit() and (int(n) >= 5) and (int(n) <= 15):
		n = int(n)
		break
	else:
		print "Invalid input. Please only enter an integer n where 5 <= n <= 15  \n"

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
loop2 = True
while(loop2):
	while(True):
		twoShipRow = raw_input("Enter the starting row for your 2 ship (between 1 and "+str(n)+"): \n")
		if twoShipRow.isdigit() and (int(twoShipRow) >= 1) and (int(twoShipRow) <= n):
			twoShipRow = int(twoShipRow)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	twoShipCol = 0
	while(True):
		twoShipCol = raw_input("Enter the starting column for your 2 ship (between 1 and "+str(n)+"): \n")
		if twoShipCol.isdigit() and (int(twoShipCol) >= 1) and (int(twoShipCol) <= n):
			twoShipCol = int(twoShipCol)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	twoShipDir = "u"
	while(True):
		twoShipDir = raw_input("Enter the direction for your 2 ship to face from your starting square (u, d, l, r - which represent up, down, left, right): \n")
		if twoShipDir == "u" or twoShipDir == "d" or twoShipDir == "l" or twoShipDir == "r":
			break
		else:
			print "Invalid input. Please only enter an direction (u, d, l, r) which represent up, down, left, right: \n"
	loop2 = not isValidShip(twoShipRow, twoShipCol, twoShipDir, n, 2)
	if loop2 == True:
		print "Invalid input. Ship coordinates are out of bounds and ship cannot be placed on board: \n"
twoShipCoord = getShipCoord(twoShipRow, twoShipCol, twoShipDir, n, 2)
myBoard = updateBoard(myBoard, twoShipCoord[0], "2")
myBoard = updateBoard(myBoard, twoShipCoord[1], "2")
print("my board is this: \n")
printBoard(myBoard)

# user places 3 ship
print("You will now be prompted to enter the starting row, column, and direction of your 3 ship: \n")
threeShipRow = 0
loop3 = True
while(loop3):
	while(True):
		threeShipRow = raw_input("Enter the starting row for your 3 ship (between 1 and "+str(n)+"): \n")
		if threeShipRow.isdigit() and (int(threeShipRow) >= 1) and (int(threeShipRow) <= n):
			threeShipRow = int(threeShipRow)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	threeShipCol = 0
	while(True):
		threeShipCol = raw_input("Enter the starting column for your 3 ship (between 1 and "+str(n)+"): \n")
		if threeShipCol.isdigit() and (int(threeShipCol) >= 1) and (int(threeShipCol) <= n):
			threeShipCol = int(threeShipCol)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	threeShipDir = "u"
	while(True):
		threeShipDir = raw_input("Enter the direction for your 3 ship to face from your starting square (u, d, l, r - which represent up, down, left, right): \n")
		if threeShipDir == "u" or threeShipDir == "d" or threeShipDir == "l" or threeShipDir == "r":
			break
		else:
			print "Invalid input. Please only enter an direction (u, d, l, r) which represent up, down, left, right: \n"
	loop3 = not isValidShip(threeShipRow, threeShipCol, threeShipDir, n, 3)
	if loop3 == True:
		print "Invalid input. Ship coordinates are out of bounds and ship cannot be placed on board: \n"
	threeShipCoord = getShipCoord(threeShipRow, threeShipCol, threeShipDir, n, 3)
	square = getBoardChar(myBoard, threeShipCoord[0])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop3 = True
	square = getBoardChar(myBoard, threeShipCoord[1])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop3 = True
	square = getBoardChar(myBoard, threeShipCoord[2])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop3 = True
threeShipCoord = getShipCoord(threeShipRow, threeShipCol, threeShipDir, n, 3)
myBoard = updateBoard(myBoard, threeShipCoord[0], "3")
myBoard = updateBoard(myBoard, threeShipCoord[1], "3")
myBoard = updateBoard(myBoard, threeShipCoord[2], "3")
print("my board is this: \n")
printBoard(myBoard)

# user places 4 ship
print("You will now be prompted to enter the starting row, column, and direction of your 4 ship: \n")
fourShipRow = 0
loop4 = True
while (loop4):
	while(True):
		fourShipRow = raw_input("Enter the starting row for your 4 ship (between 1 and "+str(n)+"): \n")
		if fourShipRow.isdigit() and (int(fourShipRow) >= 1) and (int(fourShipRow) <= n):
			fourShipRow = int(fourShipRow)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	fourShipCol = 0
	while(True):
		fourShipCol = raw_input("Enter the starting column for your 4 ship (between 1 and "+str(n)+"): \n")
		if fourShipCol.isdigit() and (int(fourShipCol) >= 1) and (int(fourShipCol) <= n):
			fourShipCol = int(fourShipCol)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	fourShipDir = "u"
	while(True):
		fourShipDir = raw_input("Enter the direction for your 4 ship to face from your starting square (u, d, l, r - which represent up, down, left, right): \n")
		if fourShipDir == "u" or fourShipDir == "d" or fourShipDir == "l" or fourShipDir == "r":
			break
		else:
			print "Invalid input. Please only enter an direction (u, d, l, r) which represent up, down, left, right: \n"
	loop4 = not isValidShip(fourShipRow, fourShipCol, fourShipDir, n, 4)
	if loop4 == True:
		print "Invalid input. Ship coordinates are out of bounds and ship cannot be placed on board: \n"
	fourShipCoord = getShipCoord(fourShipRow, fourShipCol, fourShipDir, n, 4)
	square = getBoardChar(myBoard, fourShipCoord[0])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop4 = True
	square = getBoardChar(myBoard, fourShipCoord[1])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop4 = True
	square = getBoardChar(myBoard, fourShipCoord[2])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop4 = True
	square = getBoardChar(myBoard, fourShipCoord[3])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop4 = True
fourShipCoord = getShipCoord(fourShipRow, fourShipCol, fourShipDir, n, 4)
myBoard = updateBoard(myBoard, fourShipCoord[0], "4")
myBoard = updateBoard(myBoard, fourShipCoord[1], "4")
myBoard = updateBoard(myBoard, fourShipCoord[2], "4")
myBoard = updateBoard(myBoard, fourShipCoord[3], "4")
print("my board is this: \n")
printBoard(myBoard)

# user places 5 ship
print("You will now be prompted to enter the starting row, column, and direction of your 5 ship: \n")
fiveShipRow = 0
loop5 = True
while(loop5):
	while(True):
		fiveShipRow = raw_input("Enter the starting row for your 5 ship (between 1 and "+str(n)+"): \n")
		if fiveShipRow.isdigit() and (int(fiveShipRow) >= 1) and (int(fiveShipRow) <= n):
			fiveShipRow = int(fiveShipRow)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	fiveShipCol = 0
	while(True):
		fiveShipCol = raw_input("Enter the starting column for your 5 ship (between 1 and "+str(n)+"): \n")
		if fiveShipCol.isdigit() and (int(fiveShipCol) >= 1) and (int(fiveShipCol) <= n):
			fiveShipCol = int(fiveShipCol)
			break
		else:
			print "Invalid input. Please only enter an integer where the 1 <= integer <= "+str(n)+": \n"
	fiveShipDir = "u"
	while(True):
		fiveShipDir = raw_input("Enter the direction for your 5 ship to face from your starting square (u, d, l, r - which represent up, down, left, right): \n")
		if fiveShipDir == "u" or fiveShipDir == "d" or fiveShipDir == "l" or fiveShipDir == "r":
			break
		else:
			print "Invalid input. Please only enter an direction (u, d, l, r) which represent up, down, left, right: \n"
	loop5 = not isValidShip(fiveShipRow, fiveShipCol, fiveShipDir, n, 5)
	if loop5 == True:
		print "Invalid input. Ship coordinates are out of bounds and ship cannot be placed on board: \n"
	fiveShipCoord = getShipCoord(fiveShipRow, fiveShipCol, fiveShipDir, n, 5)
	square = getBoardChar(myBoard, fiveShipCoord[0])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop5 = True
	square = getBoardChar(myBoard, fiveShipCoord[1])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop5 = True
	square = getBoardChar(myBoard, fiveShipCoord[2])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop5 = True
	square = getBoardChar(myBoard, fiveShipCoord[3])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop5 = True
	square = getBoardChar(myBoard, fiveShipCoord[4])
	if square == "*":
		pass
	else:
		print "Invalid input. Ship coordinates overlap with previous ship on board, please re-enter ship coordinates \n"
		loop5 = True
fiveShipCoord = getShipCoord(fiveShipRow, fiveShipCol, fiveShipDir, n, 5)
myBoard = updateBoard(myBoard, fiveShipCoord[0], "5")
myBoard = updateBoard(myBoard, fiveShipCoord[1], "5")
myBoard = updateBoard(myBoard, fiveShipCoord[2], "5")
myBoard = updateBoard(myBoard, fiveShipCoord[3], "5")
myBoard = updateBoard(myBoard, fiveShipCoord[4], "5")

print("my board is this: \n")
printBoard(myBoard)
# check if game is won or lost