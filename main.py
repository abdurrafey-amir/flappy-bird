import pygame


# general setup
pygame.init()

WIDTH = 500
HEIGHT = 670

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# colors
black = (0, 0, 0)
grey = pygame.Color('grey12')
white = (255, 255, 255)

# pos variables
player_jump = 0
gravity = 1


# rects
player = pygame.Rect(50, HEIGHT / 2, 30, 30)
pipe_bottom = pygame.Rect(100, HEIGHT - 50, 50, 50)
pipes = []

# functions
def player_ani(player):
    player.y += player_jump
    player.y += gravity
    # print(player.y)
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
    if player.top <= 0:
        player.top = 0 

    


# main loop
running = True
while running:
    # fps
    clock.tick(60)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_jump -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # player.y += gravity
                player_jump += 10
                

    # display
    screen.fill(grey)
    # player
    player = pygame.draw.rect(screen, white, player, 0, 12)
    player_ani(player)
    # player.y += gravity

    for i in range(2):
        pipes.append(pipe_bottom)
    for pipe in pipes:
        pygame.draw.rect(screen, black, pipe)


    # update display
    pygame.display.flip()

# quit
pygame.quit()