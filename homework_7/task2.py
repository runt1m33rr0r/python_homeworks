import string


maze = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'g', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]


def checkValidTile(x, y):
    if maze[x][y] == ' ' or maze[x][y] == 'g':
        return True
    
    return False


def chooseNext(x, y):
    width, height = len(maze[0]), len(maze)
    resultX, resultY, isValid = x, y, False

    if y - 1 > 0 and checkValidTile(x, y - 1):
        resultX, resultY, isValid = x, y - 1, True
    elif width > y + 1 and checkValidTile(x, y + 1):
        resultX, resultY, isValid = x, y + 1, True
    elif height > x + 1 and checkValidTile(x + 1, y):
        resultX, resultY, isValid = x + 1, y, True
    elif x - 1 > 0 and checkValidTile(x - 1, y):
        resultX, resultY, isValid = x - 1, y, True
    
    return resultX, resultY, isValid


def solveMaze(x, y):
    if maze[x][y] == 'g':
        return

    if maze[x][y] != 'X':
        maze[x][y] = '.'
    else:
        return
    
    steps = [(x, y)]
    isValidPath = True
    while True:
        x, y, isValidPath = chooseNext(x, y)

        if maze[x][y] == 'g':
            return

        if isValidPath:
            maze[x][y] = '.'
            steps.append((x, y))
        else:
            nextX, nextY, nextValid = chooseNext(x, y)
            if not nextValid:
                maze[x][y] = 'b'
            x, y = steps.pop()
            
            printMaze()
            print
    

def printMaze():
    for row in maze:
        print string.join(row)


solveMaze(1, 1)
printMaze()