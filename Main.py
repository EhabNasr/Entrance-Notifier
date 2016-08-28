import Detector_PIR_Based as Detector
from pygame import mixer
import time


def send_message():
    print('someone has arrived')


mixer.init()
alert = mixer.Sound('bell.wav')
alert.play()
counter = 0
while True:
#    print(Detector.detect_person())
    if Detector.detect_person():
        alert.play()
        time.sleep(0.5)
#        while Detector.detect_person():
#            pass
        counter += 1
        send_message()
        print(counter)

