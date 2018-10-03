import heapq, time

maze = []
pqueue = []

def init_board():

    with open('open maze.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            maze.append(list(line))

def distance_to_go(current_x, current_y, star_x, star_y):
    return ( abs(current_x - star_x) ) + ( abs( ( -current_y ) - ( -star_y ) ) )

def a_star():
    p_x = None
    p_y = 0
    for line in maze:
        try:
            p_x = line.index("P")
            break
        except ValueError:
            p_y += 1
            continue

    star_x = None
    star_y = 0
    for line in maze:
        try:
            star_x = line.index("*")
            break
        except ValueError:
            star_y += 1
            continue

    goal = False
    current_y = p_y
    current_x = p_x
    old_path_traveled = 0

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
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x - 1, current_y, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(pqueue, (path, path_traveled, [current_y, current_x - 1]))
            maze[current_y][current_x - 1] = 'c'

        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y - 1][current_x] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x, current_y - 1, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(pqueue, (path, path_traveled, [current_y - 1, current_x]))
            maze[current_y - 1][current_x] = 'c'

        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y][current_x + 1] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x + 1, current_y, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(pqueue, (path, path_traveled, [current_y, current_x + 1]))
            maze[current_y][current_x + 1] = 'c'

        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y + 1][current_x] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x, current_y + 1, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(pqueue, (path, path_traveled, [current_y + 1, current_x]))
            maze[current_y + 1][current_x] = 'c'

        current_tuple = heapq.heappop(pqueue)
        maze[current_y][current_x] = '.'
        current_x = current_tuple[2][1]
        current_y = current_tuple[2][0]
        maze[current_y][current_x] = 'X'
        old_path_traveled = current_tuple[1]

    for line in maze:
        for item in line:
            print(item, end = ' ')

def main():
    init_board()
    a_star()


main()
