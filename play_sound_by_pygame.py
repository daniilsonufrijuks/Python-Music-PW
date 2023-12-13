import pygame

def play_sound(file_path):
    pygame.mixer.init()
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except pygame.error as e:
        print("Error:", e)