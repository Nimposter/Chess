## learn about FEN

WhiteMove = True
Checkmate = False
Stalemate = False
CastlingRights = "KQkq"
EnPassantTarget = "-"

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

#strings to convert array indexes to chess coordinates (string splicing)
Files = "abcdefgh"
Ranks = "87654321"

#defined function to print the board, uses nested loops, for ranks (rows) and files (columns)
def DisplayBoard():
    for rank in Board:
        for piece in rank:
            print(piece, end=" ")
        print()

def KingLegalMoves(f , r):
    relative_offset = [(+1, +1) , (+1, 0) , (+1, -1),
                       (0, +1) ,            (0, -1),
                       (-1, +1) , (-1, 0) , (-1, -1)]
    Moves = []
    for x , y in relative_offset:
        if OnBoard(f + x , r + y) and not IsAttacked(f + x , r + y):
            if Board[r + y][f + x] == "*" or IsEnemy(f + x , r + y):
                Moves.append(str(f + x) + str(r + y))
    
    if WhiteMove:
        if CanCastle("K"):
            Moves.append(str(f + 2) + str(r))
        if CanCastle("Q"):
            Moves.append(str(f - 2) + str(r))
    else:
        if CanCastle("k"):
            Moves.append(str(f + 2) + str(r))
        
        if CanCastle("q"):
            Moves.append(str(f - 2) + str(r))


    return Moves

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
        if OnBoard(f + x , r + y):
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
        
        if (str(f - 1) + str(r - 1)) == EnPassantTarget or (str(f + 1) + str(r - 1)) == EnPassantTarget:
            print("En Passant")
            Moves.append(EnPassantTarget)
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
        
        if (str(f - 1) + str(r + 1)) == EnPassantTarget or (str(f + 1) + str(r + 1)) == EnPassantTarget:
            print("En Passant")
            Moves.append(EnPassantTarget)
        
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
                case "k":
                    LegalMoves = KingLegalMoves(source_file , source_rank)
                case "q" | "b" | "r":
                    LegalMoves = SlidingLegalMoves(source_file , source_rank , Board[source_rank][source_file].lower())
                case "n":
                    LegalMoves = KnightLegalMoves(source_file , source_rank)
                case "p":
                    LegalMoves = PawnLegalMoves(source_file , source_rank)
        
        print(LegalMoves)
        LegalMoves = FilterLegalMoves(source_file , source_rank , LegalMoves)
        
        
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

def IsAttacked(f , r):
    King = [(+1, +1) , (+1, 0) , (+1, -1), (0, +1) , (0, -1), (-1, +1) , (-1, 0) , (-1, -1)]
    Rook = [(1,0) , (-1,0) , (0,1) , (0,-1)]
    Bishop = [(1, 1) , (1, -1) , (-1, 1) , (-1, -1)]
    Knight = [(+2, +1) , (+2, -1) , (-2, +1), (-2, -1) , (+1, +2) , (+1, -2), (-1, +2) , (-1, -2)]
    
    for x , y in Rook:
        tempf = f
        tempr = r
        while True:
            tempf += x
            tempr += y
            if not OnBoard(tempf, tempr):
                break
            elif Board [tempr][tempf] != "*":
                if Board [tempr][tempf].lower() in  ("r" , "q"):
                    if IsEnemy(tempf , tempr):
                        return True
                break
    
    for x , y in Bishop:
        tempf = f
        tempr = r
        while True:
            tempf += x
            tempr += y
            if not OnBoard(tempf, tempr):
                break
            elif Board [tempr][tempf] != "*":
                if Board [tempr][tempf].lower() in  ("b" , "q"):
                    if IsEnemy(tempf , tempr):
                        return True
                break
    
    for x , y in Knight:
        if OnBoard(f + x , r + y):
            if Board[r + y][f + x].lower() == "n" and IsEnemy(f + x, r + y):
                return True
    
    for x , y in King:
        if OnBoard(f + x , r + y) and Board[r + y][f + x].lower() == "k" and IsEnemy(f + x , r + y):
            return True
    
    if WhiteMove:
        if OnBoard(f - 1 , r - 1) and Board[r - 1][f - 1].lower() == "p" and IsEnemy(f - 1 , r - 1):
            return True
        if OnBoard(f + 1 , r - 1) and Board[r - 1][f + 1].lower() == "p" and IsEnemy(f + 1 , r - 1):
            return True
    else:
        if OnBoard(f - 1 , r + 1) and Board[r + 1][f - 1].lower() == "p" and IsEnemy(f - 1 , r + 1):
            return True
        if OnBoard(f + 1 , r + 1) and Board[r + 1][f + 1].lower() == "p" and IsEnemy(f + 1 , r + 1):
            return True
    return False

#filters out move that leave the king in check
def FilterLegalMoves(sourcef , sourcer , Moves):
    kingf , kingr = FindKing()
    
    FilteredMoves = []
    
    for i in Moves:
        targetf = int(i[0])
        targetr = int(i[1])
        temp1 = Board[sourcer][sourcef]
        temp2 = Board[targetr][targetf]
        
        Board[targetr][targetf] = Board[sourcer][sourcef]
        Board[sourcer][sourcef] = "*"
        
        kingf, kingr = FindKing()
    
        if not IsAttacked(kingf , kingr):
            FilteredMoves.append(i)
        
        Board[sourcer][sourcef] = temp1
        Board[targetr][targetf] = temp2
    return FilteredMoves

