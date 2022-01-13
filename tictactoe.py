'''CSE 210 - Programming with Classes
 W02 Prove: Developer - Solo Code Submission
 Tic-Tac-Toe Game
 Author: Luis Carlo Romanini Neres'''

def main():
    print("Welcome to the Tic-Tac-Toe Game!")
    board_game=create_board()
    print_board(board_game)


def create_board():
    board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
    return board

def print_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def game_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            print("It is a draw")
            return False
    return True

     








if __name__ == "__main__":
    main()