import pygame
import os

os.chdir('C:/Users/nikol_000/Desktop/python_game')
retval = os.getcwd()

print ("Directory changed successfully %s" % retval)
pygame.init()

win = pygame.display.set_mode((1920,1080))

pygame.display.set_caption('my first game')

runl = [pygame.transform.flip(pygame.image.load('pics/run0.png'), True, False),
pygame.transform.flip(pygame.image.load('pics/run1.png'), True, False),
pygame.transform.flip(pygame.image.load('pics/run2.png'), True, False), 
pygame.transform.flip(pygame.image.load('pics/run3.png'), True, False),
pygame.transform.flip(pygame.image.load('pics/run4.png'), True, False), 
pygame.transform.flip(pygame.image.load('pics/run5.png'), True, False)]

runr = [pygame.image.load('pics/run0.png'), pygame.image.load('pics/run1.png'),
pygame.image.load('pics/run2.png'), pygame.image.load('pics/run3.png'),
pygame.image.load('pics/run4.png'), pygame.image.load('pics/run5.png')]

jump = [pygame.image.load('pics/jump0.png'), pygame.image.load('pics/jump1.png'),
pygame.image.load('pics/jump2.png'), pygame.image.load('pics/jump3.png')]

bg = pygame.image.load('bg.png')

idle = [pygame.image.load('pics/idle0.png'), pygame.image.load('pics/idle1.png'),
pygame.image.load('pics/idle2.png'), pygame.image.load('pics/idle3.png')]

clock = pygame.time.Clock()

x = 100
y = 600
width = 50
height = 37
velocity = 20

isJump = False
jumpcnt = 10
left = False
right = False
walkCount = 0
idleCount = 0
jumpCount = 0

def redraw_Win():
    global walkCount, idleCount,jumpCount
    win.blit(bg,(0,0))    
    if walkCount +1 >= 60:
        walkCount = 0
    if left:
        win.blit(runl[walkCount//10],(x,y))
        walkCount+=1
    elif right:
        win.blit(runr[walkCount//10],(x,y))
        walkCount+=1
    elif Idle:
        if idleCount + 1 > 60:
            idleCount = 0
        else:
            win.blit(idle[idleCount//15],(x,y))
            idleCount+=1
    else:
        if jumpCount + 1 > 60:
            jumpCount = 0
        else:
            win.blit(jump[jumpCount//15],(x,y))
            jumpCount+=1

    pygame.display.update()

#mainloop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>=velocity:
        x-=velocity
        left = True
        right = False
        idleCount = 0
        Idle = False
    elif keys[pygame.K_RIGHT] and x<=700-width-velocity:
        x+=velocity
        right = True
        left = False
        idleCount = 0
        Idle = False
    else:
        right = False
        left = False
        walkCount = 0
        Idle = True
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
            idleCount = 0
            Idle = False
    else:
        if jumpcnt >= -10:
            neg = 1
            if jumpcnt < 0:
                neg = -1
            y-= 2*(jumpcnt ** 2)*0.5 * neg
            jumpcnt-= 1 
        else:
            isJump = False
            jumpcnt = 10
    redraw_Win()
pygame.quit()
