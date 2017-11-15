# -*- coding: utf-8 -*-

from ForwardBackwardBase import *
from TurningCar import rightPointTurn, leftPointTurn
from UltraSensor import getDistance
from Tracking import track
import RPi.GPIO as GPIO
from time import sleep

speed = 20


def avoid():
    try:
        stopCar()
        sleep(1)
        rightPointTurn(30, 1)
        sleep(1)
        goForward(30, 1.5)
        sleep(1)
        leftPointTurn(30, 2)
        sleep(1)
        goForwardAny(speed)
    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()


def lineTrace():
    # goForwardAny(speed)
    # while True:
    try:
        led_list = track()
        if led_list[0] and not (led_list[4]):
            LeftPwm.ChangeDutyCycle(speed + 75)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[1] and not (led_list[3]):
            LeftPwm.ChangeDutyCycle(speed + 55)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[3] and not (led_list[1]):
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 30)
        if led_list[4] and not (led_list[0]):
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 50)

        if led_list[0] and led_list[1] and not led_list[3]:
            LeftPwm.ChangeDutyCycle(speed + 75)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[3] and led_list[4] and not led_list[1]:
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 50)

        if not led_list[0] and not led_list[1] and not led_list[2] and not led_list[3] and not led_list[4]:
            stopCar()
            GPIO.cleanup()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()


def start():
    goForwardAny(speed)
    while True:
        if getDistance() < 20:
            avoid()
        else:
            lineTrace()

def start2():
    goForwardAny(speed)
    while True:
        lineTrace()


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    # 과제 진행
    try:
        LeftPwm.start(0)
        RightPwm.start(0)
        goForward(speed, 0.3)
        start2()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()
