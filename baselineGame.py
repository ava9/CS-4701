from random import randint

#NOTES:
#n is referenced in some functions where it's not an input, need to create global variable???

myBoard = []
AIBoard = []

lasthit = -1 #0 if last hit sunk a ship, or no hits yet; otherwise num hits so far on this ship
up = -1 #direction we are pursuing the current kill; 0 if last hti sunk a ship, or no hits yet
down = -1
left = -1
right = -1
startcoords = [-1,-1]
latestcoords = [-1,-1]
killing = 0

shots = [0,0,0,0,0,0] #ignore first two entries, last 4 are hits on two-ship, three-ship, four-ship, five-ship

# setup game board
def createBoard(n, arr):
    for i in range(n):
        arr.append(["*"] * n)
    return arr

# print game board
def printBoard(board):
    for r in board:
        print " ".join(r)
    print "\n"

def isWin(board):
    count = 0
    for row in range(n):
        for col in range(n):
            if board[row][col] == "2" or board[row][col] == "3" or board[row][col] == "4" or board[row][col] == "5":
                count = count + 1
            else:
                pass
    if count > 0:
        return False
    else:
        return True
    return False

# didnt work, updated the ai board for some reason
#def maskBoard(board):
#    temp = board
#    for row in range(n):
#        for col in range(n):
#            if temp[row][col] == "2" or temp[row][col] == "3" or temp[row][col] == "4" or temp[row][col] == "5":
#                temp[row][col] = "*"
#            else:
#                pass
#    return (board, temp)

# update game board
def updateBoard(board, (row, col), charac):
    board[row - 1][col - 1] = charac
    return board

# get game board character/square
def getBoardChar(board, (row, col)):
    return board[row - 1][col - 1]

# get random row
def randRow(board):
    return randint(1, len(board))

# get random column
def randCol(board):
    return randint(1, len(board[0]))

# get random direction
def randDir():
    r = randint(0, 3)
    if r == 0:
        return "u"
    elif r == 1:
        return "d"
    elif r == 2:
        return "l"
    elif r ==3:
        return "r"
    else:
        return "u"
    return "u"

