def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(i, " | ".join(row))
        if i < 2:
            print("  " + "-" * 9)

def is_winner(board, player):
    lines = []

    # Rows and columns
    lines.extend(board)  # rows
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  # columns

    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    return any(all(cell == player for cell in line) for line in lines)

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = create_board()
    current = "X"

    print("Tic-Tac-Toe (X goes first)")
    while True:
        print_board(board)
        move = input(f"Player {current}, enter row,col (e.g. 1,2) or q to quit: ")
        if move.lower() == "q":
            print("Game ended.")
            break

        try:
            r_str, c_str = move.split(",")
            r, c = int(r_str), int(c_str)
        except ValueError:
            print("Invalid input. Use row,col format.")
            continue

        if not (0 <= r < 3 and 0 <= c < 3):
            print("Row and col must be 0, 1, or 2.")
            continue

        if board[r][c] != " ":
            print("That spot is already taken.")
            continue

        board[r][c] = current

        if is_winner(board, current):
            print_board(board)
            print(f"Player {current} wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw.")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    main()
