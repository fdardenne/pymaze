import pygame, numpy

def draw_board (maze, pygame,SQUARE_LENGTH):
    pygame.draw.rect(win, (0,0,0), (0,0,700,700))
    for x in range(len(maze)):
        for y in range(len(maze)):
            if maze[x][y] == 1:
                pygame.draw.rect(win, (0,255,0), (x*SQUARE_LENGTH,y*SQUARE_LENGTH,SQUARE_LENGTH,SQUARE_LENGTH))
            if maze[x][y] == 2:
                pygame.draw.rect(win, (255,255,255), (x*SQUARE_LENGTH,y*SQUARE_LENGTH,SQUARE_LENGTH,SQUARE_LENGTH))
            if maze[x][y] == 3:
                pygame.draw.rect(win, (255,0,0), (x*SQUARE_LENGTH,y*SQUARE_LENGTH,SQUARE_LENGTH,SQUARE_LENGTH))

def walls(maze):
    for x in range(len(maze)):
        maze[x][0] = 2
    for y in range(len(maze)):
        maze[0][y] = 2
    for x2 in range(len(maze)):
        maze[x2][len(maze)-1] = 2
    for y2 in range(len(maze)):
        maze[len(maze)-1][y2] = 2

def obstacle (maze, x, y, direction):
    if direction == 1:
        return maze[x+1][y] == 2
    if direction == 2:
        return maze[x-1][y] == 2
    if direction == 3:
        return maze[x][y-1] == 2
    if direction == 4:
        return maze[x][y+1] == 2

def game_over(maze, x, y, direction):
        if direction == 1:
            return maze[x+1][y] == 3

        if direction == 2:
            return maze[x-1][y] == 3
        if direction == 3:
            return maze[x][y-1] == 3
        if direction == 4:
            return maze[x][y+1] == 3

def load(filename, maze):
    file = open(filename, "r")
    text = file.read()
    line_list = text.split("\n")
    line_list.pop()
    for x in range(len(line_list)):
        if x == MAZE_SQUARE-2:
            break
        value_list = line_list[x].split(",")
        for y in range(len(value_list)):
            if y == MAZE_SQUARE-2:
                break
            maze[y+1][x+1] = value_list[y]
    file.close()


def save(filename, maze):
    file = open(filename, "w")
    text = ""
    for x in range(1,len(maze)-1):
        for y in range(1,len(maze[x])-1):
            text +=str( int(maze[y][x])) + ','
        text = text[:-1]
        text += "\n"

    file.write(text)
    file.close()

def find_player(maze):
    for x_pos in range(len(maze)):
        for y_pos in range(len(maze)):
            if maze[x_pos][y_pos] == 1:
                return x_pos, y_pos
    maze[1][1] = 1
    return 1,1

#In build mode you can create a level:
#click and mousemotion to place an obstacle or void
#the 'c' key to switch between void and obstacle
#when finished, close the game and your level will be saved
BUILD_MODE = True
FILE = "level1.dat"
MAZE_SQUARE = 20
SQUARE_LENGTH = int(700/MAZE_SQUARE)


pygame.init()
win = pygame.display.set_mode((700,700))
pygame.display.set_caption("PyMaze")
maze = numpy.zeros(shape = (MAZE_SQUARE,MAZE_SQUARE))

load(FILE,maze)
x,y = find_player(maze)
walls(maze)

build_var = 2
run = True
while run:
    draw_board(maze, pygame, SQUARE_LENGTH)

    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0] and BUILD_MODE:
            try:
                pos = pygame.mouse.get_pos()
                pos_x = int(pos[0]/SQUARE_LENGTH)
                pos_y = int(pos[1]/SQUARE_LENGTH)
                maze[pos_x][pos_y] = build_var
            except AttributeError:
                pass
        if keys[pygame.K_c] and BUILD_MODE:
            build_var = 2 if build_var==0 else 0
        if keys[pygame.K_UP]:
            if not obstacle(maze,x,y, 3):
                if game_over(maze,x,y,3):
                    run = False
                else:
                    maze[x][y] = 0
                    y-=1
                    maze[x][y] = 1
                    pygame.time.delay(10)

        elif keys[pygame.K_DOWN]:
            if not obstacle(maze,x,y, 4):
                if game_over(maze,x,y,4):
                    run = False
                else:
                    maze[x][y] = 0
                    y+=1
                    maze[x][y] = 1
                    pygame.time.delay(10)

        elif keys[pygame.K_LEFT]:
            if not obstacle(maze,x,y,2):
                if game_over(maze,x,y,2):
                    run = False
                else:
                    maze[x][y] = 0
                    x-=1
                    maze[x][y] = 1
                    pygame.time.delay(10)

        elif keys[pygame.K_RIGHT]:
            if not obstacle(maze,x,y, 1):
                if game_over(maze,x,y,1):
                    run = False
                else:
                    maze[x][y] = 0
                    x+=1
                    maze[x][y] = 1
                    pygame.time.delay(10)

    pygame.display.update()

#Save the matrix in a file if in BUILD_MODE
if BUILD_MODE:
    save(FILE, maze)
#Draw the Success screen
maze = numpy.zeros(shape=(MAZE_SQUARE,MAZE_SQUARE)) + 1
draw_board(maze, pygame, SQUARE_LENGTH)
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Success !", True, (0,0,0))
win.blit(text, (350-130, 350-72))
pygame.display.update()
pygame.time.delay(1000)

#Quit
pygame.quit()
