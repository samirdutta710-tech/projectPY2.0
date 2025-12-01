import random
from collections import deque

W, H = 15, 9  # width, height (odd numbers work best)

def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and maze[ny][nx] == "#":
                maze[ny][nx] = " "
                maze[y + dy//2][x + dx//2] = " "
                carve(nx, ny)

    maze[1][1] = " "
    carve(1, 1)
    maze[1][1] = "S"
    maze[height-2][width-2] = "E"
    return maze

def solve_maze(maze):
    height = len(maze)
    width = len(maze[0])
    start = None
    end = None
    for y in range(height):
        for x in range(width):
            if maze[y][x] == "S":
                start = (x, y)
            elif maze[y][x] == "E":
                end = (x, y)
    if not start or not end:
        return

    queue = deque([start])
    came_from = {start: None}
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] != "#" and (nx, ny) not in came_from:
                came_from[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    cur = end
    while cur and cur != start:
        x, y = cur
        if maze[y][x] == " ":
            maze[y][x] = "."
        cur = came_from.get(cur)

def print_maze(maze):
    for row in maze:
        print("".join(row))

def main():
    maze = generate_maze(W, H)
    print("Generated maze:")
    print_maze(maze)
    solve_maze(maze)
    print("\nSolved maze (path = '.'): ")
    print_maze(maze)

if __name__ == "__main__":
    main()