# dont cheat ????
def AIMove():
    # simple random implementation for now, need to improve
    AIloop = True
    global lasthit, up, down, left, right, startcoords, latestcoords, killing
    global shots

    breakyes = False

    while AIloop:
        #1) finish a kill
        #2) find new target
        if lasthit == -1: #seeking new target
            #for i in range(len(myBoard)):
            highest = 1 #at least one ship because or else game would have been won
            for row in range(len(myBoard)):
                for col in range(len(myBoard)):
                    #print ("HERE I AMMMMMMM ONe")
                    if (myBoard[row][col] != "*") and (myBoard[row][col] != "M") and (myBoard[row][col] != "H") and int(myBoard[row][col]) > highest:
                        #print ("HERE I AMMMMMMM Two")
                        highest = int(myBoard[row][col])
                        #print (lowest)
            #go across all rows
            #if there is interval of length lowest or bigger, choose lowest-th from left            
            count = 0
            for row in range(len(myBoard)):
                for col in range(len(myBoard)):
                    if (not myBoard[row][col] == "H") and (not myBoard[row][col] == "M"):
                        count = count + 1
                        if count == highest:
                            #print ("SEEK ROW")
                            if myBoard[row][col] == "*":
                                myBoard[row][col] = "M"
                                #AIloop = False
                                print("AI Missed ("+str(row+1)+", "+str(col+1)+")\n")
                                breakyes = True
                                break
                            else:
                                killing = int(myBoard[row][col])
                                shots[int(myBoard[row][col])] += 1
                                myBoard[row][col] = "H"
                                startcoords = [row, col]
                                latestcoords = [row, col]
                                lasthit = 1
                                
                                #AIloop = False
                                print("AI Hit ("+str(row+1)+", "+str(col+1)+")\n")
                                breakyes = True
                                break

                    else: #interval cut short
                        count = 0
                count = 0 #because end of column

                if breakyes == True:
                    #print "BREAK ROW 1"
                    break
            if breakyes == True:
                #print "BREAK ROW 2"
                break                         
    
            
            count = 0
            
            for col in range(len(myBoard)):
                for row in range(len(myBoard)):
                    if (not myBoard[row][col] == "H") and (not myBoard[row][col] == "M"):
                        count = count + 1
                        if count == highest:
                            #print ("SEEK COL")
                            if myBoard[row][col] == "*":
                                myBoard[row][col] = "M"
                                #AIloop = False
                                print("AI Missed ("+str(row+1)+", "+str(col+1)+")\n")
                                breakyes = True
                                break
                            else:
                                killing = int(myBoard[row][col])
                                shots[int(myBoard[row][col])] += 1
                                myBoard[row][col] = "H"
                                startcoords = [row, col]
                                latestcoords = [row, col]
                                lasthit = 1
                                #AIloop = False
                                print("AI Hit ("+str(row+1)+", "+str(col+1)+")\n")
                                breakyes = True
                                break


                    else: #interval cut short
                        count = 0
                count = 0 #because end of column
                
                if breakyes == True:
                    #print "BREAK COL 1"
                    break
            if breakyes == True:
                #print "BREAK COL 2"
                break                         

            count = 0            
            
            if count == 0:
                print("CORNER CASE")
            #CORNER CASE
                #print("ERROR ERROR ERROR did not find interval length highest")
                r = randRow(myBoard)
                c = randCol(myBoard)
                if myBoard[r-1][c-1] == "M" or myBoard[r-1][c-1] == "H":
                    AIloop = True
                else:
                    if myBoard[r-1][c-1] == "*":
                        myBoard[r-1][c-1] = "M"
                        AIloop = False
                        print("AI Missed ("+str(r)+", "+str(c)+")\n")
                    else:
                        num = int(myBoard[r-1][c-1])
                        myBoard[r-1][c-1] = "H"
                        AIloop = False
                        print("AI Hit ("+str(r)+", "+str(c)+")\n")
                        shots[num] += 1
                        if shots[num] == num:
                            lasthit = -1 #0 if last hit sunk a ship, or no hits yet; otherwise num hits so far on this ship
                            up = -1 #direction we are pursuing the current kill; 0 if last hti sunk a ship, or no hits yet
                            down = -1
                            left = -1
                            right = -1
                            startcoords = [-1,-1]
                            latestcoords = [-1,-1]
                            killing = 0


        #for ELSE, if you sink a ship, set up/down/eft/right all back to -1; set lasthit to -1, set startcoords and latestcoords to [-1,-1]
        else: #kill existing target
            #print ("HUNT")
            row = latestcoords[0]
            col = latestcoords[1]
            if latestcoords[0] != 0 and up != 0 and myBoard[row-1][col] != "M" and myBoard[row-1][col] != "H" and down!=1 and left!=1 and right!=1: 
            #not first row (top row)
                if myBoard[row-1][col] == "*":
                    myBoard[row-1][col] = "M"
                    if up==1:
                        down = 1
                    up = 0
                    latestcoords = startcoords
                    print("AI Missed ("+str(row)+", "+str(col+1)+")\n")
                    break
                else:
                    up = 1
                    num = int(myBoard[row-1][col])
                    myBoard[row-1][col] = "H"
                    latestcoords = [row-1, col]
                    lasthit = lasthit + 1
                    shots[num] += 1
                    
                    if num != killing:
                        latestcoords = startcoords
                        up=0
                        down = 1
                    
                    print("AI Hit ("+str(row)+", "+str(col+1)+")\n")
                    #if lasthit == killing:
                    if shots[num] == num:
                        lasthit = -1 #0 if last hit sunk a ship, or no hits yet; otherwise num hits so far on this ship
                        up = -1 #direction we are pursuing the current kill; 0 if last hti sunk a ship, or no hits yet
                        down = -1
                        left = -1
                        right = -1
                        startcoords = [-1,-1]
                        latestcoords = [-1,-1]
                        killing = 0

                    break
            if latestcoords[0] != len(myBoard)-1 and down != 0 and myBoard[row+1][col] != "M" and myBoard[row+1][col] != "H" and left!=1 and right!=1: 
            #not last row (bottom row)        
                if myBoard[row+1][col] == "*":
                    myBoard[row+1][col] = "M"
                    down = 0
                    latestcoords = startcoords
                    print("AI Missed ("+str(row+2)+", "+str(col+1)+")\n")
                    break
                else:
                    down = 1
                    num = int(myBoard[row+1][col])
                    myBoard[row+1][col] = "H"
                    latestcoords = [row+1, col]
                    lasthit = lasthit + 1
                    shots[num] += 1
                    
                    if num != killing:
                        latestcoords = startcoords
                        down = 0
                    
                    print("AI Hit ("+str(row+2)+", "+str(col+1)+")\n")
                    #if lasthit==killing:
                    if shots[num] == num:
                        lasthit = -1 #0 if last hit sunk a ship, or no hits yet; otherwise num hits so far on this ship
                        up = -1 #direction we are pursuing the current kill; 0 if last hti sunk a ship, or no hits yet
                        down = -1
                        left = -1
                        right = -1
                        startcoords = [-1,-1]
                        latestcoords = [-1,-1]
                        killing = 0
                    break
            if latestcoords[1] != 0 and left != 0 and myBoard[row][col-1] != "M" and myBoard[row][col-1] != "H" and right!=1: 
            #not first col (leftmost col)        
                if myBoard[row][col-1] == "*":
                    myBoard[row][col-1] = "M"
                    if left==1:
                        right = 1
                    left = 0
                    latestcoords = startcoords
                    print("AI Missed ("+str(row+1)+", "+str(col)+")\n")
                    break
                else:
                    left = 1
                    num = int(myBoard[row][col-1])
                    myBoard[row][col-1] = "H"
                    latestcoords = [row, col-1]
                    lasthit = lasthit + 1
                    shots[num] += 1
                    
                    if num != killing:
                        latestcoords = startcoords
                        left = 0
                        right = 1
                        
                    print("AI Hit ("+str(row+1)+", "+str(col)+")\n")
                    #if lasthit==killing:
                    if shots[num] == num:
                        lasthit = -1 #0 if last hit sunk a ship, or no hits yet; otherwise num hits so far on this ship
                        up = -1 #direction we are pursuing the current kill; 0 if last hti sunk a ship, or no hits yet
                        down = -1
                        left = -1
                        right = -1
                        startcoords = [-1,-1]
                        latestcoords = [-1,-1]
                        killing = 0
                    break
            if latestcoords[1] != len(myBoard)-1 and right != 0 and myBoard[row][col+1] != "M" and myBoard[row][col+1] != "H": 
            #not last col (rightmost col)        
                if myBoard[row][col+1] == "*":
                    myBoard[row][col+1] = "M"
                    right = 0
                    print("ERROR MUST GO RIGHT")
                    latestcoords = startcoords
                    print("AI Missed ("+str(row+1)+", "+str(col+2)+")\n")
                    break
                else:
                    num = int(myBoard[row][col+1])
                    myBoard[row][col+1] = "H"
                    latestcoords = [row, col+1]
                    lasthit = lasthit + 1
                    shots[num] += 1
                    
                    if num != killing:
                        latestcoords = startcoords
                    
                    print("AI Hit ("+str(row+1)+", "+str(col+2)+")\n")
                    #if lasthit==killing:
                    if shots[num] == num:
                        lasthit = -1 #0 if last hit sunk a ship, or no hits yet; otherwise num hits so far on this ship
                        up = -1 #direction we are pursuing the current kill; 0 if last hti sunk a ship, or no hits yet
                        down = -1
                        left = -1
                        right = -1
                        startcoords = [-1,-1]
                        latestcoords = [-1,-1]
                        killing = 0
                    break
            else:
                print("ERROR MUST GO RIGHT")        
                
        


        #adi's code
        #r = randRow(myBoard)
        #c = randCol(myBoard)
        #if myBoard[r-1][c-1] == "M" or myBoard[r-1][c-1] == "H":
        #    AIloop = True
        #else:
        #    if myBoard[r-1][c-1] == "*":
        #        myBoard[r-1][c-1] = "M"
        #        AIloop = False
        #        print("AI Missed ("+str(r)+", "+str(c)+")\n")
        #    else:
        #        myBoard[r-1][c-1] = "H"
        #        AIloop = False
        #        print("AI Hit ("+str(r)+", "+str(c)+")\n")


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

