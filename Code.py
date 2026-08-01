## learn about FEN


BlackBoard = [["r","k","b","q","k","b","k","r"], 
              ["p" for _ in range(8)], 
              ["*" for _ in range(8)], 
              ["*" for _ in range(8)], 
              ["*" for _ in range(8)], 
              ["*" for _ in range(8)],
              ["P" for _ in range(8)],
              ["R","K","B","Q","K","B","K","R"]]

def DisplayBoard():
    for row in range(8):
        for column in range(8):
            print(BlackBoard[row][column], end=" ")
        print()

#row = int(input("what row would u like to move"+"\n"))
