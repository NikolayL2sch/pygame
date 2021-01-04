import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption('my first game')

x = 350
y = 350
width = 40
height = 60
velocity = 5

isJump = False
jumpcnt = 10

run = True
while run:
    pygame.time.wait(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>=velocity:
        x-=velocity
    if keys[pygame.K_RIGHT] and x<=500-width-velocity:
        x+=velocity
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpcnt >= -10:
            neg = 1
            if jumpcnt < 0:
                neg = -1
            y-= (jumpcnt ** 2)*0.5 * neg
            jumpcnt-= 1 
        else:
            isJump = False
            jumpcnt = 10
    win.fill((0,0,0))    
    pygame.draw.rect(win,(229,111,190),(x,y,width,height))
    pygame.display.update()
pygame.quit()
