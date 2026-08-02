## learn about FEN

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

DisplayBoard()

Coords = input("enter Coordinates of piece to be moved: ")
file = Coordinates.get(Coords[0])
rank = Coordinates.get(Coords[1])
print(Board[rank][file])

Coords2 = input("enter Coordinates of square to move to: ")
file2 = Coordinates.get(Coords2[0])
rank2 = Coordinates.get(Coords2[1])

match Board[rank][file].lower():
    case "r":
        print("rook")
    case "n":
        print("knight")
    case "b":
        print("bishop")
    case "q":
        print("queen")
    case "k":
        print("king")
Board[rank2][file2] = Board[rank][file]
Board[rank][file] = "*"
DisplayBoard()

#row = int(input("what row would u like to move"+"\n"))