def FEN():
    FenString = ""
    for rank in Board:
        for piece in rank:
            if piece != "*":
                FenString = FenString + piece
                #print(FenString)
            else:
                try:
                    num = int(FenString[-1])
                    num += 1
                    #FenString = FenString[:len(FenString) - 1]
                    FenString = FenString[:-1] + str(num)
                except ValueError:
                    FenString = FenString + "1"
                '''if isinstance(FenString[-1] , int):
                    FenString[-1] + 1
                    print("int")'''
            #print(piece, end=" ")
        FenString = FenString + "/"
    FenString = FenString[:-1]
    if WhiteMove:
        FenString += " w "
    else:
        FenString += " b "
    
    FenString += CastlingRights
    
    if EnPassantTarget == "-":
        FenString += " -"
    else:
        FenString += " " + (Files[int(EnPassantTarget[0])]) + (Ranks[int(EnPassantTarget[1])])
    print(FenString)

def CanCastle(side):
    kingf , kingr = FindKing()
    if IsAttacked(kingf , kingr):
        return False
    
    match side:
        case "K":
            if "K" in CastlingRights:
                if Board[kingr][kingf + 1] == Board[kingr][kingf + 2] == "*":
                    if not IsAttacked(kingf + 1 , kingr) and not IsAttacked(kingf + 2 , kingr):
                            return True
        
        case "k":
            if "k" in CastlingRights:
                if Board[kingr][kingf + 1] == Board[kingr][kingf + 2] == "*":
                    if not IsAttacked(kingf + 1 , kingr) and not IsAttacked(kingf + 2 , kingr):
                            return True
        case "Q":
            if "Q" in CastlingRights:
                if Board[kingr][kingf - 1] == Board[kingr][kingf - 2] == Board[kingr][kingf - 3] == "*":
                    if not IsAttacked(kingf - 1 , kingr) and not IsAttacked(kingf - 2 , kingr):
                            return True
                            
                            
        case "q":
            if "q" in CastlingRights:
                if Board[kingr][kingf - 1] == Board[kingr][kingf - 2] == Board[kingr][kingf - 3] == "*":
                    if not IsAttacked(kingf - 1 , kingr) and not IsAttacked(kingf - 2 , kingr):
                            return True
    return False

#Returns the array indexes of your king
def FindKing():
    for rank in range(8):
        for file in range(8):
            if WhiteMove:
                if Board[rank][file] == "K":
                    return file , rank
            else:
                if Board[rank][file] == "k":
                    return file , rank

def CheckGameState():
    global Checkmate , Stalemate
    for rank in range(8):
        for file in range(8):
            if Board[rank][file] != "*" and not IsEnemy(file , rank):
                print("bleh")
                match Board[rank][file].lower():
                    case "k":
                        LegalMoves = KingLegalMoves(file , rank)
                    case "q" | "b" | "r":
                        LegalMoves = SlidingLegalMoves(file , rank , Board[rank][file].lower())
                    case "n":
                        LegalMoves = KnightLegalMoves(file , rank)
                    case "p":
                        LegalMoves = PawnLegalMoves(file , rank)
        
                print(LegalMoves)
                LegalMoves = FilterLegalMoves(file , rank , LegalMoves)
                
                if LegalMoves:
                    return
    kingf , kingr = FindKing()
    if IsAttacked(kingf , kingr):
        Checkmate = True
    else:
        Stalemate = True

while not Checkmate and not Stalemate:
    DisplayBoard()
    FEN()
    print("White to move") if WhiteMove else print("Black to move")
    source_rank,source_file,target_rank,target_file = GetMoves()
    
    
    match Board[source_rank][source_file]:
        case "K":
            CastlingRights = CastlingRights.replace("K" , "").replace("Q" , "")
        case "k":
            CastlingRights = CastlingRights.replace("k" , "").replace("q" , "")
        case "R":
            if source_file == 0 and source_rank == 7:
                CastlingRights = CastlingRights.replace("Q" , "")
            elif source_file == 7 and source_rank == 7:
                CastlingRights = CastlingRights.replace("K" , "")
        case "r":
            if source_file == 0 and source_rank == 0:
                CastlingRights = CastlingRights.replace("q" , "")
            elif source_file == 7 and source_rank == 0:
                CastlingRights = CastlingRights.replace("k" , "")

    match Board[target_rank][target_file]:
        case "R":
            if target_file == 0 and target_rank == 7:
                CastlingRights = CastlingRights.replace("Q" , "")
            elif target_file == 7 and target_rank == 7:
                CastlingRights = CastlingRights.replace("K" , "")
        case "r":
            if target_file == 0 and target_rank == 0:
                CastlingRights = CastlingRights.replace("q" , "")
            elif target_file == 7 and target_rank == 0:
                CastlingRights = CastlingRights.replace("k" , "")

    
    
    if (str(target_file) + str(target_rank)) == EnPassantTarget:
        if WhiteMove:
            print("enpassant executed")
            Board[target_rank + 1][target_file] = "*"
        else:
            print("enpassant executed")
            Board[target_rank - 1][target_file] = "*"
    if abs(target_rank - source_rank) == 2 and Board[source_rank][source_file].lower() == "p":
        EnPassantTarget = str(source_file) + str((source_rank + target_rank) // 2)
    elif EnPassantTarget != "-":
        EnPassantTarget = "-"
    if abs(target_file - source_file) == 2 and Board[source_rank][source_file].lower() == "k":
        if target_file == 6:
            Board[target_rank][target_file - 1] = Board[source_rank][7]
            Board[source_rank][7] = "*"
        elif target_file == 2:
            Board[target_rank][target_file + 1] = Board[source_rank][0]
            Board[source_rank][0] = "*"
    
     
    print(EnPassantTarget)
    print(type(EnPassantTarget))
        
    Board[target_rank][target_file] = Board[source_rank][source_file]
    Board[source_rank][source_file] = "*"
    
    WhiteMove = not WhiteMove

    CheckGameState()
