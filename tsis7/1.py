import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
clock = pygame.time.Clock()
main_clock = pygame.image.load("mickey.png")
minute_hand = pygame.image.load("right.png")
second_hand = pygame.image.load("left.png")
main_clock = pygame.transform.scale(main_clock, (500, 400))
hand_scale_factor = 0.5
minute_hand = pygame.transform.scale(minute_hand, (int(minute_hand.get_width() * hand_scale_factor), int(minute_hand.get_height() * hand_scale_factor)))
second_hand = pygame.transform.scale(second_hand, (int(second_hand.get_width() * hand_scale_factor), int(second_hand.get_height() * hand_scale_factor)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    current_time = datetime.datetime.now()
    minute_angle = -6 * ((current_time.minute + current_time.second / 60) * 6)
    second_angle = -6 * current_time.second 

    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)

    screen.blit(main_clock, main_clock.get_rect(center=screen.get_rect().center))
    screen.blit(rotated_minute_hand, rotated_minute_hand.get_rect(center=screen.get_rect().center))
    screen.blit(rotated_second_hand, rotated_second_hand.get_rect(center=screen.get_rect().center))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
