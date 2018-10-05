from collections import deque
import heapq

#Function to initiliaze the maze into a usable array
def init_maze(maze):

    # Read in the given file line by line until the end of file
    with open('open maze.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            maze.append(list(line))


# Helper function that prints out the given maze
def print_maze(maze):
    for line in maze:
        for item in line:
            print(item, end = ' ')
    print('\n')


# Helper function that finds the coordinates for the 'P' start spot
def get_p_coords(maze):

    p_x = None
    p_y = 0

    for line in maze:
        # Check each line for the 'P' spot
        try:
            p_x = line.index("P")
            break
        # If it is not found, update the y counter
        except ValueError:
            p_y += 1
            continue

    return [p_x, p_y]


# Helper function that finds the coordinates for the '*' goal spot
def get_star_coords(maze):

    star_x = None
    star_y = 0

    for line in maze:
        # Check each line for the star
        try:
            star_x = line.index("*")
            break
        # If its not found, update the star y counter
        except ValueError:
            star_y += 1
            continue

    return [star_x, star_y]

# Heuristic function that uses Manhattan Distance for Greedy Best First & A*
def distance_to_go(current_x, current_y, star_x, star_y):
    return ( abs(current_x - star_x) ) + ( abs( ( -current_y ) - ( -star_y ) ) )


# Function to use the Breadth First Search Algorithm
def breadth_first(maze):

    # Queue to hold the nodes to be expanded
    queue = deque([])

    # First find the location of the 'P' starting spot in maze
    # Then add it to the queue
    p_coords = get_p_coords(maze)
    current_y = p_coords[1]
    current_x = p_coords[0]
    queue.append([current_y, current_x])
    goal = False

    # Check and expand nodes (Clockwise Left to Right)
    # Continue while the goal hasn't been reached
    while (not goal):

        # First goal check the space to the left
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            break
        elif (maze[current_y][current_x - 1] == ' '):
            queue.append([current_y, current_x - 1])
            maze[current_y][current_x - 1] = 'c'

        # Then check the space above
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            break
        elif (maze[current_y - 1][current_x] == ' '):
            queue.append([current_y - 1, current_x])
            maze[current_y - 1][current_x] = 'c'

        # Check the space to the right
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            break
        elif (maze[current_y][current_x + 1] == ' '):
            queue.append([current_y, current_x + 1])
            maze[current_y][current_x + 1] = 'c'

        # Finally check the space below
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            break
        elif (maze[current_y + 1][current_x] == ' '):
            queue.append([current_y + 1, current_x])
            maze[current_y + 1][current_x] = 'c'

        # Update the search path with a '.' and update current position
        current_coords = queue.popleft()
        maze[current_y][current_x] = '.'
        current_x = current_coords[1]
        current_y = current_coords[0]


# Function to use the Depth First Search Algorithm
def depth_first(maze):

    # Stack to hold unexpanded nodes for the depth_first algorithm
    stack = []

    # First find the location of the 'P' starting spot in maze
    # Then add it to the stack
    p_coords = get_p_coords(maze)
    current_y = p_coords[1]
    current_x = p_coords[0]
    stack.append([current_y, current_x])
    goal = False

    # Check and expand nodes (Clockwise Left to Right)
    # Continue checking until the goal is reached
    while (not goal):

        # First goal check the left node
        # If not a goal, then add it to the stack and expand it
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            break
        elif (maze[current_y][current_x - 1] == ' '):
            maze[current_y][current_x] = '.'
            current_x = current_x - 1
            maze[current_y][current_x] = '>'
            stack.append([current_y, current_x])
            continue

        # Then goal check the top node
        # If not a goal, then add it to the stack and expand it
        elif (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            break
        elif (maze[current_y - 1][current_x] == ' '):
            maze[current_y][current_x] = '.'
            current_y = current_y - 1
            maze[current_y][current_x] = 'v'
            stack.append([current_y, current_x])
            continue

        # Goal check the right node
        # If not a goal, then add it to the stack and expand it
        elif (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            break
        elif (maze[current_y][current_x + 1] == ' '):
            maze[current_y][current_x] = '.'
            current_x = current_x + 1
            maze[current_y][current_x] = '<'
            stack.append([current_y, current_x])
            continue

        # Finally goal check the bottom node
        # If not a goal, then add it to the stack and expand it
        elif (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            break
        elif (maze[current_y + 1][current_x] == ' '):
            maze[current_y][current_x] = '.'
            current_y = current_y + 1
            maze[current_y][current_x] = '^'
            stack.append([current_y, current_x])
            continue

        # If nowhere left to go, backtrack on the stack and update coordinates
        else:
            maze[current_y][current_x] = '.'
            current_coords = stack.pop()
            current_x = current_coords[1]
            current_y = current_coords[0]


# Function to use the Greedy Best First Search Algorithm
def greedy_best_first(maze):

    # Priority Queue used by the Greedy algorithm
    g_pqueu = []

    # First find the location of the 'P' starting spot in maze
    # Then add it to the priority queue
    p_coords = get_p_coords(maze)
    current_y = p_coords[1]
    current_x = p_coords[0]

    # Then find the location of the '*' starting spot in maze
    # Then add it to the priority queue
    star_coords = get_star_coords(maze)
    star_y = star_coords[1]
    star_x = star_coords[0]
    goal = False

    while (not goal):

        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            break
        elif (maze[current_y][current_x - 1] == ' '):
            path = distance_to_go(current_x - 1, current_y, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y, current_x - 1]))
            maze[current_y][current_x - 1] = 'c'

        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            break
        elif (maze[current_y - 1][current_x] == ' '):
            path = distance_to_go(current_x, current_y - 1, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y - 1, current_x]))
            maze[current_y - 1][current_x] = 'c'

        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            break
        elif (maze[current_y][current_x + 1] == ' '):
            path = distance_to_go(current_x + 1, current_y, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y, current_x + 1]))
            maze[current_y][current_x + 1] = 'c'

        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            break
        elif (maze[current_y + 1][current_x] == ' '):
            path = distance_to_go(current_x, current_y + 1, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y + 1, current_x]))
            maze[current_y + 1][current_x] = 'c'

        current_coords = heapq.heappop(g_pqueu)
        maze[current_y][current_x] = '.'
        current_x = current_coords[1][1]
        current_y = current_coords[1][0]


