# Created by Danila
# Synthesizer

import keyboard
from play_sound_by_pygame import play_sound

def synthesizer_pad():
    while True:
        # short piano notes
        if keyboard.is_pressed("q"):
            play_sound("316908__jaz_the_man_2__re.wav")
        if keyboard.is_pressed("w"):
            play_sound("316912__jaz_the_man_2__sol.wav")
        if keyboard.is_pressed("e"):
            play_sound("316913__jaz_the_man_2__si.wav")
        if keyboard.is_pressed("r"):
            play_sound("316901__jaz_the_man_2__do-octave.wav")

        # long piano notes
        if keyboard.is_pressed("a"):
            play_sound("316909__jaz_the_man_2__re-stretched.wav")
        if keyboard.is_pressed("s"):
            play_sound("316905__jaz_the_man_2__fa-stretched.wav")
        if keyboard.is_pressed("d"):
            play_sound("316903__jaz_the_man_2__la-stretched.wav")
        if keyboard.is_pressed("f"):
            play_sound("316900__jaz_the_man_2__do-stretched-octave.wav")

        # electronic sounds
        if keyboard.is_pressed("z"):
            play_sound("126_Fm_TheGridArpBass_02_550.wav")
        if keyboard.is_pressed("x"):
            play_sound("BlofeldCowbell_02_550.wav")
        if keyboard.is_pressed("c"):
            play_sound("Am_PhattyStabSynth_01_550.wav")
        if keyboard.is_pressed("v"):
            play_sound("F_PhattyStabSynth_02_550.wav")
