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
        LeftPwm.ChangeDutyCycle(0)
        RightPwm.ChangeDutyCycle(0)
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
    GPIO.output(MotorLeft_A, GPIO.LOW)
    GPIO.output(MotorLeft_B, GPIO.HIGH)
    GPIO.output(MotorRight_A, GPIO.HIGH)
    GPIO.output(MotorRight_B, GPIO.LOW)
    # goForwardAny(speed)
    # while True:
    try:
        led_list = track()
        if led_list[0] and not (led_list[4]):
            LeftPwm.ChangeDutyCycle(speed + 85)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[1] and not (led_list[3]):
            LeftPwm.ChangeDutyCycle(speed + 65)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[3] and not (led_list[1]):
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 40)
        if led_list[4] and not (led_list[0]):
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 60)

        if led_list[0] and led_list[1] and not led_list[3]:
            LeftPwm.ChangeDutyCycle(speed + 85)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[3] and led_list[4] and not led_list[1]:
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 60)

        if not led_list[0] and not led_list[1] and not led_list[2] and not led_list[3] and not led_list[4]:
            stopCar()
            GPIO.cleanup()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()


def start():
    goForwardAny(speed)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    while True:
        if getDistance() < 20:
            avoid()
            LeftPwm.ChangeDutyCycle(0)
            RightPwm.ChangeDutyCycle(0)
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
        start()
        # start2()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()