# create AI ship locations
def placeAIShips(board, n):
    # 2 ship
    loop2 = True
    while(loop2):
        r = randRow(board)
        c = randCol(board)
        d = randDir()
        if isValidShip(r, c, d, n, 2):
            coord2 = getShipCoord(r, c, d, n, 2)
            board = updateBoard(board, coord2[0], "2")
            board = updateBoard(board, coord2[1], "2")
            loop2 = False
        else: 
            loop2 = True

    # 3 ship
    loop3 = True
    while(loop3):
        r = randRow(board)
        c = randCol(board)
        d = randDir()
        if isValidShip(r, c, d, n, 3):
            coord3 = getShipCoord(r, c, d, n, 3)
            square0 = getBoardChar(board, coord3[0])
            square1 = getBoardChar(board, coord3[1])
            square2 = getBoardChar(board, coord3[2])
            if square0 == "*" and square1 == "*" and square2 == "*":
                board = updateBoard(board, coord3[0], "3")
                board = updateBoard(board, coord3[1], "3")
                board = updateBoard(board, coord3[2], "3")
                loop3 = False
            else:
                loop3 = True
        else: 
            loop3 = True

    # 4 ship
    loop4 = True
    while(loop4):
        r = randRow(board)
        c = randCol(board)
        d = randDir()
        if isValidShip(r, c, d, n, 4):
            coord4 = getShipCoord(r, c, d, n, 4)
            square0 = getBoardChar(board, coord4[0])
            square1 = getBoardChar(board, coord4[1])
            square2 = getBoardChar(board, coord4[2])
            square3 = getBoardChar(board, coord4[3])
            if square0 == "*" and square1 == "*" and square2 == "*" and square3 == "*":
                board = updateBoard(board, coord4[0], "4")
                board = updateBoard(board, coord4[1], "4")
                board = updateBoard(board, coord4[2], "4")
                board = updateBoard(board, coord4[3], "4")
                loop4 = False
            else:
                loop4 = True
        else: 
            loop4 = True

    # 5 ship
    loop5 = True
    while(loop5):
        r = randRow(board)
        c = randCol(board)
        d = randDir()
        if isValidShip(r, c, d, n, 5):
            coord5 = getShipCoord(r, c, d, n, 5)
            square0 = getBoardChar(board, coord5[0])
            square1 = getBoardChar(board, coord5[1])
            square2 = getBoardChar(board, coord5[2])
            square3 = getBoardChar(board, coord5[3])
            square4 = getBoardChar(board, coord5[4])
            if square0 == "*" and square1 == "*" and square2 == "*" and square3 == "*" and square4 == "*":
                board = updateBoard(board, coord5[0], "5")
                board = updateBoard(board, coord5[1], "5")
                board = updateBoard(board, coord5[2], "5")
                board = updateBoard(board, coord5[3], "5")
                board = updateBoard(board, coord5[4], "5")
                loop5 = False
            else:
                loop5 = True
        else: 
            loop5 = True
    return board




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
    else:
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
    else: 
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
    else:
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

