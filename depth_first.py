maze = []

def init_board():

    with open('open maze.txt', 'r') as f:
        while True:
            c = f.readline()
            if not c:
                break
            maze.append(list(c))



def depth_first():
    y_index = 0
    x_index = None
    for line in maze:
        try:
            x_index = line.index("P")
            break
        except ValueError:
            y_index += 1
            continue


def main():
    init_board()
    depth_first()

main()
