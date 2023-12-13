# . - 0.1 секунды
# / - 0.5 секунды

# {
# Z1/5....1...1..5/1/ 5 .... 1 ... 1 .. 5 . 5 / 1 / 5 .... 1 ... 1 .. 5 / 1Z / 5 .... 1 ... 1 .. 5.5/
# }
from play_sound_by_pygame import play_sound
from threading import Thread
from time import sleep


def drum_beat():
    # drum_beat_sample = "1/5/1....1..5/.1/5/1....1..5..5...1/5/1....1..5/.1/5/1....1..5..5..."
    while True:
        # for i in drum_beat_sample:
        #     if i == '.':
        #         time.sleep(0.1)
        #     if i == '/':
        #         time.sleep(0.5)
        #     if i == '1':
        #         play_sound("cyborg-03-Plonk.wav")
        #     if i == '5':
        #         play_sound("R8-Snare-3.wav")
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.5)
        play_sound("R8-Snare-3.wav")
        sleep(0.5)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.3)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.2)
        play_sound("R8-Snare-3.wav")
        sleep(0.5)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.5)
        play_sound("R8-Snare-3.wav")
        sleep(0.5)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.3)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.2)
        play_sound("R8-Snare-3.wav")
        sleep(0.2)
        play_sound("R8-Snare-3.wav")
        sleep(0.3)

def bass():
    #bass_sample = "z!!!!!!!/."
    while True:
        # for i in bass_sample:
        #     if i == '.':
        #         time.sleep(0.1)
        #     if i == '/':
        #         time.sleep(0.5)
        #     if i =='!':
        #         time.sleep(1)
        #     if i == 'z':
        #         play_sound("126_Fm_TheGridArpBass_02_550.wav")
        play_sound("126_Fm_TheGridArpBass_02_550.wav")
        sleep(7.8)

def cymbals():
    while True:
        play_sound("11_HiHats_02_34_SP.wav")
        sleep(0.5)


def guitars():
    while True:
        play_sound("guitar-single-note-c_120bpm_C_minor.wav")
        play_sound("guitar-single-note-c-2_120bpm_C_minor.wav")
        sleep(2)
        play_sound("guitar-single-note-d_120bpm_C_minor.wav")
        play_sound("guitar-single-note-g-sharp-3_120bpm_C_minor.wav")
        sleep(2)
        play_sound("guitar-single-note-c-2_120bpm_C_minor.wav")
        sleep(2)
        play_sound("guitar-single-note-c_120bpm_C_minor.wav")
        sleep(1)
        play_sound("guitar-single-note-c-2_120bpm_C_minor.wav")
        sleep(1)
    

def main():
    threadDrums = Thread(target=drum_beat)
    thread2Bass = Thread(target=bass)
    threadCymbals = Thread(target=cymbals)
    threadGuitar = Thread(target=guitars)

    threadDrums.start()
    thread2Bass.start()
    threadCymbals.start()
    threadGuitar.start()

    threadDrums.join()
    thread2Bass.join()
    threadCymbals.join()
    threadGuitar.join()

main()