######################################################################
# Date : 2017/10 ~
# Member's Name : 이정우, 이정훈, 장민혁
# Member's ID : 20171676, 20171678, 20171691
# Module name: TurningCar.py
# Purpose: 자동차의 턴 함수 모듈
######################################################################

# -*- coding: utf-8 -*-

from ForwardBackwardBase import *
import RPi.GPIO as GPIO
from time import sleep


def rightSwingTurn(speed, running_time):
    """
    오른쪽으로 스윙턴 하는 함수

    :param speed:
    :param running_time:
    :return:
    """
    leftMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.LOW)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(0)

    sleep(running_time)


def leftSwingTurn(speed, running_time):
    """
    왼쪽으로 스윙턴 하는 함수

    :param speed:
    :param running_time:
    :return:
    """
    rightMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


def rightPointTurn(speed, running_time):
    """
    오른쪽으로 포인트턴 하는 함수

    :param speed:
    :param running_time:
    :return:
    """
    leftMotor("forward")
    rightMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


def leftPointTurn(speed, running_time):
    """
    왼쪽으로 포인트턴 하는 함수

    :param speed:
    :param running_time:
    :return:
    """
    leftMotor("backward")
    rightMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


# 모듈 테스트
if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    baseSetup()
    try:
        LeftPwm.start(0)
        RightPwm.start(0)

        rightSwingTurn(45, 2)
        sleep(2)
        leftPointTurn(45, 2)
        sleep(2)
        rightPointTurn(45, 2)
        sleep(2)
        leftPointTurn(45, 2)

    except KeyboardInterrupt:
        stopCar()
