# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

##############################
# 본인 자동차 설정에 맞춰서 작성
left1 = 18
left2 = 26
center = 24
right2 = 40
right1 = 32
##############################

GPIO.setup(left1, GPIO.IN)
GPIO.setup(left2, GPIO.IN)
GPIO.setup(center, GPIO.IN)
GPIO.setup(right2, GPIO.IN)
GPIO.setup(right1, GPIO.IN)


def track():

    return GPIO.input(left1), GPIO.input(left2), GPIO.input(center), GPIO.input(right2), GPIO.input(right1)


if __name__ == "__main__":
    try:
        while True:
            print("leftmostled  detects black line(0) or white ground(1): " + str(GPIO.input(left1)))
            print("leftlessled  detects black line(0) or white ground(1): " + str(GPIO.input(left2)))
            print("centerled    detects black line(0) or white ground(1): " + str(GPIO.input(center)))
            print("rightlessled detects black line(0) or white ground(1): " + str(GPIO.input(right2)))
            print("rightmostled detects black line(0) or white ground(1): " + str(GPIO.input(right1)))
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
