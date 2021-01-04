import pygame
import os

os.chdir('C:/Users/nikol_000/Desktop/python_game')
retval = os.getcwd()

print ("Directory changed successfully %s" % retval)
pygame.init()

win = pygame.display.set_mode((500,500))

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

bg = pygame.image.load('pics/bg.jpg')

idle = [pygame.image.load('pics/idle0.png'), pygame.image.load('pics/idle1.png'),
pygame.image.load('pics/idle2.png'), pygame.image.load('pics/idle3.png')]

clock = pygame.time.Clock()

x = 350
y = 350
width = 50
height = 37
velocity = 5

isJump = False
jumpcnt = 10
left = False
right = False
walkCount = 0
idleCount = 0


def redraw_Win():
    global walkCount, idleCount
    win.blit(bg,(0,0))    
    if walkCount +1 >= 30:
        walkCount = 0
        idleCount = 0
    if left:
        win.blit(runl[walkCount//5],(x,y))
        walkCount+=1
    elif right:
        win.blit(runr[walkCount//5],(x,y))
        walkCount+=1
    elif Idle:
        if idleCount>3:
            idleCount%=3
        win.blit(idle[idleCount//3],(x,y))
        idleCount+=1
    pygame.display.update()

#mainloop
run = True
while run:
    clock.tick(30)

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
    elif keys[pygame.K_RIGHT] and x<=500-width-velocity:
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
            y-= (jumpcnt ** 2)*0.5 * neg
            jumpcnt-= 1 
        else:
            isJump = False
            jumpcnt = 10
    redraw_Win()
pygame.quit()
