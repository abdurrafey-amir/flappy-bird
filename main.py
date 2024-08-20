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
player_x = 50
player_y = HEIGHT / 2
player_jump = 0
gravity = -1 

# functions
def player_render(x, y):
    player_rect = pygame.Rect(x, y, 30, 30)
    player = pygame.draw.rect(screen, white, player_rect, 0, 12)
    return player

def player_ani(player):
    player.y += player_jump
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
                player_jump += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.y += gravity

    # display
    screen.fill(grey)
    # player
    player = player_render(player_x, player_y)
    player_ani(player)
    player.y += gravity


    # update display
    pygame.display.flip()

# quit
pygame.quit()