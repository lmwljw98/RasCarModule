######################################################################
# Date : 2017/12 ~
# Member's Name : 이정우, 이정훈, 장민혁
# Member's ID : 20171676, 20171678, 20171691
# Module name: mazeescape.py
# Purpose: 라인트레이싱을 활용한 미로탈출 시행
######################################################################

# -*- coding: utf-8 -*-

from ForwardBackwardBase import *
from TurningCar import rightPointTurn, leftPointTurn
from Tracking import track
import RPi.GPIO as GPIO
from time import sleep

base_speed = 15


def lineTrace():
    """
    라인트레이싱을 시행하는 함수.
    LED 불이 들어온 상태에 따라 왼쪽 혹은 오른쪽 바퀴의 속도를
    실시간으로 조정하여 방향을 잡는다.

    :return:
    """
    goForwardAny(30)
    while True:
        try:
            led_list = track()  # Black = 0, White = 1 return.

            if led_list[0] and not (led_list[4]):
                LeftPwm.ChangeDutyCycle(base_speed + 75)
                RightPwm.ChangeDutyCycle(base_speed)
            if led_list[1] and not (led_list[3]):
                LeftPwm.ChangeDutyCycle(base_speed + 65)
                RightPwm.ChangeDutyCycle(base_speed)
            if led_list[3] and not (led_list[1]):
                LeftPwm.ChangeDutyCycle(base_speed)
                RightPwm.ChangeDutyCycle(base_speed + 40)
            if led_list[4] and not (led_list[0]):
                LeftPwm.ChangeDutyCycle(base_speed)
                RightPwm.ChangeDutyCycle(base_speed + 60)

            led_list = track()
            mazeSearch(led_list)  # 마지막으로 저장된 led_list를 인자로, 미로탐색을 시행한다.

        except KeyboardInterrupt:
            stopCar()
            GPIO.cleanup()


def inner_led_search(turn_keyword):
    """
    턴할 방향이 정해진 후에 시행되는 함수.
    지속해서 LED를 탐색하며 정해진 방향으로 조금씩 턴을 한다.
    자동차가 선 가운데에 위치되있다면, 종료한다.

    :param turn_keyword:
    :return:
    """
    while True:
        inner_led_list = track()
        print(inner_led_list)
        if turn_keyword == "left":  # "left"가 인자로 넘어온 경우, 왼쪽으로 턴을 진행한다.
            leftPointTurn(28, 0.5)
        elif turn_keyword == "right":  # "right"가 인자로 넘어온 경우, 오른쪽으로 턴을 진행한다.
            rightPointTurn(28, 0.5)
        if not inner_led_list[2]:
            goForwardAny(30)
            break


def mazeSearch(led_list):
    """
    미로탐색을 진행하는 함수.
    우수법을 기준으로 작성.
    U턴, 좌회전, 우회전을 해야하는 경우의 조건에 따라 상황에 맞는 행동을 취한다.

    :param led_list:
    :return:
    """
    try:
        if led_list[0] and led_list[1] and led_list[2] and led_list[3] and led_list[4]:
            # 더 이상 길이 없는 경우 (1, 1, 1, 1, 1)
            print("u")  # For debugging
            print(led_list)  # For debugging
            stopCar()
            sleep(1)
            goForward(37, 0.5)
            inner_led_search("left")
            return 0  # For function escape

        elif led_list[0] and led_list[1] and not led_list[2] and not led_list[3] and not led_list[4]:
            # 왼쪽에 길이 없고 오른쪽에만 길이 있는 경우 (1, 1, 0, 0, 0)
            print("right")  # For debugging
            print(led_list)  # For debugging
            stopCar()
            sleep(1)
            goForward(37, 0.5)
            inner_led_search("right")
            return 0  # For function escape

        elif not led_list[0] and not led_list[1] and not led_list[2] and led_list[3] and led_list[4]:
            # 오른쪽에 길이 없고 왼쪽에만 길이 있는 경우 (0, 0, 0, 1, 1)
            print("left")  # For debugging
            print(led_list)  # For debugging
            stopCar()
            sleep(1)
            goForward(37, 0.5)

            # 멈춰선 후 앞으로 조금 이동하였을 때, 길이 없는 경우 좌회전, 있을 경우 직진한다.
            check = track()
            if check[2]:
                inner_led_search("left")
                return 0  # For function escape
            else:
                goForwardAny(30)
                return 1  # For function escape

        elif not led_list[0] and not led_list[1] and not led_list[2] and not led_list[3] and not led_list[4]:
            # 양쪽에 모두 길이 있을 경우 (0, 0, 0, 0, 0)
            print("all")  # For debugging
            print(led_list)  # For debugging
            stopCar()
            sleep(1)
            goForward(37, 0.5)
            inner_led_search("right")
            return 0  # For function escape

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    try:
        LeftPwm.start(0)
        RightPwm.start(0)
        goForward(base_speed, 0.3)
        lineTrace()

    except KeyboardInterrupt:
        stopCar()
        GPIO.cleanup()
