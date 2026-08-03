## learn about FEN

#initializes the board to starting position via an array
Board = [["r","n","b","q","k","b","n","r"],
        ["p" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
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

def RookLegalMoves(f , r):
    Moves = []
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves to right of rook
        tempf += 1
        if tempf > 7 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves to left of rook
        tempf -= 1
        if tempf < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves below rook
        tempr += 1
        if tempr > 7 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves above rook
        tempr -= 1
        if tempr < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    return Moves

def BishopLegalMoves(f , r):
    Moves = []
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves toward bottom-right of bishop
        tempf += 1
        tempr += 1
        if tempf > 7 or tempr > 7 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves towards top-left of bishop
        tempf -= 1
        tempr -= 1
        if tempf < 0 or tempr < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves towards bottom-left of bishop
        tempf -= 1
        tempr += 1
        if tempr > 7 or tempf < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves towards top-left of bishop
        tempf += 1
        tempr -= 1
        if tempf > 7 or tempr < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    return Moves

def QueenLegalMoves(f , r):
    Moves = []
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves to right of rook
        tempf += 1
        if tempf > 7 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves to left of rook
        tempf -= 1
        if tempf < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves below rook
        tempr += 1
        if tempr > 7 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves above rook
        tempr -= 1
        if tempr < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves toward bottom-right of bishop
        tempf += 1
        tempr += 1
        if tempf > 7 or tempr > 7 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves towards top-left of bishop
        tempf -= 1
        tempr -= 1
        if tempf < 0 or tempr < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves towards bottom-left of bishop
        tempf -= 1
        tempr += 1
        if tempr > 7 or tempf < 0 or Board [tempr][tempf] != "*":
            break
        else:
            Moves.append(str(tempf) + str(tempr))
    tempf = f
    tempr = r
    while True:
        #calculates all legal moves towards top-left of bishop
        tempf += 1
        tempr -= 1
        if tempf > 7 or tempr < 0 or Board [tempr][tempf] != "*":
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
        if 0 <= f + x <= 7 and 0 <= r + y <= 7:
            Moves.append(str(f + x) + str(r + y))
    return Moves

def GetMoves():
    while True:
        Coords = input("enter Coordinates of piece to be moved: ")
        source_file = Coordinates.get(Coords[0])
        source_rank = Coordinates.get(Coords[1])
        #print(source_file, source_rank)
        print( "you have chosen",Board[source_rank][source_file])
        match Board[source_rank][source_file].lower():
            case "r":
                LegalMoves = RookLegalMoves(source_file , source_rank)
            case "b":
                LegalMoves = BishopLegalMoves(source_file , source_rank)
            case "q":
                LegalMoves = QueenLegalMoves(source_file , source_rank)
            case "n":
                LegalMoves = KnightLegalMoves(source_file , source_rank)
        print(LegalMoves)
        
        Coords2 = input("enter Coordinates of square to move to: ")
        target_file = Coordinates.get(Coords2[0])
        target_rank = Coordinates.get(Coords2[1])
        for i in LegalMoves:
            if i == str(target_file) + str(target_rank):
                #print("Legal Move")
                return source_rank,source_file,target_rank,target_file
        print("illegal move")

DisplayBoard()
source_rank,source_file,target_rank,target_file = GetMoves()

Board[target_rank][target_file] = Board[source_rank][source_file]
Board[source_rank][source_file] = "*"
DisplayBoard()

#row = int(input("what row would u like to move"+"\n"))
