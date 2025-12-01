from typing import List

Board = List[List[int]]

def print_board(board: Board):
    for r in range(9):
        row = ""
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row += " |"
            row += f" {board[r][c] if board[r][c] != 0 else '.'}"
        print(row)
        if (r + 1) % 3 == 0 and r != 8:
            print("-" * 22)

def find_empty(board: Board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def valid(board: Board, row: int, col: int, num: int) -> bool:
    if any(board[row][c] == num for c in range(9)):
        return False
    if any(board[r][col] == num for r in range(9)):
        return False
    box_r = (row // 3) * 3
    box_c = (col // 3) * 3
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if board[r][c] == num:
                return False
    return True

def solve(board: Board) -> bool:
    spot = find_empty(board)
    if not spot:
        return True
    r, c = spot
    for num in range(1, 10):
        if valid(board, r, c, num):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0
    return False

def read_board() -> Board:
    print("Enter Sudoku rows (9 digits, 0 for empty):")
    board = []
    for _ in range(9):
        row_str = input().strip()
        row = [int(ch) for ch in row_str if ch.isdigit()]
        if len(row) != 9:
            raise ValueError("Each row must have 9 digits.")
        board.append(row)
    return board

def main():
    try:
        board = read_board()
    except ValueError as e:
        print("Error:", e)
        return

    print("\nInput:")
    print_board(board)
    if solve(board):
        print("\nSolved:")
        print_board(board)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
