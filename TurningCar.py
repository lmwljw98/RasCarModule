# -*- coding: utf-8 -*-

from ForwardBackwardBase import *
import RPi.GPIO as GPIO
from time import sleep


# 구동체의 턴 관련 함수가 포함된 모듈

# 오른쪽으로 스윙턴 하는 함수
def rightSwingTurn(speed, running_time):
    leftMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.LOW)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(0)

    sleep(running_time)


# 왼쪽으로 스윙턴 하는 함수
def leftSwingTurn(speed, running_time):
    rightMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


# 오른쪽으로 포인트턴 하는 함수
def rightPointTurn(speed, running_time):
    leftMotor("forward")
    rightMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


# 왼쪽으로 포인트턴 하는 함수
def leftPointTurn(speed, running_time):
    leftMotor("backward")
    rightMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


# 모듈 테스트
if __name__ == "__main__":
    # set up GPIO mode as BOARD
    GPIO.setmode(GPIO.BOARD)
    baseSetup()
    try:
        LeftPwm.start(0)
        RightPwm.start(0)

        rightSwingTurn(45, 2)
        sleep(2)
        leftSwingTurn(45, 2)
        sleep(2)
        rightPointTurn(45, 2)
        sleep(2)
        leftPointTurn(45, 2)

    except KeyboardInterrupt:
        stopCar()
