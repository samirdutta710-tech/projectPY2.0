ROWS = 6
COLS = 7

def create_board():
    return [["." for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + " ".join(str(c) for c in range(COLS)))
    for r in range(ROWS):
        print(r, " ".join(board[r]))
    print()

def drop_piece(board, col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ".":
            board[row][col] = piece
            return True
    return False

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def check_winner(board, piece):
    directions = [(0,1), (1,0), (1,1), (1,-1)]
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != piece:
                continue
            for dr, dc in directions:
                count = 0
                rr, cc = r, c
                while in_bounds(rr, cc) and board[rr][cc] == piece:
                    count += 1
                    if count == 4:
                        return True
                    rr += dr
                    cc += dc
    return False

def board_full(board):
    return all(cell != "." for row in board for cell in row)

def main():
    board = create_board()
    current = "X"
    print("Connect Four (X vs O)")

    while True:
        print_board(board)
        choice = input(f"Player {current}, choose column (0-{COLS-1}) or q to quit: ").strip()
        if choice.lower() == "q":
            print("Game ended.")
            break
        if not choice.isdigit():
            print("Please enter a column number.")
            continue
        col = int(choice)
        if not (0 <= col < COLS):
            print("Column out of range.")
            continue
        if not drop_piece(board, col, current):
            print("Column is full.")
            continue

        if check_winner(board, current):
            print_board(board)
            print(f"Player {current} wins! 🎉")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw.")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    main()
