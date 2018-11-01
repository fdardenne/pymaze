import pygame, numpy

pygame.init()
win = pygame.display.set_mode((700,700))
pygame.display.set_caption("PySnake")

maze = numpy.zeros(shape = (10,10))
x = 0
y = 4
maze[x][y] = 1
square = 70

#Creation d'obstacle
for y_case in range(9):
    maze[3][y_case] = 2
maze[9][9] = 3

def draw_board (maze, pygame,square):
    pygame.draw.rect(win, (0,0,0), (0,0,700,700))
    for x in range(len(maze)):
        for y in range(len(maze)):
            if maze[x][y] == 1:
                pygame.draw.rect(win, (0,255,0), (x*square,y*square,square,square))
            if maze[x][y] == 2:
                pygame.draw.rect(win, (255,255,255), (x*square,y*square,square,square))
            if maze[x][y] == 3:
                pygame.draw.rect(win, (255,0,0), (x*square,y*square,square,square))

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
    text = fichier.read()
    line_list = text.split("\n")
    for x in range(1,len(line_list)):
        value_list = line_list[x].split(",")
        for y in range(1,len(value_list)):
            maze[x][y] = value_list[y]

walls(maze)
run = True
while run:
    draw_board(maze, pygame, square)

    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_UP]:
            if not obstacle(maze,x,y, 3):
                if game_over(maze,x,y,3):
                    run = false
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

        #2:UP 3:DOWN 1:LEFT 0:RIGHT



maze    = numpy.zeros(shape=(10,10)) + 3
draw_board(maze, pygame, square)
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Game Over", True, (0,0,0))
win.blit(text, (350-130, 350-72))

pygame.display.update()
pygame.time.delay(1000)

pygame.quit()
