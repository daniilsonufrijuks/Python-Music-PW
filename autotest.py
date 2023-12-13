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
        play_sound("126_Fm_TheGridArpBass_02_550.wav")
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.5)
        play_sound("R8-Snare-3.wav")
        sleep(0.4)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.3)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.2)
        play_sound("R8-Snare-3.wav")
        sleep(0.5)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.5)
        play_sound("R8-Snare-3.wav")
        sleep(0.4)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.3)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.2)
        play_sound("R8-Snare-3.wav")
        sleep(0.1)
        play_sound("R8-Snare-3.wav")
        sleep(0.5)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.5)
        play_sound("R8-Snare-3.wav")
        sleep(0.4)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.3)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.2)
        play_sound("R8-Snare-3.wav")
        sleep(0.5)
        play_sound("cyborg-03-Plonk.wav")
        play_sound("126_Fm_TheGridArpBass_02_550.wav")
        sleep(0.5)
        play_sound("R8-Snare-3.wav")
        sleep(0.4)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.3)
        play_sound("cyborg-03-Plonk.wav")
        sleep(0.2)
        play_sound("R8-Snare-3.wav")
        sleep(0.1)
        play_sound("R8-Snare-3.wav")
        sleep(0.5)

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
        sleep(1)
        sleep(1)
        sleep(1)
        sleep(1)
        sleep(1)
        sleep(1)
        sleep(1)
        sleep(0.5)
        sleep(0.1)
    

def main():
    thread1 = Thread(target=drum_beat)
    thread2 = Thread(target=bass)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

main()