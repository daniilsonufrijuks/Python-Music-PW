# main file

from drumpad import drum_pad
from synthesizer import synthesizer_pad
from guitarpad import guitar_pad
from threading import Thread


def main():
    thread1 = Thread(target=drum_pad)
    thread2 = Thread(target=synthesizer_pad)
    thread3 = Thread(target=guitar_pad)
    #drum_pad()
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()


main()