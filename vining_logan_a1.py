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
    # Also create variable to hold the number of expanded nodes
    p_coords = get_p_coords(maze)
    current_y = p_coords[1]
    current_x = p_coords[0]
    b_path_cost = 0
    queue.append(([current_y, current_x], b_path_cost))
    b_expanded = 1
    goal = False

    # Check and expand nodes (Clockwise Left to Right)
    # Continue while the goal hasn't been reached
    while (not goal):

        # First goal check the space to the left and if it matches, print path cost
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            print('Path Cost = ' + str(b_path_cost + 1))
            break
        elif (maze[current_y][current_x - 1] == ' '):
            queue.append(([current_y, current_x - 1], b_path_cost + 1))
            maze[current_y][current_x - 1] = 'c'

        # Then check the space above and if it matches, print path cost
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            print('Path Cost = ' + str(b_path_cost + 1))
            break
        elif (maze[current_y - 1][current_x] == ' '):
            queue.append(([current_y - 1, current_x], b_path_cost + 1))
            maze[current_y - 1][current_x] = 'c'

        # Check the space to the right and if it matches, print path cost
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            print('Path Cost = ' + str(b_path_cost + 1))
            break
        elif (maze[current_y][current_x + 1] == ' '):
            queue.append(([current_y, current_x + 1], b_path_cost + 1))
            maze[current_y][current_x + 1] = 'c'

        # Finally check the space below and if it matches, print path cost
        # If not a goal and is open, add it to the unexpanded queue
        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            print('Path Cost = ' + str(b_path_cost + 1))
            break
        elif (maze[current_y + 1][current_x] == ' '):
            queue.append(([current_y + 1, current_x], b_path_cost + 1))
            maze[current_y + 1][current_x] = 'c'

        # Update the search path with a '.' and update current position
        # Also update the number of expanded nodes after popping
        current_node = queue.popleft()
        b_expanded += 1
        maze[current_y][current_x] = '.'
        current_x = current_node[0][1]
        current_y = current_node[0][0]
        b_path_cost = current_node[1]

    # Finish by printing the number of expanded nodes
    print('Expanded Nodes = ' + str(b_expanded))

