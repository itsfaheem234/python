board = [" " for _ in range(9)]


def show_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False


def board_full():
    return " " not in board


def play_game():
    current_player = "X"

    while True:
        show_board()

        print(f"player {current_player}'s turn")

        try:
            position = int(input("choose a position (1-9): "))

            if position < 1 or position > 9:
                print("please choose a number from 1 to 9.")
                continue

            position -= 1

            if board[position] != " ":
                print("that position is already taken!")
                continue

            board[position] = current_player

        except ValueError:
            print("please enter a number.")
            continue

        if check_winner(current_player):
            show_board()
            print(f" player {current_player} wins!")
            break

        if board_full():
            show_board()
            print("it's a draw! ")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


print("===== TIC-TAC-TOE =====")
print("player 1 = X")
print("player 2 = O")

play_game()
