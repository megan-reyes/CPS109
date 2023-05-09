
board = [["X","O","O"], ["O","X","O"], ["O","#","X"]]
board2 = []
for sublist in board:
    for item in sublist:
        board2.append(item)

def checkRows(board2):

    for i in range(3):
        if board2[i] == "X" and board2[i+3] == "X" and board2[i+6] == "X":
            print("P1 wins")
        elif board2[i] == "O" and board2[i+3] == "O" and board2[i+6] == "O":
            print("P2 wins")
        elif board2[i:i+3] == "X":
            print("P1 wins")
        elif board2[i:i+3] == "O":
            print("P2 wins")


def checkWinner(board2):

    if checkRows(board2):
        checkRows(board2)
    elif board2[0] == "X" and board2[4] == "X" and board2[8] == "X":
            print("P1 wins")
    elif board2[0] == "O" and board2[4] == "O" and board2[8] == "O":
            print("P2 wins")
    elif board2[2] == "X" and board2[4] == "X" and board2[6] == "X":
            print("P1 wins")
    elif board2[2] == "O" and board2[4] == "O" and board2[6] == "O":
            print("P2 wins")
    else:
        print('Tie')



checkWinner(board2)

#
# board = [["X","O","O"], ["O","X","O"], ["O","#","X"]]
# # Test 2
# board = [["X","O","O"], ["O","X","O"], ["X","#","O"]]
# # Test 3
# board = [["X","X","O"], ["O","X","O"], ["X","O","#"]]
