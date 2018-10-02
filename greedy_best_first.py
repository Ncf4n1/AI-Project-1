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

def calc_distance(p_x, p_y, star_x, star_y):
    return ( abs(p_x - star_x) ) + ( abs( ( -p_y ) - ( -star_y ) ) )

def greedy_best_first():
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
            path = calc_distance(current_x - 1, current_y, star_x, star_y)
            heapq.heappush(pqueue, (path, [current_y, current_x - 1]))
            maze[current_y][current_x - 1] = '.'

        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y - 1][current_x] == ' '):
            path = calc_distance(current_x, current_y - 1, star_x, star_y)
            heapq.heappush(pqueue, (path, [current_y - 1, current_x]))
            maze[current_y - 1][current_x] = '.'

        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y][current_x + 1] == ' '):
            path = calc_distance(current_x + 1, current_y, star_x, star_y)
            heapq.heappush(pqueue, (path, [current_y, current_x + 1]))
            maze[current_y][current_x + 1] = '.'

        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print("You solved the maze")
            break
        elif (maze[current_y + 1][current_x] == ' '):
            path = calc_distance(current_x, current_y + 1, star_x, star_y)
            heapq.heappush(pqueue, (path, [current_y + 1, current_x]))
            maze[current_y + 1][current_x] = '.'

        current_coords = heapq.heappop(pqueue)
        maze[current_y][current_x] = '.'
        current_x = current_coords[1][1]
        current_y = current_coords[1][0]
        maze[current_y][current_x] = 'X'

    for line in maze:
        for item in line:
            print(item, end = ' ')

def main():
    init_board()
    greedy_best_first()


main()
