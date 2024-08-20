import pygame
import random
# import pygame.camera
# import pygame.freetype


# general setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
# pygame.camera.init()


WIDTH = 500
HEIGHT = 670

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# colors
black = (0, 0, 0)
grey = pygame.Color('grey12')
white = (255, 255, 255)
background = pygame.image.load('assets/background.jpg')
bg_x = 0
bg_y =  0

# pos variables
player_jump = 0
player_speed = 1
gravity = 1.5


# rects
player = pygame.FRect(50, HEIGHT / 2, 30, 30)
pipe_bottom1 = pygame.FRect(200, HEIGHT - 250, 50, 320)
pipe_top1 = pygame.FRect(200, 0, 50, 320)
pipe_bottom2 = pygame.FRect(400, HEIGHT - 250, 50, 320)
pipe_top2 = pygame.FRect(400, 0, 50, 320)

# sounds
flap_sound = pygame.mixer.Sound('assets/flap.mp3')
die_sound = pygame.mixer.Sound('assets/die.mp3')
point_sound = pygame.mixer.Sound('assets/point.mp3')

# functions
def player_ani(player):
    player.y += player_jump
    player.y += gravity
    player.x += player_speed
    
    # print(player.y)
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
    if player.top <= 0:
        player.top = 0 

    # collisions
    if player.colliderect(pipe_bottom1) or player.colliderect(pipe_bottom2) or player.colliderect(pipe_top1) or player.colliderect(pipe_top2):
        pygame.mixer.Sound.play(die_sound)
        player.x = 50

    # pipes
    if player.right >= WIDTH:
        pygame.mixer.Sound.play(point_sound)
        player.x = 50
        
        pipe_1_x = random.randint(100, 250)
        pipe_2_x = random.randint(250, 450)

        if (pipe_1_x - pipe_2_x < 100):
            pipe_1_x = random.randint(100, 250)
            pipe_2_x = random.randint(250, 400)

        # while (pipe_1 - pipe_2 < 100) or (pipe_1 < 100) or (pipe_2 < 100):
        #     pipe_1 = random.randint(100, 250)
        #     pipe_2 = random.randint(250, 400)

        pipe_bottom1.x = pipe_1_x
        pipe_top1.x = pipe_1_x
        
        pipe_bottom2.x = pipe_2_x
        pipe_top2.x = pipe_2_x

        pipe_bottom1_y = random.randint(335, HEIGHT)
        pipe_top1_y = random.randint(0, 335)
        pipe_bottom2_y = random.randint(335, HEIGHT)
        pipe_top2_y = random.randint(0, 335)

    
        pipe_bottom1.top = pipe_bottom1_y
        pipe_top1.bottom = pipe_top1_y
        pipe_bottom2.top = pipe_bottom2_y
        pipe_top2.bottom = pipe_top2_y

        

    


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
                pygame.mixer.Sound.play(flap_sound)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # player.y += gravity
                player_jump += 10
                

    # display
    screen.fill(grey)
    # bg_x += 1
    # print(bg_x)
    # screen.blit(background, (bg_x, 0))
    
    # moving background
    bg_y -= 0.5
    if bg_y <= -1000:
        bg_y = -500
    screen.blit(background, (bg_y, 0))
    # player
    player = pygame.draw.rect(screen, white, player, 0, 12)
    player_ani(player)
    # player.y += gravity
    pygame.draw.rect(screen, white, pipe_bottom1)
    pygame.draw.rect(screen, white, pipe_top1)
    pygame.draw.rect(screen, white, pipe_bottom2)
    pygame.draw.rect(screen, white, pipe_top2)

    # for i in range(2):
    #     pipes.append(pipe_bottom)
    # for pipe in pipes:
    #     pygame.draw.rect(screen, black, pipe)


    # update display
    pygame.display.flip()

# quit
pygame.quit()