AIBoard = placeAIShips(AIBoard, n)
print("AI board is this: \n")
printBoard(AIBoard)

while (not isWin(myBoard)) and (not isWin(AIBoard)):
    # Enter square to hit 
    userTargetRow = 0
    gameRow = True
    while(gameRow):
        userTargetRow = raw_input("Enter the row of the square to hit where 1 <= row <= "+str(n)+":  \n")
        if userTargetRow.isdigit() and (int(userTargetRow) >= 1) and (int(userTargetRow) <= n):
            userTargetRow = int(userTargetRow)
            gameRow = False
        else:
            print "Invalid input. Please only enter an interger row where 1 <= row <= "+str(n)+":  \n"
            gameRow = True

    userTargetCol = 0
    gameCol = True
    while(gameCol):
        userTargetCol = raw_input("Enter the row of the square to hit where 1 <= row <= "+str(n)+":  \n")
        if userTargetCol.isdigit() and (int(userTargetCol) >= 1) and (int(userTargetCol) <= n):
            userTargetCol = int(userTargetCol)
            gameCol = False
        else:
            print "Invalid input. Please only enter an interger row where 1 <= row <= "+str(n)+":  \n"
            gameCol = True
    square = getBoardChar(AIBoard, (userTargetRow, userTargetCol))
    if (square == "2" or square == "3" or square == "4" or square == "5"):
        AIBoard = updateBoard(AIBoard, (userTargetRow, userTargetCol), "H")
        print("You Hit ("+str(userTargetRow)+", "+str(userTargetCol)+")\n")
    else:
        AIBoard = updateBoard(AIBoard, (userTargetRow, userTargetCol), "M")
        print("You Missed ("+str(userTargetRow)+", "+str(userTargetCol)+")\n")
    print("AI board is this: \n")
    printBoard(AIBoard)

    AIMove()
    print("My board is this: \n")
    printBoard(myBoard)

if (isWin(myBoard)):
    print "AI WINS"
if (isWin(AIBoard)):
    print "YOU WIN"

# check if game is won or lost