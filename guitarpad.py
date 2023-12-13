# Created by Ralph
# Guitar Pad Machine

import keyboard
from play_sound_by_pygame import play_sound

def guitar_pad():
    while True:
        if keyboard.is_pressed("h"):
            play_sound("guitar-single-note-d_120bpm_C_minor.wav")
        if keyboard.is_pressed("j"):
            play_sound("guitar-single-note-c-2_120bpm_C_minor.wav")
        if keyboard.is_pressed("k"):
            play_sound("guitar-single-note-b_120bpm_C_minor.wav")
        if keyboard.is_pressed("l"):
            play_sound("guitar-single-note-g-sharp-3_120bpm_C_minor.wav")
        if keyboard.is_pressed("u"):
            play_sound("guitar-single-note-c_120bpm_C_minor.wav")