import time

maze = []
stack = []

def init_board():

    with open('open maze.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            maze.append(list(line))


def depth_first():
    p_x = None
    p_y = 0
    for line in maze:
        try:
            p_x = line.index("P")
            break
        except ValueError:
            p_y += 1
            continue

    stack.append([p_y, p_x])
    goal = False
    current_y = p_y
    current_x = p_x

    while (not goal):
        for line in maze:
            for item in line:
                print(item, end = ' ')
            print('')

        time.sleep(0.1)
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            print("You solved the maze")
            break
        elif (maze[current_y][current_x - 1] == ' '):
            maze[current_y][current_x] = '.'
            current_x = current_x - 1
            maze[current_y][current_x] = '>'
            stack.append([current_y, current_x])
            continue
        elif (maze[current_y - 1][current_x] == '*'):
            goal = True
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            print("You solved the maze")
            break
        elif (maze[current_y - 1][current_x] == ' '):
            maze[current_y][current_x] = '.'
            current_y = current_y - 1
            maze[current_y][current_x] = 'v'
            stack.append([current_y, current_x])
            continue
        elif (maze[current_y][current_x + 1] == '*'):
            goal = True
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'X'
            print("You solved the maze")
            break
        elif (maze[current_y][current_x + 1] == ' '):
            maze[current_y][current_x] = '.'
            current_x = current_x + 1
            maze[current_y][current_x] = '<'
            stack.append([current_y, current_x])
            continue
        elif (maze[current_y + 1][current_x] == '*'):
            goal = True
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'X'
            print("You solved the maze")
            break
        elif (maze[current_y + 1][current_x] == ' '):
            maze[current_y][current_x] = '.'
            current_y = current_y + 1
            maze[current_y][current_x] = '^'
            stack.append([current_y, current_x])
            continue
        else:
            maze[current_y][current_x] = '.'
            current_coords = stack.pop()
            current_x = current_coords[1]
            current_y = current_coords[0]
            maze[current_y][current_x] = 'X'

    for line in maze:
        for item in line:
            print(item, end = ' ')
        print('')

def main():
    init_board()
    depth_first()

main()
