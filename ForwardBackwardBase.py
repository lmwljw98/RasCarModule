######################################################################
# Date : 2017/10 ~
# Member's Name : 이정우, 이정훈, 장민혁
# Member's ID : 20171676, 20171678, 20171691
# Module name: ForwardBackwardBase.py
# Purpose: 전진, 후진, 기본 셋업을 위한 모듈
######################################################################

# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

# Global Variables
##############################
# 본인 자동차 설정에 맞춰서 작성

MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 36

MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 38

##############################

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# 전역변수로 선언하여 다른 모듈에서 사용
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


def leftMotor(direction):
    """
    왼쪽 모터의 전/후진을 인자로 받아 조정하는 함수

    :param direction:
    :return:
    """
    if direction == 'forward':
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    elif direction == 'backward':
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)


def rightMotor(direction):
    """
    오른쪽 모터의 전/후진을 인자로 받아 조정하는 함수

    :param direction:
    :return:
    """
    if direction == 'forward':
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)


def goForward(speed, running_time):
    """
    구동체의 속도와 주행 시간을 인자로 받아 전진하는 함수

    :param speed:
    :param running_time:
    :return:
    """
    leftMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightMotor("forward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed * 1.025)
    sleep(running_time)


def goBackward(speed, running_time):
    """
    구동체의 속도와 주행 시간을 인자로 받아 후진하는 함수

    :param speed:
    :param running_time:
    :return:
    """
    leftMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightMotor("backward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed * 1.025)
    sleep(running_time)


def goForwardAny(speed):
    """
    멈추라는 명령이 있기 전까지 인자로 받은 속도로 계속 전진하는 함수

    :param speed:
    :return:
    """
    leftMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightMotor("forward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed * 1.025)


def goBackwardAny(speed):
    """
    멈추라는 명령이 있기 전까지 인자로 받은 속도로 계속 후진하는 함수

    :param speed:
    :return:
    """
    leftMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightMotor("backward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed * 1.025)


def stopCar():
    """
    구동체를 멈추는 함수

    :return:
    """
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)

    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


# 테스트용
if __name__ == "__main__":
    try:
        LeftPwm.start(0)
        RightPwm.start(0)
        goForward(60, 2)
        sleep(1)
        goBackward(60, 2)
        sleep(1)
        # command for stop
        stopCar()

    # when the Ctrl+C key has been pressed,
    # the moving object will be stopped
    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()
