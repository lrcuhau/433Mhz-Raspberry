import time
import sys
import RPi.GPIO as GPIO
print ("Start")


delay = 0.000001

NUM_ATTEMPTS = 10
TRANSMIT_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANSMIT_PIN, GPIO.OUT)


with open("/home/pi/NAS_Daten/out_V2.csv") as characters:
    print("Anfang1")
    for character in characters.read():
#        print(character)
        if character == '1':   
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(delay)
        elif character == '0':
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(delay)
        else:
            continue
    print("Ende1")

GPIO.cleanup()
