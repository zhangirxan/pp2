import pygame
import os

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

background_image = pygame.image.load("nigga.jpg")
music_directory = "C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis7\\music"
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]
current_index = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_index]))

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
        elif event.type == pygame.QUIT:
            running = False

    screen.blit(pygame.transform.scale(background_image, (width, height)), (0, 0))
    pygame.display.flip()
pygame.quit()
