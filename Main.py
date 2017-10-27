from ForwardBackwardBase import *
from TurningCar import rightSwingTurn, leftSwingTurn, rightPointTurn, leftPointTurn
from UltraSensor import getDistance
import RPi.GPIO as GPIO
from time import sleep


def A3_firstStep():
    while True:
        try:
            distance = getDistance()
            if distance > 30:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                rightSwingTurn(50, 1)
                break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()


def A3_secondStep():
    while True:
        try:
            distance = getDistance()
            if distance > 30:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                rightPointTurn(50, 1)
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
            if distance > 30:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                leftPointTurn(50, 1)
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
            if distance > 30:
                goForwardAny(40)
            else:
                stopCar()
                sleep(1)
                leftSwingTurn(50, 1)
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

    A3_firstStep()
    A3_secondStep()
    goForward(25, 3)

    A3_thirdStep()
    A3_fourthStep()
    goForward(25, 3)
except KeyboardInterrupt:
    stopCar()
    GPIO.cleanup()