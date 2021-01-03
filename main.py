import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption('my first game')

x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.wait(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=velocity
    if keys[pygame.K_RIGHT]:
        x+=velocity
    if keys[pygame.K_DOWN]:
        y+=velocity
    if keys[pygame.K_UP]:
        y-=velocity
    win.fill((0,0,0))    
    pygame.draw.rect(win,(229,111,190),(x,y,width,height))
    pygame.display.update()
pygame.quit()