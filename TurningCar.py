from ForwardBackwardBase import *
import RPi.GPIO as GPIO
from time import sleep


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


if __name__ == "__main__":
    baseSetup()
    try:
        LeftPwm.start(0)
        RightPwm.start(0)

        rightSwingTurn(30, 2)
        goForward(30, 2)
        LeftSwingTurn(30, 2)
        goBackward(30, 2)

        rightPointTurn(30, 2)
        goForward(30, 2)
        leftPointTurn(30 ,2)
        goBackward(30, 2)

    except KeyboardInterrupt:
        stopCar()