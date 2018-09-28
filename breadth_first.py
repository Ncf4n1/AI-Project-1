from collections import deque
import time

maze = []
queue = deque([])

def init_board():

    with open('open maze.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            maze.append(list(line))


def breadth_first():
    p_x = None
    p_y = 0
    for line in maze:
        try:
            p_x = line.index("P")
            break
        except ValueError:
            p_y += 1
            continue

    queue.append([p_y, p_x])
    goal = False
    current_y = p_y
    current_x = p_x

    while (not goal):
        for line in maze:
            for item in line:
                print(item, end = ' ')

        time.sleep(0.1)
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y][current_x - 1] == ' '):
            queue.append([current_y, current_x - 1])
            maze[current_y][current_x - 1] = '.'

        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y - 1][current_x] == ' '):
            queue.append([current_y - 1, current_x])
            maze[current_y - 1][current_x] = '.'

        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y][current_x + 1] == ' '):
            queue.append([current_y, current_x + 1])
            maze[current_y][current_x + 1] = '.'

        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y + 1][current_x] == ' '):
            queue.append([current_y + 1, current_x])
            maze[current_y + 1][current_x] = '.'

        current_coords = queue.popleft()
        maze[current_y][current_x] = '.'
        current_x = current_coords[1]
        current_y = current_coords[0]
        maze[current_y][current_x] = 'X'


    for line in maze:
        for item in line:
            print(item, end = ' ')


def main():
    init_board()
    breadth_first()

main()
