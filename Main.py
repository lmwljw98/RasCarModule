from ForwardBackwardBase import *
from TurningCar import rightSwingTurn, leftSwingTurn, rightPointTurn, leftPointTurn
from UltraSensor import getDistance
import RPi.GPIO as GPIO
from time import sleep


def A3_firstStep(speed):
    while True:
        try:
            distance = getDistance()
            if distance > 20:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                #rightSwingTurn(43, 1)
                rightSwingTurn(speed, 1)
                break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()


def A3_secondStep(speed):
    while True:
        try:
            distance = getDistance()
            if distance > 20:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                #rightPointTurn(43, 1)
                rightPointTurn(speed, 1)
                break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()


def A3_thirdStep():
    while True:
        try:
            distance = getDistance()
            if distance > 20:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                leftPointTurn(43, 1)
                break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()


def A3_fourthStep():
    while True:
        try:
            distance = getDistance()
            if distance > 20:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                leftSwingTurn(43, 1)
                break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()

try:
    # set up GPIO mode as BOARD
    GPIO.setmode(GPIO.BOARD)
    baseSetup()
    LeftPwm.start(0)
    RightPwm.start(0)
    speed = int(raw_input())
    A3_firstStep(speed)
    A3_secondStep(speed)
    goForward(40, 1)
    sleep(1)
    raw_input()
    A3_thirdStep()
    A3_fourthStep()
    goForward(40, 1)
    stopCar()
    GPIO.cleanup()
except KeyboardInterrupt:
    stopCar()
    GPIO.cleanup()