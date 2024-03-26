import pygame
import sys
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Japan")

radius = 25
ball_pos = [width//2, height//2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += 20
    elif keys[pygame.K_LEFT]:
        ball_pos[0] -= 20
    elif keys[pygame.K_UP]:
        ball_pos[1] -= 20
    elif keys[pygame.K_DOWN]:
        ball_pos[1] += 20

    ball_pos[0] = max(radius, min(width - radius, ball_pos[0]))
    ball_pos[1] = max(radius, min(height - radius, ball_pos[1]))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
