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
pygame.display.set_caption('Flappy Bird')
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
# player = pygame.FRect(50, HEIGHT / 2, 30, 30)
player_surf = pygame.image.load('assets/player.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (65, 65))
player = player_surf.get_frect(center = (50, HEIGHT / 2))

# masking
player_mask = pygame.mask.from_surface(player_surf)

pipe_surf = pygame.Surface((50, 310))
pipe_surf.fill(white)
pipe_bottom1_mask = pygame.mask.from_surface(pipe_surf)
pipe_top1_mask = pygame.mask.from_surface(pipe_surf)
pipe_bottom2_mask = pygame.mask.from_surface(pipe_surf)
pipe_top2_mask = pygame.mask.from_surface(pipe_surf)
# mask_image = pipe_top2_mask.to_surface()

# mask_image = player_mask.to_surface()
# mask_image1 = pipe_bottom1_mask.to_surface()

# pipes
pipe_bottom1 = pygame.FRect(200, HEIGHT - 150, 50, 310)
pipe_top1 = pygame.FRect(200, 0, 50, 310)
pipe_bottom2 = pygame.FRect(400, HEIGHT - 250, 50, 310)
pipe_top2 = pygame.FRect(400, -100, 50, 310)


# sounds
flap_sound = pygame.mixer.Sound('assets/flap.mp3')
die_sound = pygame.mixer.Sound('assets/die.mp3')
point_sound = pygame.mixer.Sound('assets/point.mp3')

# font
font = pygame.font.Font("freesansbold.ttf", 24)
score = 0

# functions
def offset(player, pipe):
    off = (pipe.x - player.x, pipe.y - player.y)
    return off



def player_ani(player):
    global score
    player.y += player_jump
    player.y += gravity
    player.x += player_speed
    
    # print(player.y)
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
    if player.top <= 0:
        player.top = 0 

    # collisions
    # if (abs(player.right - pipe_bottom1.left) <= 10) or (abs(player.right - pipe_bottom2.left) <= 10) or (abs(player.right - pipe_top1.left) <= 10) or (abs(player.right - pipe_top2.left) <= 10):
    #     if (abs(player.bottom - pipe_bottom1.top) <= 10) or (abs(player.bottom - pipe_bottom2.top) <= 10) or (abs(player.top - pipe_top1.bottom) <= 10) or (abs(player.top - pipe_top2.bottom) <= 10):
    

    # if (player.colliderect(pipe_bottom1) or player.colliderect(pipe_bottom2) or player.colliderect(pipe_top1) or player.colliderect(pipe_top2)):
    #             pygame.mixer.Sound.play(die_sound)
    #             reset()

    # mask collisions
    if (player_mask.overlap(pipe_bottom1_mask, offset(player, pipe_bottom1))) or (player_mask.overlap(pipe_bottom2_mask, offset(player, pipe_bottom2))) or (player_mask.overlap(pipe_top1_mask, offset(player, pipe_top1))) or (player_mask.overlap(pipe_top2_mask, offset(player, pipe_top2))):
        pygame.mixer.Sound.play(die_sound)
        reset()
    

    # pipes
    if player.right >= WIDTH:
        pygame.mixer.Sound.play(point_sound)
        player.x = 50
        score += 1
        
        pipe_1_x = random.randint(100, 250)
        pipe_2_x = random.randint(250, 450)

        if (pipe_1_x - pipe_2_x < 100):
            pipe_1_x = random.randint(100, 250)
            pipe_2_x = random.randint(250, 400)
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

        pipe_bottom1_y = random.randint(335, 450)
        pipe_top1_y = random.randint(200, 335)
        pipe_bottom2_y = random.randint(335, 450)
        pipe_top2_y = random.randint(200, 335)

    
        pipe_bottom1.top = pipe_bottom1_y
        pipe_top1.bottom = pipe_top1_y
        pipe_bottom2.top = pipe_bottom2_y
        pipe_top2.bottom = pipe_top2_y

    
        

def reset():
    global score
    player.x = 50
    player.y = HEIGHT / 2
    pipe_bottom1.left = 200
    pipe_top1.left = 200
    pipe_bottom2.left = 400
    pipe_top2.left = 400
    pipe_bottom1.top = HEIGHT - 150
    pipe_top1.top = 0
    pipe_bottom2.top = HEIGHT - 250
    pipe_top2.top = -100
    score = 0

# pipe_bottom1 = pygame.FRect(200, HEIGHT - 150, 50, 310)
# pipe_top1 = pygame.FRect(200, 0, 50, 310)
# pipe_bottom2 = pygame.FRect(400, HEIGHT - 250, 50, 310)
# pipe_top2 = pygame.FRect(400, -100, 50, 310)


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
    # score
    score_text = font.render(f'Score: {score}', False, grey)
    screen.blit(score_text, (WIDTH / 2 - 50, HEIGHT / 2))
    
    # player
    # player = screen.blit(player_surf, player)
    player_ani(player)
    # player.y += gravity
    
    # pygame.draw.rect(screen, white, pipe_bottom1)
    # pygame.draw.rect(screen, white, pipe_top1)
    # pygame.draw.rect(screen, white, pipe_bottom2)
    # pygame.draw.rect(screen, white, pipe_top2)
    
    # screen.blit(mask_image, (0, 0))
    # for i in range(2):
    #     pipes.append(pipe_bottom)
    # for pipe in pipes:
    #     pygame.draw.rect(screen, black, pipe)

    screen.blit(player_surf, player)
    screen.blit(pipe_surf, pipe_bottom1)
    screen.blit(pipe_surf, pipe_top1)
    screen.blit(pipe_surf, pipe_bottom2)
    screen.blit(pipe_surf, pipe_top2)
    
    # screen.blit(mask_image, player)
    # screen.blit(mask_image1, pipe_bottom1)


    # update display
    pygame.display.flip()

# quit
pygame.quit()