# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

# 기본적인 Setup과 구동체의 전/후진과 관련된 함수가 포함된 모듈

# Global Variables
MotorLeft_A = 12
MotorLeft_B = 11
# MotorLeft_PWM = 36
MotorLeft_PWM = 35

MotorRight_A = 15
MotorRight_B = 13
# MotorRight_PWM = 38
MotorRight_PWM = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# setup을 미리 해주지 않으면 Pwm을 선언할 수 없어서 한번 미리 setup 해준다.
# (전역변수로 선언하여 다른 모듈에서 사용하기 위함.)
GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# 왼쪽 모터의 전/후진을 인자로 받아 조정하는 함수
def leftMotor(x):
    if x == 'forward':
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    elif x == 'backward':
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)


# 오른쪽 모터의 전/후진을 인자로 받아 조정하는 함수
def rightMotor(x):
    if x == 'forward':
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    elif x == 'backward':
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)


# 구동체의 속도와 주행 시간을 인자로 받아 전진하는 함수
def goForward(speed, running_time):
    # set the left motor to go forward
    leftMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightMotor("forward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed * 1.025)
    # set the running time of the left motor to go forward
    sleep(running_time)


# 구동체의 속도와 주행 시간을 인자로 받아 후진하는 함수
def goBackward(speed, running_time):
    leftMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightMotor("backward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed * 1.025)
    # set the running time of the left motor to go forward
    sleep(running_time)


# 멈추라는 명령이 있기 전까지 인자로 받은 속도로 계속 전진하는 함수
def goForwardAny(speed):
    # set the left motor to go forward
    leftMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightMotor("forward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed * 1.025)
    # set the running time of the left motor to go forward


# 멈추라는 명령이 있기 전까지 인자로 받은 속도로 계속 후진하는 함수
def goBackwardAny(speed):
    leftMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightMotor("backward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed * 1.025)
    # set the running time of the left motor to go forward


# 구동체를 멈추는 함수
def stopCar():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # right motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


# 테스트용
# mission has been started as below
if __name__ == "__main__":
    # set up GPIO mode as BOARD
    # baseSetup()
    try:
        # setup and initialize the left motor and right motor
        LeftPwm.start(0)
        RightPwm.start(0)
        # command for forwarding with speed of 40 and time 3 seconds
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
