"""This  is the source code file of this project"""


def evaluate(board):
    for i in range(3):
        if board[i][0] != "-" and board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                print("Player 1 Won the game.")
                return True
            else:
                print("Player 2 Won the game.")
                return True
    for i in range(3):
        if board[0][i] != "-" and board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                print("Player 1 Won the game.")
                return True
            else:
                print("Plpayer 2 Won the game.")
                return True
    if board[0][0] != "-" and board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            print("Player 1 Won the game.")
            return True
        else:
            print("Player 2 Won the game.")
            return True
    if board[0][2] != "-" and board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            print("Player 1 Won the game.")
            return True
        else:
            print("Player 2 Won the game.")
            return True
    return False


# Option menu creation
print("\n   Welcome to \"TIC-TAC-TOE\"   ")
print("Select game mode")
print("1. Mutliplayer")
print("2. Exit")
# Taking game mode input
print("Enter option : ", end=" ")
option = int(input())

if option == 1:
    print("#" * 30)
    print("Let the game Begin")
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    pla = 1
    for z in range(1,11):
        if z==10:
            print("Draw match.")
            break
        for i in range(3):
            for j in range(3):
                print(board[i][j], end=" ")
                if j == 2:
                    continue
                print("|", end=" ")
            print()
        print("Player ", pla, " Turn .\nspecify row number and column number where you want to place")
        posx, posy = map(int, (input().split()))
        if pla ==1:
            board[posx - 1][posy - 1] = "X"
            pla=pla+1
        elif pla==2:
            board[posx-1][posy-1] = "O"
            pla=pla-1
        if evaluate(board):
            break;
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
            if j == 2:
                continue
            print("|", end=" ")
        print()
else:
    print("Thank you see you later.")
