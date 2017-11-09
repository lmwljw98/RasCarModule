# -*- coding: utf-8 -*-

from ForwardBackwardBase import *
from TurningCar import rightPointTurn, leftPointTurn
from UltraSensor import getDistance
import RPi.GPIO as GPIO
from time import sleep
from Tracking import track

speed = 20


def avoid_and_lineTrace():
    while True:
        try:
            distance = getDistance()
            if distance > 20:
                led_list = track()
                if led_list[2] == 0:
                    goForwardAny(speed)
                if led_list[0] and not (led_list[4]):
                    goForwardAny_LR(speed + 30, speed)
                if led_list[1] and not (led_list[3]):
                    goForwardAny_LR(speed + 15, speed)
                if led_list[3] and not (led_list[1]):
                    goForwardAny_LR(speed, speed + 15)
                if led_list[4] and not (led_list[0]):
                    goForwardAny_LR(speed, speed + 30)

                if not led_list[0] and not led_list[1] and not led_list[2] and not led_list[3] and not led_list[4]:
                    stopCar()
                    GPIO.cleanup()
                    break
            else:
                stopCar()
                sleep(1)
                rightPointTurn(30, 1)
                sleep(1)
                goForward(30, 1.2)
                sleep(1)
                leftPointTurn(30, 1)
                sleep(1)
                goForward(30, 1.2)
                break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()


def lineTrace():
    while True:
        led_list = track()
        if led_list[2] == 0:
            goForwardAny(speed)
        if led_list[0] and not (led_list[4]):
            goForwardAny_LR(speed + 30, speed)
        if led_list[1] and not (led_list[3]):
            goForwardAny_LR(speed + 15, speed)
        if led_list[3] and not (led_list[1]):
            goForwardAny_LR(speed, speed + 15)
        if led_list[4] and not (led_list[0]):
            goForwardAny_LR(speed, speed + 30)

        if not led_list[0] and not led_list[1] and not led_list[2] and not led_list[3] and not led_list[4]:
            stopCar()
            GPIO.cleanup()
            break


if __name__ == "__main__":
    # 과제 진행
    try:
        GPIO.setmode(GPIO.BOARD)
        baseSetup()
        LeftPwm.start(0)
        RightPwm.start(0)

        lineTrace()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()
