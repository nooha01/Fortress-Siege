import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Fortress Siege")
x = y = 250
radius = 15
run = True
vel = 10
while run:
    win.fill((0, 0, 0))

    pygame.draw.circle(win, (255, 255,255),(int(x), int(y)), radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        x -= vel
    if userInput[pygame.K_RIGHT]:
        x += vel
    if userInput[pygame.K_UP]:
        y -= vel
    if userInput[pygame.K_DOWN]:
        y += vel
    pygame.time.delay(10)
    pygame.display.update()