# Function to use the A* Search Algorithm
def a_star(maze):

    # Priority Queue used by the Greedy algorithm
    a_pqueue = []

    # First find the location of the 'P' starting spot in maze
    # Then add it to the priority queue
    p_coords = get_p_coords(maze)
    current_y = p_coords[1]
    current_x = p_coords[0]

    # Then find the location of the '*' starting spot in maze
    # Then add it to the priority queue
    star_coords = get_star_coords(maze)
    star_y = star_coords[1]
    star_x = star_coords[0]
    goal = False
    old_path_traveled = 0

    while (not goal):

        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            break
        elif (maze[current_y][current_x - 1] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x - 1, current_y, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y, current_x - 1]))
            maze[current_y][current_x - 1] = 'c'

        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            break
        elif (maze[current_y - 1][current_x] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x, current_y - 1, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y - 1, current_x]))
            maze[current_y - 1][current_x] = 'c'

        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            break
        elif (maze[current_y][current_x + 1] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x + 1, current_y, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y, current_x + 1]))
            maze[current_y][current_x + 1] = 'c'

        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            break
        elif (maze[current_y + 1][current_x] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x, current_y + 1, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y + 1, current_x]))
            maze[current_y + 1][current_x] = 'c'

        current_tuple = heapq.heappop(a_pqueue)
        maze[current_y][current_x] = '.'
        current_x = current_tuple[2][1]
        current_y = current_tuple[2][0]
        old_path_traveled = current_tuple[1]


# Main function to begin the program
def main():
    # Maze array that holds the maze characters from text file
    maze = []
    init_maze(maze)
    print_maze(maze)

    # Variable to hold algorithm entered by user
    alg = None

    # Ask the user which search algorithm they want to use
    while not alg:
        print('Maze Search Program')
        print('---------------------')
        print('Options:')
        print('Breadth First Search: BFS')
        print('Depth First Search: DFS')
        print('Greedy Best First Search: GBF')
        print('A* Search: AS')
        print('\n')
        alg = input('Please enter a search algorithm: ')

        # Call the appropriate search algorithm based on user input
        if (alg == 'BFS'):
            breadth_first(maze)
            print_maze(maze)
        elif (alg == 'DFS'):
            depth_first(maze)
            print_maze(maze)
        elif (alg == 'GBF'):
            greedy_best_first(maze)
            print_maze(maze)
        elif (alg == 'AS'):
            a_star(maze)
            print_maze(maze)

        # If the user does not enter a correct input,
        # Ask them to enter an input again
        else:
            print('Invalid input!')
            print('\n')
            alg = None


main()