# Function to use the Depth First Search Algorithm
def depth_first(maze):

    # Stack to hold unexpanded nodes for the depth_first algorithm
    stack = []

    # First find the location of the 'P' starting spot in maze
    # Then add it to the stack
    p_coords = get_p_coords(maze)
    current_y = p_coords[1]
    current_x = p_coords[0]
    d_path_cost = 0
    stack.append([current_y, current_x])
    d_expanded = 0
    goal = False

    # Check and expand nodes (Clockwise Left to Right)
    # Continue checking until the goal is reached
    while (not goal):

        # First goal check the left node and if it matches, print path cost
        # If not a goal, then add it to the stack, expand it, & update path cost
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            print('Path Cost = ' + str(d_path_cost + 1))
            break
        elif (maze[current_y][current_x - 1] == ' '):
            stack.append([current_y, current_x - 1])
            d_path_cost += 1
            d_expanded += 1
            maze[current_y][current_x - 1] = '.'
            continue

        # Then goal check the top node and if it matches, print path cost
        # If not a goal, then add it to the stack, expand it, & update path cost
        elif (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            print('Path Cost = ' + str(d_path_cost + 1))
            break
        elif (maze[current_y - 1][current_x] == ' '):
            stack.append([current_y - 1, current_x])
            d_path_cost += 1
            d_expanded += 1
            maze[current_y - 1][current_x] = '.'
            continue

        # Goal check the right node and if it matches, print path cost
        # If not a goal, then add it to the stack, expand it, & update path cost
        elif (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            print('Path Cost = ' + str(d_path_cost + 1))
            break
        elif (maze[current_y][current_x + 1] == ' '):
            stack.append([current_y, current_x + 1])
            d_path_cost += 1
            d_expanded += 1
            maze[current_y][current_x + 1] = '.'
            continue

        # Finally goal check the bottom node and if it matches, print path cost
        # If not a goal, then add it to the stack, expand it, and update path cost
        elif (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            print('Path Cost = ' + str(d_path_cost + 1))
            break
        elif (maze[current_y + 1][current_x] == ' '):
            stack.append([current_y + 1, current_x])
            d_path_cost += 1
            d_expanded += 1
            maze[current_y + 1][current_x] = '.'
            continue

        # If nowhere left to go, backtrack on the stack and update coordinates
        else:
            maze[current_y][current_x] = '.'
            current_coords = stack.pop()
            d_path_cost -= 1
            current_x = current_coords[1]
            current_y = current_coords[0]

    print('Expanded Nodes = ' + str(d_expanded))


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

    g_expanded = 0
    g_path_cost = 0
    goal = False

    # Check and expand nodes (Clockwise Left to Right)
    # Continue checking until the goal is reached
    while (not goal):

        # First goal check the left node and if it matches, print path cost
        # If not a goal, then calculate its distance to goal and add it to the PQ
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            print('Path Cost = ' + str(g_path_cost + 1))
            break
        elif (maze[current_y][current_x - 1] == ' '):
            path = distance_to_go(current_x - 1, current_y, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y, current_x - 1], g_path_cost + 1))
            maze[current_y][current_x - 1] = 'c'

        # Then goal check the top node and if it matches, print path cost
        # If not a goal, then calculate its distance to goal and add it to the PQ
        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            print('Path Cost = ' + str(g_path_cost + 1))
            break
        elif (maze[current_y - 1][current_x] == ' '):
            path = distance_to_go(current_x, current_y - 1, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y - 1, current_x], g_path_cost + 1))
            maze[current_y - 1][current_x] = 'c'

        # Goal check the right node and if it matches, print path cost
        # If not a goal, then calculate its distance to goal and add it to the PQ
        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            print('Path Cost = ' + str(g_path_cost + 1))
            break
        elif (maze[current_y][current_x + 1] == ' '):
            path = distance_to_go(current_x + 1, current_y, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y, current_x + 1], g_path_cost + 1))
            maze[current_y][current_x + 1] = 'c'

        # Finally goal check the bottom node and if it matches, print path cost
        # If not a goal, then calculate its distance to goal and add it to the PQ
        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            print('Path Cost = ' + str(g_path_cost + 1))
            break
        elif (maze[current_y + 1][current_x] == ' '):
            path = distance_to_go(current_x, current_y + 1, star_x, star_y)
            heapq.heappush(g_pqueu, (path, [current_y + 1, current_x], g_path_cost + 1))
            maze[current_y + 1][current_x] = 'c'

        # Update the old position with a '.' and update the current position
        # Also update the expanded node count and the node path cost
        current_node = heapq.heappop(g_pqueu)
        g_expanded += 1
        maze[current_y][current_x] = '.'
        current_x = current_node[1][1]
        current_y = current_node[1][0]
        g_path_cost = current_node[2]

    print('Expanded Nodes = ' + str(g_expanded))


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
    a_expanded = 0
    old_path_traveled = 0

    # Check and expand nodes (Clockwise Left to Right)
    # Continue checking until the goal is reached
    while (not goal):

        # First goal check the left node
        # If not a goal, then calculate the sum of the distance to goal plus
        # the path cost to the current position
        if (maze[current_y][current_x - 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x - 1] = 'O'
            print('Path Cost = ' + str(old_path_traveled + 1))
            break
        elif (maze[current_y][current_x - 1] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x - 1, current_y, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y, current_x - 1]))
            maze[current_y][current_x - 1] = 'c'

        # Then goal check the top node
        # If not a goal, then calculate the sum of the distance to goal plus
        # the path cost to the current position
        if (maze[current_y - 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y - 1][current_x] = 'O'
            print('Path Cost = ' + str(old_path_traveled + 1))
            break
        elif (maze[current_y - 1][current_x] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x, current_y - 1, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y - 1, current_x]))
            maze[current_y - 1][current_x] = 'c'

        # Goal check the right node
        # If not a goal, then calculate the sum of the distance to goal plus
        # the path cost to the current position
        if (maze[current_y][current_x + 1] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y][current_x + 1] = 'O'
            print('Path Cost = ' + str(old_path_traveled + 1))
            break
        elif (maze[current_y][current_x + 1] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x + 1, current_y, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y, current_x + 1]))
            maze[current_y][current_x + 1] = 'c'

        # Finally goal check the bottom node
        # If not a goal, then calculate the sum of the distance to goal plus
        # the path cost to the current position
        if (maze[current_y + 1][current_x] == '*'):
            goal = True
            print('\n')
            maze[current_y][current_x] = '.'
            maze[current_y + 1][current_x] = 'O'
            print('Path Cost = ' + str(old_path_traveled + 1))
            break
        elif (maze[current_y + 1][current_x] == ' '):
            path_traveled = old_path_traveled + 1
            path_to_go = distance_to_go(current_x, current_y + 1, star_x, star_y)
            path = path_traveled + path_to_go
            heapq.heappush(a_pqueue, (path, path_traveled, [current_y + 1, current_x]))
            maze[current_y + 1][current_x] = 'c'

        # Update the old position with a '.' and update the current position
        # Update the the path cost of the old position as well
        current_tuple = heapq.heappop(a_pqueue)
        a_expanded += 1
        maze[current_y][current_x] = '.'
        current_x = current_tuple[2][1]
        current_y = current_tuple[2][0]
        old_path_traveled = current_tuple[1]

    print('Expanded Nodes = ' + str(a_expanded))


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
