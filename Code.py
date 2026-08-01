## learn about FEN


Board = [["r","n","b","q","k","b","n","r"],
        ["p" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["*" for _ in range(8)],
        ["P" for _ in range(8)],
        ["R","N","B","Q","K","B","N","R"]]

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
def DisplayBoard():
    for rank in range(8):
        for file in range(8):
            print(Board[rank][file], end=" ")
        print()
DisplayBoard()

Coords = input("enter Coordinates: ")
file = Coordinates.get(Coords[0])
rank = Coordinates.get(Coords[1])
print(file)
print(rank)
print(Board[rank][file])

#Board[7][0] = "*"
#Board[4][0] = "R"
#DisplayBoard()
#row = int(input("what row would u like to move"+"\n"))
