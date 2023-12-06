# Created by Dan 
# Drum Pad machine

import keyboard
import pygame

def play_sound(file_path):
    pygame.mixer.init()
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except pygame.error as e:
        print("Ошибка воспроизведения звука:", e)

def drum_pad():
    while True:
        if keyboard.is_pressed("7"):
            play_sound("R8-Conga.wav")
        if keyboard.is_pressed("8"):
            play_sound("R8-Kick-2.wav")
        if keyboard.is_pressed("9"):
            play_sound("cyborg-06-MetalTwang2.wav")
        if keyboard.is_pressed("4"):
            play_sound("R8-Low-Tom.wav")
        if keyboard.is_pressed("5"):
            play_sound("R8-Snare-3.wav")
        if keyboard.is_pressed("6"):
            play_sound("voxy-SNARE1.wav")
        if keyboard.is_pressed("1"):
            play_sound("cyborg-03-Plonk.wav")
        if keyboard.is_pressed("2"):
            play_sound("cyborg-05-TTweat.wav")
        if keyboard.is_pressed("3"):
            play_sound("cyborg-06-Warp.wav")

