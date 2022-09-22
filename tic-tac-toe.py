# Author: Camila Santana

def main():
    current_player = next_player("")
    new_board = create_board()
    while not (has_winner(new_board) or is_a_draw(new_board)):
        show_board(new_board)
        make_move(current_player, new_board)
        current_player = next_player(current_player)
    show_board(new_board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
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

def make_move(player, board):
    try:
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        board[square - 1] = player
    except ValueError:
        print ("Please enter only numbers. Try again")
    except IndexError:
        print ("Please enter numbers between 1 and 9. Try again")

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
 

if __name__ == "__main__":
    main()