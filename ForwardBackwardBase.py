# 기본적인 Setup 함수와 전진, 후진이 포함되어 있는 모듈

import RPi.GPIO as GPIO
from time import sleep

# Global Variables
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# 기본적인 세팅
def baseSetup():
    # set up GPIO mode as BOARD
    GPIO.setmode(GPIO.BOARD)

    # set GPIO warnings as false
    GPIO.setwarnings(False)

    GPIO.setup(MotorLeft_A, GPIO.OUT)
    GPIO.setup(MotorLeft_B, GPIO.OUT)
    GPIO.setup(MotorLeft_PWM, GPIO.OUT)

    GPIO.setup(MotorRight_A, GPIO.OUT)
    GPIO.setup(MotorRight_B, GPIO.OUT)
    GPIO.setup(MotorRight_PWM, GPIO.OUT)


# 왼쪽 모터의 전후진 상태 세팅
def leftMotor(x):
    if x == 'forward':
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif x == 'backward':
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)


# 오른쪽 모터의 전후진 상태 세팅
def rightMotor(x):
    if x == 'forward':
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif x == 'backward':
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)


# 지정한 속도와 지정한 시간만큼 앞으로 전진하는 함수
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
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(running_time)


# 지정한 속도와 지정한 시간만큼 뒤로 후진하는 함수
def goBackward(speed, running_time):
    leftMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightMotor("backward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(running_time)


# 지정한 속도로 계속 전진할 수 있도록 하는 함수
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
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(0.00001)


# 지정한 속도로 계속 후진할 수 있도록 하는 함수
def goBackwardAny(speed):
    leftMotor("backward")
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightMotor("backward")
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(0.0001)


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


# mission has been started as below
if __name__ == "__main__":
    baseSetup()
    try:
        # setup and initialize the left motor and right motor
        LeftPwm.start(0)
        RightPwm.start(0)
        # command for forwarding with speed of 40 and time 3 seconds
        goForward(40, 3)
        sleep(1)
        goBackward(40, 3)
        sleep(1)
        # command for stop
        stopCar()

    # when the Ctrl+C key has been pressed,
    # the moving object will be stopped
    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()
