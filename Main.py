import Detector_pingBased as Detector


def send_message():
    print('someone has arrived')


counter = 0
while True:
    if Detector.detect_person():
        while Detector.detect_person():
            pass
        counter += 1
        send_message()