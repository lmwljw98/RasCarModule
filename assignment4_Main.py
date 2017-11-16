# -*- coding: utf-8 -*-

from ForwardBackwardBase import *
from TurningCar import rightPointTurn, leftPointTurn
from UltraSensor import getDistance
from Tracking import track
import RPi.GPIO as GPIO
from time import sleep

speed = 15


def avoid():
    try:
        LeftPwm.ChangeDutyCycle(0)
        RightPwm.ChangeDutyCycle(0)
        sleep(1)
        ##########################################
        # 상황에 따라서 다르기 때문에 각자 조절해야함
        rightPointTurn(35, 1)
        sleep(1)
        goForward(30, 1.5)
        leftPointTurn(35, 2)
        ##########################################
        sleep(1.5)
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
            # print 'a'
            LeftPwm.ChangeDutyCycle(speed + 75)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[1] and not (led_list[3]):
            # print 'b'
            LeftPwm.ChangeDutyCycle(speed + 65)
            RightPwm.ChangeDutyCycle(speed)
        if led_list[3] and not (led_list[1]):
            # print 'c'
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 40)
        if led_list[4] and not (led_list[0]):
            # print 'd'
            LeftPwm.ChangeDutyCycle(speed)
            RightPwm.ChangeDutyCycle(speed + 60)

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()


def start():
    try:
        goForwardAny(speed)
        while True:
            a = getDistance()
            if a > 22:
                lineTrace()
            else:
                # print 'avoid'
                avoid()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()


def start2():
    goForwardAny(speed)
    while True:
        lineTrace()


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(MotorLeft_A, GPIO.OUT)
    GPIO.setup(MotorLeft_B, GPIO.OUT)
    GPIO.setup(MotorLeft_PWM, GPIO.OUT)

    GPIO.setup(MotorRight_A, GPIO.OUT)
    GPIO.setup(MotorRight_B, GPIO.OUT)
    GPIO.setup(MotorRight_PWM, GPIO.OUT)

    # 과제 진행
    try:
        LeftPwm.start(0)
        RightPwm.start(0)
        goForward(speed, 0.3)
        start()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()
