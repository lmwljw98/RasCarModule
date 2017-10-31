# -*- coding: utf-8 -*-

from ForwardBackwardBase import *
from TurningCar import rightSwingTurn, leftSwingTurn, rightPointTurn, leftPointTurn
from UltraSensor import getDistance
import RPi.GPIO as GPIO
from time import sleep


# 과제 진행을 위한 실행파일

# firstStep ~ secondStep -> 과제3의 1차 과제 수행
def A3_firstStep():
    while True:
        try:
            distance = getDistance()
            if distance > 20:  # 장애물과 구동체 사이의 거리가 20 이상일 경우 계속 전진
                goForwardAny(30)
            else:
                stopCar()
                sleep(1)
                rightSwingTurn(35, 1)
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
            if distance > 20:
                goForwardAny(30)
            else:
                stopCar()
                sleep(1)
                rightPointTurn(35, 1)
                break

        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()


# thirdStep ~ fourthStep -> 과제3의 2차 과제 수행
def A3_thirdStep():
    while True:
        try:
            distance = getDistance()
            if distance > 20:
                goForwardAny(30)
            else:
                stopCar()
                sleep(1)
                leftPointTurn(27, 1)
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
                goForwardAny(30)
            else:
                stopCar()
                sleep(1)
                leftSwingTurn(35, 1)
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

    # 1차 과제 수행
    A3_firstStep()
    A3_secondStep()
    goForward(30, 1)
    stopCar()
    GPIO.cleanup()
    sleep(1)
    # 과제 수행 후 Stop

    # 아무 값이나 input 받으면 2차 과제 수행
    anything = raw_input()

    A3_thirdStep()
    A3_fourthStep()
    goForward(30, 1)
    stopCar()
    GPIO.cleanup()
except KeyboardInterrupt:
    stopCar()
    GPIO.cleanup()
