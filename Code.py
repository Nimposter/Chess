## learn about FEN

Checkmate = False
Stalemate = False
WhiteMove = True

#initializes the board to starting position via an array
Board = [["r","n","b","q","k","b","n","r"],
        ["p" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["P" for _ in range(8)],
        ["R","N","B","Q","K","B","N","R"]]

#dictionary to convert chess coordinates to array indexes
Coordinates = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "1" : 7,
    "2" : 6,
    "3" : 5,
    "4" : 4,
    "5" : 3,
    "6" : 2,
    "7" : 1,
    "8" : 0
}

#defined function to print the board, uses nested loops, for ranks (rows) and files (columns)
def DisplayBoard():
    for rank in range(8):
        for file in range(8):
            print(Board[rank][file], end=" ")
        print()

def SlidingLegalMoves(f , r , piece):
    if piece == "q":
        directions = [(1,0) , (-1,0) , (0,1) , (0,-1) , (1, 1) , (1, -1) , (-1, 1) , (-1, -1)]
    elif piece == "r":
        directions = [(1,0) , (-1,0) , (0,1) , (0,-1)]
    elif piece == "b":
        directions = [(1, 1) , (1, -1) , (-1, 1) , (-1, -1)]
    Moves = []
    for x , y in directions:
        tempf = f
        tempr = r
        while True:
            tempf += x
            tempr += y
            if not OnBoard(tempf, tempr):
                break
            elif Board [tempr][tempf] != "*":
                if IsEnemy(tempf , tempr):
                    Moves.append(str(tempf) + str(tempr))
                break
            else:
                Moves.append(str(tempf) + str(tempr))
    return Moves

def KnightLegalMoves(f , r):
    relative_offset = [(+2, +1) , (+2, -1) , (-2, +1),
                      (-2, -1) , (+1, +2) , (+1, -2),
                      (-1, +2) , (-1, -2)]
    Moves = []
    for x , y in relative_offset:
        if OnBoard(f + x, r + y):
            if Board[r + y][f + x] == "*":
                Moves.append(str(f + x) + str(r + y))
            elif IsEnemy(f + x, r + y):
                Moves.append(str(f + x) + str(r + y))
    return Moves

def PawnLegalMoves(f , r):
    Moves = []
    if WhiteMove:
        if Board[r - 1][f] == "*":
            Moves.append(str(f) + str(r - 1))
            if r == 6 and Board[r - 2][f] == "*":
                Moves.append(str(f) + str(r - 2))
        if OnBoard(f - 1 , r - 1) and Board[r - 1][f - 1] != "*" and IsEnemy(f - 1 , r - 1):
            print("left capture")
            Moves.append(str(f - 1) + str(r - 1))
        if OnBoard(f + 1 , r - 1) and Board[r - 1][f + 1] != "*" and IsEnemy(f + 1 , r - 1):
            print("right capture")
            Moves.append(str(f + 1) + str(r - 1))
    else:
        if Board[r + 1][f] == "*":
            Moves.append(str(f) + str(r + 1))
            if r == 1 and Board[r + 2][f] == "*":
                Moves.append(str(f) + str(r + 2))
        if OnBoard(f - 1 , r + 1) and Board[r + 1][f - 1] != "*" and IsEnemy(f - 1 , r + 1):
            print("left capture")
            Moves.append(str(f - 1) + str(r + 1))
        if OnBoard(f + 1 , r + 1) and Board[r + 1][f + 1] != "*" and IsEnemy(f + 1 , r + 1):
            print("right capture")
            Moves.append(str(f + 1) + str(r + 1))
        
    return Moves

def GetMoves():
    #repeats until user has entered a valid move
    while True:
        
        #loops until user has selected their piece
        while True:
            #gets input for the square of the piece to move
            Coords = input("enter Coordinates of piece to be moved: ")
            source_file = Coordinates.get(Coords[0])
            source_rank = Coordinates.get(Coords[1])
            
            #checks user has selected their piece, not opponents or empty square
            if WhiteMove and Board[source_rank][source_file] == Board[source_rank][source_file].upper() != "*":
                break
            if not WhiteMove and Board[source_rank][source_file] == Board[source_rank][source_file].lower() != "*":
                break
            else:
                print("please select your own piece")
        
        print( "you have chosen",Board[source_rank][source_file])
        
        #determines what piece has been selected and calls the respective move generation function
        match Board[source_rank][source_file].lower():
                case "q" | "b" | "r":
                    LegalMoves = SlidingLegalMoves(source_file , source_rank , Board[source_rank][source_file].lower())
                case "n":
                    LegalMoves = KnightLegalMoves(source_file , source_rank)
                case "p":
                    LegalMoves = PawnLegalMoves(source_file , source_rank)
        
        print(LegalMoves)
        
        #gets input from user of square to move to
        Coords2 = input("enter Coordinates of square to move to: ")
        target_file = Coordinates.get(Coords2[0])
        target_rank = Coordinates.get(Coords2[1])
        
        #checks whether move user has entered is a legal move or not
        for i in LegalMoves:
            if i == str(target_file) + str(target_rank):
                #print("Legal Move")
                #if entered move is legal, it returns to the main program
                return source_rank,source_file,target_rank,target_file
        print("illegal move")

def OnBoard(f , r):
    return 0 <= f <= 7 and 0 <= r <= 7

def IsEnemy(f , r):
    if Board[r][f] == Board[r][f].upper():
        return not WhiteMove
    else:
        return WhiteMove

while not Checkmate and not Stalemate:
    DisplayBoard()
    print("White to move") if WhiteMove else print("Black to move")
    source_rank,source_file,target_rank,target_file = GetMoves()
    
    Board[target_rank][target_file] = Board[source_rank][source_file]
    Board[source_rank][source_file] = "*"
    WhiteMove = not WhiteMove
