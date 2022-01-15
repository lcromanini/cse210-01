'''CSE 210 - Programming with Classes
 W02 Prove: Developer - Solo Code Submission
 Tic-Tac-Toe Game
 Author: Luis Carlo Romanini Neres'''

#Main function to call the others. 
def main():
    play_again=""
    #A while loop to play initiate the game as long as user types something different than "N" or "n"
    while play_again.upper()!="N":
        print("Welcome to the Tic-Tac-Toe Game!")
        player = next_player("")
    #Calling the fucntion create_board() to create the board for the game. 
        board_game=create_board()
        while not (has_winner(board_game) or game_draw(board_game)):
    #Calling the function print_board to print the board. 
            print_board(board_game)
            current_player(player, board_game)
            player = next_player(player)
        print_board(board_game)
        print("Good game. Thanks for playing!")
        play_again=input("Do you want to play again? Y/N ") 

#Function create_board
def create_board():
    board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
    return board
#This function prints the board according to the game rules. 
def print_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")
#This function determine the rules for the draw situation. 
def game_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])    

def current_player(player, board):
    square = int(input(f"{player}'s turn to choose a number between 1 and 9: "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"     



if __name__ == "__main__":
    main()