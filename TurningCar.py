from ForwardBackwardBase import *
import RPi.GPIO as GPIO
from time import sleep


def rightSwingTurn(speed, running_time):
    leftMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.LOW)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(0)

    sleep(running_time)

def leftSwingTurn(speed, running_time):
    rightMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


def rightPointTurn(speed, running_time):
    leftMotor("forward")
    rightMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


def leftPointTurn(speed, running_time):
    leftMotor("backward")
    rightMotor("forward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

    sleep(running_time)


if __name__ == "__main__":
    # set up GPIO mode as BOARD
    GPIO.setmode(GPIO.BOARD)
    baseSetup()
    LeftPwm = leftPWM()
    RightPwm = rightPWM()

    try:
        LeftPwm.start(0)
        RightPwm.start(0)

        rightSwingTurn(60, 2)
        goForward(30, 2)
        LeftSwingTurn(60, 2)
        goBackward(30, 2)

        rightPointTurn(60, 2)
        goForward(30, 2)
        leftPointTurn(60, 2)
        goBackward(30, 2)

    except KeyboardInterrupt:
        stopCar()